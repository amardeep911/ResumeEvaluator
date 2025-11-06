from langgraph.graph import StateGraph, START, END

from src.graph.state.graph_state import ResumeState
from src.graph.nodes.pdf_loader import pdf_loader

def create_graph():
    graph = StateGraph(ResumeState)

    graph.add_node("pdf_loader", pdf_loader)

    graph.add_edge(START, "pdf_loader")
    graph.add_edge("pdf_loader", END)

    compile_graph = graph.compile()

    return compile_graph