from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Question
from models import QuestionModel

router = APIRouter()

# Create a new question
@router.post("/questions/", response_model=QuestionModel)
def create_question(question_data: dict):
    db: Session = SessionLocal()

    validTypes = ["MC", "SA", "Rearrange", "Prompt"]

    if question_data['type'] not in validTypes:
        raise HTTPException(status_code=404, detail="Not a valid question type")


    elif question_data['type'] == "MC":
        db_question = Question(collection=question_data['collection'], 
                           question=question_data['question'], 
                           type=question_data['type'],
                           op1=question_data['op1'],
                           op2=question_data['op2'],
                           op3=question_data['op3'],
                           op4=question_data['op4'],
                           answer=question_data['answer'])
    elif question_data['type'] == "SA" or question_data['type'] == "Rearrange":
        db_question = Question(collection=question_data['collection'], 
                    question=question_data['question'], 
                    type=question_data['type'],
                    answer=question_data['answer'])
    elif question_data['type'] == "Prompt":
        db_question = Question(collection=question_data['collection'], 
            question=question_data['question'], 
            type=question_data['type'],
            prompt=question_data['prompt'],
            answer=question_data['answer'])
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
    
    db_question.question = question_data['question']
    db_question.prompt = question_data['prompt']
    db_question.op1 = question_data['op1']
    db_question.op2 = question_data['op2']
    db_question.op3 = question_data['op3']
    db_question.op4 = question_data['op4']
    db_question.answer = question_data['answer']

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
