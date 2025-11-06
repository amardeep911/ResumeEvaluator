from typing import TypedDict

class ResumeState(TypedDict):
    pdf_path: str
    resume_text: str
    skills_section: str
    experience_section: str
    projects_section: str
    job_description: str
    skills_score: float
    experience_score: float
    project_score: float
    education_score: float
    final_score: float
    decision: str
    analysis_summary: str
