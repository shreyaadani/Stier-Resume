import streamlit as st
from resume_parser import extract_text_from_pdf, split_into_sections
from job_matcher import match_resume_to_job
from ats_score import score_resume
from visualizer import plot_match_report

st.title("📄 Resume Analyzer + ATS Score")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    text = extract_text_from_pdf(uploaded_file)
    sections = split_into_sections(text)

    st.subheader("🧾 Extracted Sections")
    for name, content in sections.items():
        st.markdown(f"**{name.title()}:**\n{content[:300]}...")

    st.subheader("📊 Match Report")
    match = match_resume_to_job(sections, job_description)
    for k, v in match.items():
        st.write(f"{k.title()}: {v}")

    st.pyplot(plot_match_report(match))

    st.subheader("📈 ATS Score Estimate")
    score, breakdown = score_resume(text, job_description)
    st.metric("ATS Score", f"{score}%")
    st.write("Breakdown:")
    for k, v in breakdown.items():
        st.write(f"{k}: {v}%")
