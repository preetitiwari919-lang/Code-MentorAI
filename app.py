import streamlit as st
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "codementor.db"

st.set_page_config(page_title="CodeMentor AI", page_icon="💻", layout="wide")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS activity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student TEXT NOT NULL,
                activity TEXT NOT NULL,
                score INTEGER,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()

def save_activity(student, activity, score=None):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO activity (student, activity, score, created_at) VALUES (?, ?, ?, ?)",
            (student, activity, score, datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()

def get_activities(student):
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(
            "SELECT activity, score, created_at FROM activity WHERE student = ? ORDER BY id DESC",
            (student,)
        ).fetchall()

init_db()

st.title("💻 CodeMentor AI")
st.caption("A beginner-friendly Hindi-English Python learning assistant")
st.info("Portfolio prototype: guided explanations, practice questions, code-help tips and local progress tracking. This version does not call a live AI model.")

with st.sidebar:
    st.header("👩‍🎓 Learner profile")
    student = st.text_input("Your name", value="Learner")
    st.caption("Your activity is stored locally in this app's SQLite database.")
    page = st.radio("Navigate", ["Home", "Hindi Python Tutor", "Practice Quiz", "Code Help", "My Progress"])

st.write(f"Welcome, **{student or 'Learner'}**!")

if page == "Home":
    st.subheader("Learn programming one step at a time")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📚 Learn")
        st.write("Understand Python concepts with simple English and Hindi explanations.")
        st.markdown("### 🧩 Practise")
        st.write("Answer beginner questions and check your understanding.")
    with c2:
        st.markdown("### 🛠️ Debug")
        st.write("Explore common Python errors and ways to fix them.")
        st.markdown("### 📈 Track")
        st.write("Record quiz attempts and review your learning activity.")
    st.warning("Learning tip: Try writing the code yourself before looking at an explanation.")

elif page == "Hindi Python Tutor":
    st.subheader("📚 Hindi-English Python Tutor")
    topics = {
        "Variables": (
            "A variable stores a value so that a program can use it later.",
            "Variable ek naam hai jisme hum value store karte hain.",
            "name = 'Preeti'\nage = 25\nprint(name)\nprint(age)"
        ),
        "If / Else": (
            "An if/else statement lets a program make a decision.",
            "if/else program ko condition ke basis par decision lene deta hai.",
            "marks = 75\nif marks >= 50:\n    print('Pass')\nelse:\n    print('Try again')"
        ),
        "For Loops": (
            "A for loop repeats code for each item in a sequence.",
            "for loop kisi sequence ke har item ke liye code repeat karta hai.",
            "for number in range(1, 6):\n    print(number)"
        ),
        "Functions": (
            "A function is a reusable block of code that performs a task.",
            "Function code ka reusable block hota hai jo ek particular kaam karta hai.",
            "def greet(name):\n    return 'Hello ' + name\n\nprint(greet('Aarya'))"
        ),
        "Lists": (
            "A list stores multiple items in one ordered collection.",
            "List ek ordered collection hai jisme multiple values store kar sakte hain.",
            "fruits = ['apple', 'mango', 'banana']\nprint(fruits[0])"
        ),
        "Dictionaries": (
            "A dictionary stores information as key-value pairs.",
            "Dictionary data ko key-value pairs ke form mein store karti hai.",
            "student = {'name': 'Aarya', 'grade': 2}\nprint(student['name'])"
        )
    }
    topic = st.selectbox("Choose a topic", list(topics.keys()))
    english, hindi, example = topics[topic]
    st.markdown(f"### {topic}")
    st.write("**English:** " + english)
    st.write("**Hindi:** " + hindi)
    st.code(example, language="python")
    if st.button("Mark topic as studied"):
        save_activity(student or "Learner", f"Studied: {topic}")
        st.success("Your learning activity has been saved.")

elif page == "Practice Quiz":
    st.subheader("🧩 Python Beginner Quiz")
    questions = [
        ("Which symbol is used for comments in Python?", ["//", "#", "<!--"], 1,
         "The # symbol starts a single-line comment in Python."),
        ("What does len([10, 20, 30]) return?", ["2", "3", "30"], 1,
         "len() returns the number of items. There are three items."),
        ("Which data type stores True or False?", ["bool", "str", "list"], 0,
         "bool is Python's Boolean data type."),
        ("Which keyword defines a function?", ["function", "define", "def"], 2,
         "Python uses the def keyword to define a function."),
        ("What does range(3) produce in a loop?", ["0, 1, 2", "1, 2, 3", "3 only"], 0,
         "range(3) produces 0, 1 and 2.")
    ]
    with st.form("quiz_form"):
        answers = []
        for i, (question, options, correct, explanation) in enumerate(questions):
            st.markdown(f"**{i+1}. {question}**")
            answers.append(st.radio("Choose an answer:", options, key=f"q{i}", index=None))
        submitted = st.form_submit_button("Check my answers")
    if submitted:
        score = 0
        for answer, (question, options, correct, explanation) in zip(answers, questions):
            if answer == options[correct]:
                score += 1
        st.metric("Your score", f"{score} / {len(questions)}")
        for i, (answer, q) in enumerate(zip(answers, questions)):
            question, options, correct, explanation = q
            if answer == options[correct]:
                st.success(f"Question {i+1}: Correct!")
            else:
                st.error(f"Question {i+1}: Correct answer: {options[correct]}")
            st.caption(explanation)
        save_activity(student or "Learner", "Python beginner quiz", score)
        st.success("Your quiz result has been saved.")

elif page == "Code Help":
    st.subheader("🛠️ Beginner Code Help")
    st.write("Choose a common Python error to see what it means and how to investigate it.")
    errors = {
        "SyntaxError": (
            "Python cannot understand the structure of the code.",
            "Check spelling, brackets, quotes, colons and indentation.",
            "if age >= 18:\n    print('Adult')"
        ),
        "NameError": (
            "The program is using a name that has not been defined.",
            "Check variable spelling and make sure the variable is created before use.",
            "student_name = 'Aarya'\nprint(student_name)"
        ),
        "TypeError": (
            "An operation is being used with an incompatible type.",
            "Check the data types. Convert values when appropriate.",
            "age = 10\nprint('Age: ' + str(age))"
        ),
        "IndentationError": (
            "Python indentation is inconsistent or missing.",
            "Use consistent indentation, normally four spaces inside a code block.",
            "for number in range(3):\n    print(number)"
        ),
        "IndexError": (
            "The code is trying to access a list position that does not exist.",
            "Check the list length and remember that Python indexes start at zero.",
            "items = ['pen', 'book']\nprint(items[1])"
        )
    }
    chosen = st.selectbox("Select an error", list(errors.keys()))
    meaning, fix, example = errors[chosen]
    st.markdown(f"**Meaning:** {meaning}")
    st.markdown(f"**How to investigate:** {fix}")
    st.code(example, language="python")
    st.caption("Tip: Read the final line of a traceback first, then inspect the line number shown.")

elif page == "My Progress":
    st.subheader("📈 My Learning Progress")
    rows = get_activities(student or "Learner")
    if not rows:
        st.info("No activity recorded yet. Study a topic or complete the quiz to see your progress.")
    else:
        quiz_scores = [r[1] for r in rows if r[1] is not None]
        col1, col2 = st.columns(2)
        col1.metric("Activities completed", len(rows))
        col2.metric("Quiz attempts", len(quiz_scores))
        if quiz_scores:
            st.metric("Best quiz score", f"{max(quiz_scores)} / 5")
        st.markdown("### Recent activity")
        for activity, score, created in rows:
            detail = f" — Score: {score}/5" if score is not None else ""
            st.write(f"• **{activity}**{detail}  \n  <small>{created}</small>", unsafe_allow_html=True)
        st.caption("Progress is stored in a local SQLite database for this prototype.")
