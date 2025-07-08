from fastapi import FastAPI
from analyzer import ResumeAnalyzer
from generator import ResumeGenerator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoResume - Your intelligent resume analyzer and generator!"}

@app.post("/analyze/")
def analyze_resume(resume_text: str):
    analyzer = ResumeAnalyzer()
    analysis_result = analyzer.analyze_resume(resume_text)
    return analysis_result

@app.post("/generate/")
def generate_resume(job_title: str, job_description: str):
    generator = ResumeGenerator()
    new_resume = generator.generate_resume(job_title, job_description)
    return new_resume

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)