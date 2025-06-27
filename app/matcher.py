import json
import os
from difflib import SequenceMatcher
from typing import List, Dict, Tuple
from pathlib import Path

# Load config
CONFIG_PATH = Path("config.json")
if not CONFIG_PATH.exists():
    raise FileNotFoundError("Missing config.json. Cannot start service.")

with open(CONFIG_PATH) as f:
    CONFIG = json.load(f)

# Load students data
STUDENTS_PATH = Path("data/students.json")
if not STUDENTS_PATH.exists():
    raise FileNotFoundError("Missing data/students.json.")

with open(STUDENTS_PATH) as f:
    STUDENTS = json.load(f)

def string_similarity(a: str, b: str) -> float:
    """Returns a similarity ratio between 0 and 1"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def jaccard_similarity(list1: List[str], list2: List[str]) -> float:
    set1, set2 = set(list1), set(list2)
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union) if union else 0.0

def compute_match_score(input_student: Dict, candidate: Dict, config: Dict) -> Tuple[float, Dict]:
    # Goal similarity
    goal_sim = string_similarity(input_student["goal"], candidate["goal"])
    goal_score = goal_sim * config["boost_goal_match"]

    # Study time match
    study_time_match = input_student["preferred_study_time"] == candidate["preferred_study_time"]
    study_time_score = config["study_time_weight"] if study_time_match else 0.0

    # Study type match
    study_type_match = input_student["study_type"] == candidate["study_type"]
    study_type_score = config["study_type_weight"] if study_type_match else 0.0

    # Personality overlap
    personality_sim = jaccard_similarity(input_student["personality"], candidate["personality"])
    personality_score = personality_sim * config["personality_weight"]

    # Total score
    total_score = goal_score + study_time_score + study_type_score + personality_score
    max_possible_score = (
        config["boost_goal_match"]
        + config["study_time_weight"]
        + config["study_type_weight"]
        + config["personality_weight"]
    )
    normalized_score = round(total_score / max_possible_score, 2)

    reasoning = {
        "goal_similarity": round(goal_sim, 2),
        "study_time_match": study_time_match,
        "study_type_match": study_type_match,
        "personality_overlap": list(set(input_student["personality"]) & set(candidate["personality"]))
    }

    return normalized_score, reasoning

def find_best_match(input_student: Dict) -> Dict:
    best_match = None
    best_score = 0
    best_reasoning = {}

    for candidate in STUDENTS:
        if candidate["student_id"] == input_student["student_id"]:
            continue  # skip self

        score, reasoning = compute_match_score(input_student, candidate, CONFIG)
        if CONFIG["log_match_details"]:
            print(f"Match candidate {candidate['student_id']} scored {score}")

        if score > best_score:
            best_score = score
            best_match = candidate
            best_reasoning = reasoning

    if best_score < CONFIG["minimum_match_score"] or best_match is None:
        return {
            "matched_student_id": None,
            "match_score": 0.0,
            "reasoning": {}
        }

    return {
        "matched_student_id": best_match["student_id"],
        "match_score": best_score,
        "reasoning": best_reasoning
    }
