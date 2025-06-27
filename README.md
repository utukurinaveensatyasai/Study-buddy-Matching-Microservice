# 📚 Study Buddy Matching Microservice

A lightweight Python-based microservice that recommends a compatible study buddy based on academic goals, study preferences, and personality traits — fully offline and explainable.

---

## 🚀 Features

- 🔍 **Deterministic Offline Matching**
- 🧠 Hybrid Scoring (Goals, Study Time, Study Type, Personality)
- 📊 Normalized Match Score (0–1)
- ⚙️ Configurable Logic via `config.json`
- 🧪 FastAPI-based REST API with test coverage
- 🐳 Fully Dockerized and Portable

---

## 📦 Project Structure

study-buddy/
├── app/
│ ├── main.py # FastAPI server
│ └── matcher.py # Matching logic
├── data/
│ └── students.json # Offline candidate dataset
├── tests/
│ └── test_match.py # Unit tests
├── config.json # Thresholds and weights
├── Dockerfile # For containerization
├── requirements.txt # Python dependencies
├── schema.json # Output validation schema
└── README.md


---

## 📥 API Usage

### ➤ POST `/match`

Find the best matching study buddy.

#### ✅ Request Payload

```json
{
  "student_id": "stu_9482",
  "goal": "Crack GATE 2025",
  "preferred_study_time": "early_morning",
  "study_type": "visual",
  "personality": ["focused", "introvert"]
}

➤ GET /health
Check service health.
{ "status": "ok" }

➤ GET /version
Returns config version and minimum score.

🛠️ Setup & Run
🔧 Without Docker
pip install -r requirements.txt
uvicorn app.main:app --reload

Access the server at: http://localhost:8000

🐳 With Docker

docker build -t study-buddy .
docker run -p 8000:8000 study-buddy

✅ Running Tests

pytest tests/

⚙️ Config (config.json)
Controls matching weights and thresholds:


{
  "version": "1.0.0",
  "minimum_match_score": 0.6,
  "boost_goal_match": 1.5,
  "personality_weight": 1.0,
  "study_time_weight": 1.2,
  "study_type_weight": 1.0,
  "log_match_details": true
}
📌 Constraints
No GPT, external API, or vector embeddings

All logic must be local

Must return scores between 0–1

Schema-compliant output with full explanation

👨‍💻 Author
Utukuri Naveen Satya Sai
Intern at Turtil AI, Hyderabad 🧠

📚 License
MIT License — free to use and modify.


---

✅ You're now fully set to run your project end-to-end.

Would you like a **zip folder of everything**, or are you ready to test the code locally and let me know if you encounter any issues?
