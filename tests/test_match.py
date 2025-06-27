import json
import requests
import time
import os

# Adjust paths as needed
STUDENT_DATA_PATH = os.path.join("data", "students.json")
MATCH_ENDPOINT = "http://127.0.0.1:8000/match"

# Load student dataset
with open(STUDENT_DATA_PATH, "r") as f:
    students = json.load(f)

total_students = len(students)
total_time = 0
failures = 0

print(f"🔍 Testing {total_students} students...")

for i, student in enumerate(students):
    payload = {
        "student_id": student["student_id"],
        "goal": student["goal"],
        "preferred_study_time": student["preferred_study_time"],
        "study_type": student["study_type"],
        "personality": student["personality"]
    }

    start = time.time()
    try:
        response = requests.post(MATCH_ENDPOINT, json=payload)
        elapsed = time.time() - start
        total_time += elapsed

        if response.status_code == 200:
            data = response.json()
            score = data.get("match_score")
            match_id = data.get("matched_student_id")
            print(f"{i+1:04d}. ✅ ID: {student['student_id']} → {match_id}, Score: {score:.2f}, Time: {elapsed:.3f}s")
        else:
            failures += 1
            print(f"{i+1:04d}. ❌ Failed match, status code: {response.status_code}")
    except Exception as e:
        failures += 1
        print(f"{i+1:04d}. ❌ Exception: {str(e)}")

# Summary
print("\n✅ Done.")
print(f"🧪 Total students tested: {total_students}")
print(f"❌ Failures: {failures}")
print(f"⏱️ Total time: {total_time:.2f} seconds")
print(f"⚡ Average per match: {total_time / total_students:.4f} seconds")
