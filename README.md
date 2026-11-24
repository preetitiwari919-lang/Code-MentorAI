# CodeMentor AI 💻

**A beginner-friendly Hindi-English Python learning assistant built with Python and Streamlit.**

CodeMentor AI is an educational portfolio prototype designed to support beginner learners with concept explanations, coding practice, debugging guidance and simple progress tracking.

## Features

- Hindi-English explanations of beginner Python concepts
- Python multiple-choice practice quiz with answer explanations
- Beginner-friendly guidance for common Python errors
- Learner activity and quiz score tracking using SQLite
- Simple interactive web interface built with Streamlit

## Technology

- Python
- Streamlit
- SQLite
- Git and GitHub

## Run locally

1. Install Python 3.10 or later.
2. Clone this repository or download the project.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the app:

   ```bash
   streamlit run app.py
   ```

## Project structure

```text
CodeMentorAI/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml
```

## Learning purpose and scope

This is an early-stage educational prototype. Its tutor explanations and error guidance are predefined examples; it does not currently connect to a live LLM or AI API, execute arbitrary learner-submitted code, or provide production-grade authentication.

## Planned improvements

- Connect a suitable LLM API for conversational Hindi-English tutoring
- Add more Python and DSA exercises
- Expand teacher and learner dashboards
- Add FastAPI backend endpoints
- Add richer learner feedback and reporting

## Author

**Preeti Tiwari**  
Technology educator | Python learning | AI-assisted education

This project was created as a practical learning and portfolio project to explore how simple software tools can support programming education.
