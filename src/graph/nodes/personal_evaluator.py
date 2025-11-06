from typing import List
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from src.utils.llm_utils import get_llm
from src.graph.state.graph_state import ResumeState

class PersonalInfo(BaseModel):
    name: str
    email: str
    phone: str
    languages: List[str]

def personal_info_extractor(state: ResumeState) -> ResumeState:
    print("Personal Info Extractor called")

    resume_text = state["resume_text"]
    llm = get_llm().with_structured_output(PersonalInfo)

    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant that extracts **personal information** from a resume.

Based only on the resume text below, extract:
1. Candidate’s full name.
2. Candidate’s email address.
3. Candidate’s phone number (with country code if available).
4. Languages the candidate speaks or writes (like English, Hindi, French, etc.).

If some field is missing, assign null to that field.

Return only this JSON object:
- name: string
- email: string
- phone: string
- languages: string[]

Resume Text:
{resume}
""")

    messages = prompt.format_messages(resume=resume_text)
    result: PersonalInfo = llm.invoke(messages)

    # Return only updated fields
    return {
        "name": result.name,
        "email": result.email,
        "phone_number": result.phone,
        "languages": list(result.languages or []),
    }