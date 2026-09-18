import streamlit as st
from resume_parser import extract_text_from_pdf
from ranking import rank_resumes
from skill_extractor import extract_skills, find_skill_gaps

st.set_page_config(page_title="AI Resume Screening", page_icon="📄", layout="wide")
st.title("AI Resume Screening & Candidate Ranking")
st.write("Upload resumes, add a job description, and rank candidates using TF-IDF cosine similarity.")

job_description=st.text_area("Job Description",height=220,placeholder="Paste the job description here...")
uploaded_files=st.file_uploader("Upload candidate resumes",type=["pdf"],accept_multiple_files=True)

if st.button("Rank Candidates",type="primary"):
    if not job_description.strip():
        st.warning("Please enter a job description."); st.stop()
    if not uploaded_files:
        st.warning("Please upload at least one PDF resume."); st.stop()

    resumes=[]
    for file in uploaded_files:
        text=extract_text_from_pdf(file)
        if text.strip():
            resumes.append({"name":file.name,"text":text})

    if not resumes:
        st.error("No readable text was found in the uploaded resumes."); st.stop()

    with st.spinner("Ranking resumes..."):
        ranked=rank_resumes(job_description,resumes)

    st.subheader("Candidate Ranking")
    table=ranked[["name","match_score"]].copy()
    table["match_score"]=table["match_score"].map(lambda x:f"{x:.2f}%")
    table.index=range(1,len(table)+1)
    table.index.name="Rank"
    st.dataframe(table,use_container_width=True)

    selected_name=st.selectbox("Select a candidate",ranked["name"].tolist())
    candidate=ranked[ranked["name"]==selected_name].iloc[0]

    col1,col2=st.columns(2)
    with col1: st.metric("Match Score",f"{candidate['match_score']:.2f}%")
    with col2: st.metric("Skills Found",len(extract_skills(candidate["text"])))

    required=extract_skills(job_description)
    found=extract_skills(candidate["text"])
    missing=find_skill_gaps(required,found)

    st.write("### Matching Skills")
    st.write(", ".join(found) if found else "No skills detected.")
    st.write("### Skill Gap")
    st.write(", ".join(missing) if missing else "No skill gaps found.")
    st.write("### Extracted Resume Text")
    st.text_area("Resume text",candidate["text"],height=300,label_visibility="collapsed")
