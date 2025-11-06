from langgraph.graph import StateGraph, START, END

from src.graph.state.graph_state import ResumeState
from src.graph.nodes.pdf_loader import pdf_loader
from src.graph.nodes.skills_evaluator import skills_evaluator
from src.graph.nodes.personal_evaluator import personal_info_extractor
def create_graph():
    graph = StateGraph(ResumeState)

    graph.add_node("pdf_loader", pdf_loader)
    graph.add_node("skills_evaluator", skills_evaluator)
    graph.add_node("personal_info_evaluator", personal_info_extractor)

    graph.add_edge(START, "pdf_loader")
    graph.add_edge("pdf_loader", "skills_evaluator")
    graph.add_edge("pdf_loader", "personal_info_evaluator")
    graph.add_edge("skills_evaluator", END)
    graph.add_edge("personal_info_evaluator", END)

    compile_graph = graph.compile()

    return compile_graph