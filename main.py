from fastapi import FastAPI
app = FastAPI(
    title="My Developer Profile API",
    description="My personal API for profile, skills, projects and learning information",
    version="1.0.0"
)
# HOME ENDPOINT
@app.get("/")
def home():
    return {
        "message": "Welcome to My Developer Profile API"
    }
# PROFILE ENDPOINT
@app.get("/profile")
def get_profile():
    return {
        "name": "Varun Kumar",
        "role": "SAP Integration Developer",
        "location": "India",
        "skills": [
            "SAP CPI",
            "SAP Integration Suite",
            "SAP API Management",
            "Postman",
            "Python"
        ]
    }
# GET ALL SKILLS
@app.get("/skills")
def get_skills():
    return {
        "skills": [
            {
                "name": "SAP CPI",
                "level": "Learning"
            },
            {
                "name": "SAP API Management",
                "level": "Learning"
            },
            {
                "name": "Python",
                "level": "Learning"
            },
            {
                "name": "Postman",
                "level": "Learning"
            }
        ]
    }
# GET ONE SKILL USING PATH PARAMETER
@app.get("/skills/{skill_name}")
def get_skill(skill_name: str):
    skills = {
        "sap-cpi": {
            "name": "SAP CPI",
            "level": "Learning"
        },

        "api-management": {
            "name": "SAP API Management",
            "level": "Learning"
        },

        "python": {
            "name": "Python",
            "level": "Learning"
        },

        "postman": {
            "name": "Postman",
            "level": "Learning"
        }
    }

    skill = skills.get(skill_name.lower())

    if skill:
        return skill

    return {
        "message": "Skill not found"
    }