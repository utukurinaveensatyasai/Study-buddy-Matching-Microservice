from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List, Literal

import json
from pathlib import Path

from app.matcher import find_best_match

# Load config
CONFIG_PATH = Path("config.json")
if not CONFIG_PATH.exists():
    raise FileNotFoundError("Missing config.json.")

with open(CONFIG_PATH) as f:
    CONFIG = json.load(f)

app = FastAPI(title="Study Buddy Matcher")

# Pydantic Models
class MatchRequest(BaseModel):
    student_id: str
    goal: str
    preferred_study_time: str
    study_type: str
    personality: List[str] = Field(..., min_items=1)

class MatchReasoning(BaseModel):
    goal_similarity: float
    study_time_match: bool
    study_type_match: bool
    personality_overlap: List[str]

class MatchResponse(BaseModel):
    matched_student_id: Optional[str]
    match_score: float
    reasoning: MatchReasoning

class HealthResponse(BaseModel):
    status: Literal["ok"]

class ConfigSchema(BaseModel):
    version: str = Field(..., example="1.0.0")
    minimum_match_score: float = Field(..., example=0.6)
    boost_goal_match: float = Field(..., example=1.5)
    personality_weight: float = Field(..., example=1.0)
    study_time_weight: float = Field(..., example=1.2)
    study_type_weight: float = Field(..., example=1.0)
    log_match_details: bool = Field(..., example=True)

class VersionResponse(BaseModel):
    version: str = Field(..., example="1.0.0")
    config: ConfigSchema


# Endpoints
@app.get("/health", response_model=HealthResponse, tags=["Utility"])
def health():
    return {"status": "ok"}

@app.get("/version", response_model=VersionResponse, tags=["Utility"])
def version():
    return {
        "version": CONFIG.get("version"),
        "config": ConfigSchema(**CONFIG)
    }

@app.post("/match", response_model=MatchResponse, tags=["Matcher"])
def match(request: MatchRequest):
    try:
        result = find_best_match(request.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
