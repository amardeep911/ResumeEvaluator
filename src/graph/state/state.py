# src/graph/state/state.py
"""
ResumeState Definition
=======================

Defines the global state structure for the LangGraph pipeline.
Every node (pdf_loader, preprocessing, skills_evaluator, etc.)
reads/writes to this shared state.
"""

from typing import TypedDict, List, Optional

class ResumeState(TypedDict, total=False):
    # ----------------------
    # A. Ingestion
    # ----------------------
    pdf_path: Optional[str]
    resume_text: Optional[str]

    # ----------------------
    # B. Preprocessing
    # ----------------------
    skills_section: Optional[str]
    experience_section: Optional[str]
    projects_section: Optional[str]
    education_section: Optional[str]

    # ----------------------
    # C. Evaluation
    # ----------------------
    role_inferred: Optional[str]
    skills_score: Optional[float]
    experience_score: Optional[float]
    project_score: Optional[float]
    education_score: Optional[float]

    matched_skills: Optional[List[str]]
    missing_skills: Optional[List[str]]

    # ----------------------
    # D. Aggregation
    # ----------------------
    final_score: Optional[float]
    decision: Optional[str]
    analysis_summary: Optional[str]

    # ----------------------
    # E. Metadata
    # ----------------------
    resume_metadata: Optional[dict]
