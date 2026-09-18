# AI Resume Screening & Candidate Ranking System

A simple ATS-style application that compares resumes with a job description and ranks candidates using TF-IDF and cosine similarity.

## Features

- Upload multiple PDF resumes
- Paste a job description
- Extract resume text
- Convert text into TF-IDF vectors
- Calculate cosine similarity
- Rank candidates by match score
- Detect common skills
- Show a basic skill gap
- View extracted resume text

## Flow

PDF Resume → Text Extraction → TF-IDF → Cosine Similarity → Match Score → Ranking → Skill Gap

## Files

- `app.py` — Streamlit interface and application flow
- `resume_parser.py` — extracts text from PDF resumes
- `ranking.py` — TF-IDF and cosine similarity
- `skill_extractor.py` — simple skill detection
- `requirements.txt` — Python packages

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

## Learning order

Read `app.py` first, then `resume_parser.py`, `ranking.py`, and finally `skill_extractor.py`.

The project intentionally keeps the code simple so the complete flow can be understood and explained in an interview.

## Limitations

The match score is a text-similarity score, not a hiring probability. Skill detection uses a predefined list. A future version can add embeddings, better skill extraction, DOCX support, experience extraction, education extraction, and a database.

Do not upload real candidate resumes to GitHub because they may contain personal information.
