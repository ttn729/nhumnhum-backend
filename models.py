from pydantic import BaseModel


class QuestionModel(BaseModel):
    id: int
    collection: str
    question: str
    type: str
    prompt: str | None
    op1: str | None
    op2: str | None
    op3: str | None
    op4: str | None
    answer: str
