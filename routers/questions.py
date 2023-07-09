from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Question
from models import QuestionModel

router = APIRouter()

# Create a new question
@router.post("/questions/", response_model=QuestionModel)
def create_question(question_data: dict):
    db: Session = SessionLocal()
    db_question = Question(collection=question_data['collection'], prompt=question_data['prompt'], type=question_data['type'])
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

# Get all questions
@router.get("/questions/", response_model=list[QuestionModel])
def read_questions():
    db: Session = SessionLocal()
    questions = db.query(Question).all()
    return questions


# Get a specific question by ID
@router.get("/questions/{question_id}", response_model=QuestionModel)
def read_question(question_id: int):
    db: Session = SessionLocal()
    question = db.query(Question).filter(Question.id == question_id).first()
    if question is None:
        raise HTTPException(status_code=404, detail="question not found")
    return question


# Update a question
@router.put("/questions/{question_id}", response_model=QuestionModel)
def update_question(question_id: int, question_data: dict):
    db: Session = SessionLocal()
    db_question = db.query(Question).filter(Question.id == question_data['id']).first()
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    db_question.prompt = question_data['prompt']
    db_question.type = question_data['type']
    db.commit()
    db.refresh(db_question)
    return db_question


# Delete an question
@router.delete("/questions/{question_id}")
def delete_question(question_id: int):
    db: Session = SessionLocal()
    question = db.query(Question).filter(Question.id == question_id).first()
    if question is None:
        raise HTTPException(status_code=404, detail="question not found")
    db.delete(question)
    db.commit()
    return {"message": "question deleted"}
