def match_resume_to_job(sectioned_data, job_description):
    job_words = set(job_description.lower().split())
    match = {}
    for section, content in sectioned_data.items():
        section_words = set(content.lower().split())
        count = sum(1 for word in section_words if word in job_words)
        match[section] = f"{count} / {len(section_words)}"
    return match
