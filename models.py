from pydantic import BaseModel


class QuestionModel(BaseModel):
    id: int
    collection: str
    prompt: str
    type: str