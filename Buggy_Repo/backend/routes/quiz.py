
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from db import init_db

router = APIRouter(tags=["quiz"])

class AnswerRequest(BaseModel):
    question_id: int
    answer: str
    score: int

async def get_quiz_collection():
    db = await init_db()
    return db["quiz_collection"]

@router.get("/question")
async def get_question():
    collection = await get_quiz_collection()
    questions = await collection.find().to_list(length=5)
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
    question = random.choice(questions)
    return {
        "id": str(question["_id"]),
        "text": question["text"],
        "options": question["options"]
    }

@router.post("/answer")
async def submit_answer(data: AnswerRequest):
    collection = await get_quiz_collection()
    question = await collection.find_one({"_id": ObjectId(data.question_id)})
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    is_correct = data.answer == question["correct"]
    if is_correct:
        data.score += 10

    return {
        "is_correct": is_correct,
        "correct_answer": question["correct"],
        "score": data.score
    }
