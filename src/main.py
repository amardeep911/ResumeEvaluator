from src.graph.stategraph import create_graph

# pdf_path: str
#     resume_text: str
#     skills_section: str
#     experience_section: str
#     projects_section: str
#     job_description: str
#     skills_score: float
#     experience_score: float
#     project_score: float
#     education_score: float
#     final_score: float
#     decision: str
#     analysis_summary: str
#     skills_score: int
#     matched_skills : Optional[List[str]]
#     missing_skills : Optional[List[str]]
#     role_inferred: str


graph = create_graph()

result = graph.invoke({
    "pdf_path": "your own absolute path to pdf"
})


print(result["resume_text"])
print(result["skills_score"])
print(result["role_inferred"])
print(result["matched_skills"])
print(result["missing_skills"])

