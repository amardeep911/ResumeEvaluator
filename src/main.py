from src.graph.stategraph import create_graph

# State Example ()
#     pdf_path: str
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


graph = create_graph()

result = graph.invoke({
    "pdf_path": "Your absolute path goes here"
})

print(result["resume_text"])

