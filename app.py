import streamlit as st
from resume_parser import extract_text_from_pdf, split_into_sections
from job_matcher import match_resume_to_job
from ats_score import score_resume
from visualize import plot_match_report

# --- Sidebar ---
st.sidebar.image("assets/logo.png", use_column_width=True)
st.sidebar.title("📄 Resume Analyzer")
st.sidebar.markdown("Upload your resume and job description to get:")
st.sidebar.markdown("- 🧠 Smart section detection\n- 📈 ATS score\n- 📊 Visual match report")

# --- Main Title ---
st.markdown("<h1 style='text-align: center;'>🚀 Resume Analyzer Dashboard</h1>", unsafe_allow_html=True)
st.markdown("### 📎 Upload your documents below")

# --- File Inputs ---
uploaded_file = st.file_uploader("Resume PDF", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=150)

# --- Run Button ---
if uploaded_file and job_description:
    if st.button("🔍 Run Resume Analysis"):
        with st.spinner("Analyzing your resume..."):

            # Step 1: Extract
            text = extract_text_from_pdf(uploaded_file)
            sections = split_into_sections(text)

            # Step 2: Display Sections
            st.markdown("## 📄 Extracted Sections")
            for name, content in sections.items():
                with st.expander(name.title()):
                    st.write(content[:500] + "..." if len(content) > 500 else content)

            # Step 3: Match Report
            st.markdown("## 📊 Match Report")
            match = match_resume_to_job(sections, job_description)
            for k, v in match.items():
                st.markdown(f"- **{k.title()}**: {v}")

            st.pyplot(plot_match_report(match))

            # Step 4: ATS Score
            st.markdown("## ✅ ATS Score Estimate")
            score, breakdown = score_resume(text, job_description)
            st.metric("ATS Score", f"{score}%")
            st.markdown("**Breakdown:**")
            for k, v in breakdown.items():
                st.markdown(f"- {k}: {v}%")
    else:
        st.info("⬆️ Upload files and press the button to start.")
else:
    st.info("📝 Upload a resume and paste a job description to begin.")
