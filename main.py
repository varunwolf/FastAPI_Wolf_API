from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()
class Skill(BaseModel):
    name: str
    level: str
skills = [
    {
        "name": "SAP CPI",
        "level": "Learning"
    },
    {
        "name": "SAP API Management",
        "level": "First"
    },
    {
        "name": "Python",
        "level": "Second"
    },
    {
        "name": "Postman",
        "level": "Advance"
    },
    {
        "name": "LangChain",
        "level": "Beginner"
    },
    {
        "name": "LangChain",
        "level": "Beginner"
    },
    {
        "name": "LangGraph",
        "level": "Beginner"
    }
]
@app.get("/")
def home():
    return {
        "message": "Welcome to My Developer Profile API"
    }
@app.get("/skills")
def get_skills():
    return {
        "skills": skills
    }
# IMPORTANT:
# This must come BEFORE /skills/{skill_name}
@app.get("/skills/search")
def search_skills(level: str | None = None):

    if level is None:
        return {
            "skills": skills
        }
    filtered_skills = []
    for skill in skills:
        if skill["level"].lower() == level.lower():
            filtered_skills.append(skill)
    return {
        "skills": filtered_skills
    }
# Keep dynamic path AFTER /skills/search
@app.get("/skills/{skill_name}")
def get_skill(skill_name: str):

    for skill in skills:
        if skill["name"].lower() == skill_name.lower():
            return skill

    raise HTTPException(
        status_code=404,
        detail="Skill not found"
    )
@app.post("/skills", status_code=status.HTTP_201_CREATED)
def create_skill(skill: Skill):

    new_skill = {
        "name": skill.name,
        "level": skill.level
    }

    skills.append(new_skill)

    return {
        "message": "Skill created successfully",
        "skill": new_skill
    }