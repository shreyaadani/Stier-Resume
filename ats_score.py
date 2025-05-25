import re

def score_resume(resume_text, job_description):
    jd_keywords = set(job_description.lower().split())
    resume_keywords = set(resume_text.lower().split())

    keyword_hits = jd_keywords & resume_keywords
    keyword_score = len(keyword_hits) / len(jd_keywords) if jd_keywords else 0

    sections = ["education", "experience", "skills", "contact", "projects"]
    section_score = sum(1 for section in sections if section in resume_text.lower()) / len(sections)

    word_count = len(resume_text.split())
    length_score = 1.0 if 300 <= word_count <= 800 else 0.5 if word_count < 300 else 0.3

    structure_score = 1.0 if re.search(r'(education|experience|projects|skills)', resume_text.lower()) else 0.5

    final_score = (0.4 * keyword_score + 0.2 * section_score + 0.2 * length_score + 0.2 * structure_score)
    
    return round(final_score * 100, 2), {
        "Keyword Match": round(keyword_score * 100, 2),
        "Sections Found": round(section_score * 100, 2),
        "Length Appropriateness": round(length_score * 100, 2),
        "Structure Score": round(structure_score * 100, 2)
    }
