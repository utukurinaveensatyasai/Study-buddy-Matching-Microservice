# 📚 Study Buddy Matching Microservice

A lightweight, offline-ready Python-based microservice that intelligently recommends compatible study partners based on academic goals, study preferences, and personality traits. Built with FastAPI, configurable via JSON, and containerized for deployment anywhere.

---

## 🚀 Key Features

- 🔍 **Offline, Deterministic Matching Engine**
- 🧠 **Hybrid Scoring Algorithm** combining:
  - Academic Goals
  - Preferred Study Time
  - Study Type
  - Personality Trait Overlap
- 📊 **Normalized Match Score** between 0.0 and 1.0
- ⚙️ **Fully Configurable** via `config.json`
- 📡 RESTful API with **FastAPI** + OpenAPI Docs
- 🧪 Robust Unit Tests with `pytest`
- 🐳 Dockerized for easy deployment

---

## 📁 Project Structure

```
study-buddy/
├── app/
│   ├── main.py              # FastAPI server and endpoints
│   └── matcher.py           # Core matching logic
├── data/
│   └── students.json        # Offline dataset of student profiles
├── tests/
│   └── test_match.py        # Unit and performance tests
├── config.json              # Configurable weights and thresholds
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker build file
├── schema.json              # Optional output validation schema
└── README.md                # Project documentation
```

---

## 🌐 API Endpoints

### 🔎 `POST /match`
Find the best-matching study buddy for a student.

#### ✅ Request Payload:
```json
{
  "student_id": "stu_9482",
  "goal": "Crack GATE 2025",
  "preferred_study_time": "early_morning",
  "study_type": "visual",
  "personality": ["focused", "introvert"]
}
```

#### ✅ Response:
```json
{
  "matched_student_id": "stu_4312",
  "match_score": 0.84,
  "reasoning": {
    "goal_similarity": 0.9,
    "study_time_match": true,
    "study_type_match": false,
    "personality_overlap": ["focused"]
  }
}
```

---

### 🩺 `GET /health`
Check if the service is running.

```json
{ "status": "ok" }
```

---

### 🧪 `GET /version`
Returns API version and current matching configuration.

```json
{
  "version": "1.0.0",
  "config": {
    "minimum_match_score": 0.6,
    "boost_goal_match": 1.5,
    "personality_weight": 1.0,
    "study_time_weight": 1.2,
    "study_type_weight": 1.0,
    "log_match_details": true
  }
}
```

---

## ⚙️ Configuration: `config.json`

All scoring parameters are centrally configurable:

```json
{
  "version": "1.0.0",
  "minimum_match_score": 0.6,
  "boost_goal_match": 1.5,
  "personality_weight": 1.0,
  "study_time_weight": 1.2,
  "study_type_weight": 1.0,
  "log_match_details": true
}
```

Update these values to fine-tune your matching logic without changing any code.

---

## 🛠️ Setup & Run

### 🔧 Local Development (without Docker)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Access the app at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🐳 Docker Deployment

Build and run the containerized app:
```bash
docker build -t study-buddy .
docker run -p 8000:8000 study-buddy
```

---

## ✅ Testing the Application

Run the full test suite: Ensure on another cmd tab the uvicorn must be run and then on another tab run below for testing 1000 students.
```bash
python -m tests.test_match
```
or



✔️ Validates response structure, matching logic, and performance for 1000 students.

---

## 📌 Project Constraints

- ❌ No usage of GPT or online APIs
- ⚙️ All logic runs locally using `matcher.py`
- 🔒 Schema-compliant output with explanation
- ⚡ Designed to handle 1000 matches under 1 second each

---

## 📚 Author Info

**👤 Utukuri Naveen Satya Sai**  
AI Intern at Turtil, Hyderabad  
📧 22a31a1263@pragati.ac.in

Team Name: **Continuum Craft**  
Partner: **U. Guna Shekar**  
College: LIET

---

## 📝 License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and distribute.

---

## 📎 Final Submission Checklist

✅ Fully working offline matcher  
✅ 1000-student dataset with config  
✅ API tested and documented  
✅ Dockerized deployment  
✅ Report PDF + Explainer video  
✅ Submission zipped with all assets

---

**🚀 Ready to be evaluated for real-world scalability and software engineering standards.**
