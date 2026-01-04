# End-to-End-AI-Resume-Screening-System
This project aims to develop an AI-powered system that automates the resume screening process . the system will analyze resumes by extracting key information like skills, experience and education, and compare them  to job requirements . using machine learning algorithms, it will based on how well they match the job description.
## The goal of the project? 

 ✅ Upload Resumes (**PDF or Text**).
 
 ✅ Job Description as input.
 
 ✅ Text analysis.
 
 ✅ calculate matching score.
 
 ✅ Rank Job Aplliers.

# Technology Used
- [Python 3.x](https://www.python.org)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [TD_IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Tensorflow](https://mlflow.org/)
- [React.js](https://react.dev/)
- [Docker](https://www.docker.com/).

  
## 📁 Project Directory Structure

```text
<project root directory>
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI application for handling requests
│   │   ├── models.py             # ML model loading and inference
│   │   ├── preprocessing.py      # Text preprocessing for resumes
│   │   ├── requirements.py       # Job requirements parsing and comparison
│   │   ├── utils.py              # Utility functions (file handling, errors, etc.)
│   │   └── mlflow_tracking.py    # MLflow integration
│   ├── Dockerfile                # Backend Docker config
│   └── requirements.txt          # Backend dependencies
│
├── frontend/
│   ├── public/                   # Static assets
│   ├── src/
│   │   ├── components/           # React components
│   │   ├── App.js                # Main React app
│   │   ├── api.js                # API layer (Axios)
│   │   └── index.js              # Entry point
│   ├── Dockerfile                # Frontend Docker config
│   └── package.json              # Frontend dependencies
│
├── docker-compose.yml            # Multi-container setup
├── .gitignore
└── README.md
```


## **System architecture**
<img width="1006" height="478" alt="Gemini_Generated_Image_z6zhrdz6zhrdz6zh" src="https://github.com/user-attachments/assets/bd91242c-212f-4e8f-ae87-4e57527cdd19" />

 
