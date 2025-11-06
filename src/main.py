from src.graph.stategraph import create_graph

graph = create_graph()

result = graph.invoke({
    "pdf_path": "/Users/hardik/PycharmProjects/ResumeEvaluator/src/data/HardikResumeUpdated.pdf"
})


# print(result["resume_text"])
print(result["skills_score"])
print(result["role_inferred"])
print(result["matched_skills"])
print(result["missing_skills"])

print("-----------")
print(result["name"])
print(result["email"])
print(result["phone_number"])
print(result["languages"])

