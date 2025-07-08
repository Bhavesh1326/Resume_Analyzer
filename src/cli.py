import typer
import pdfplumber
import sys
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import google.generativeai as genai
import json
from typing import Optional

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from config import SQLALCHEMY_DATABASE_URL, GEMINI_API_KEY
from src.db.models import User, Resume, JobDescription, Analysis

app = typer.Typer()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

@app.command()
def add_user(name: str, email: str):
    """Add a new user."""
    session = SessionLocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.close()
    typer.echo(f"User '{name}' added.")

@app.command()
def add_resume(user_id: int, file_path: str):
    """Add a new resume for a user from a PDF file."""
    with pdfplumber.open(file_path) as pdf:
        content = "\n".join(page.extract_text() or "" for page in pdf.pages)
    session = SessionLocal()
    resume = Resume(user_id=user_id, content=content)
    session.add(resume)
    session.commit()
    session.close()
    typer.echo(f"Resume from '{file_path}' added for user ID {user_id}.")

@app.command()
def add_job(title: str, description: str):
    """Add a new job description."""
    session = SessionLocal()
    job = JobDescription(title=title, description=description)
    session.add(job)
    session.commit()
    session.close()
    typer.echo(f"Job '{title}' added.")

@app.command()
def list_users():
    """List all users."""
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        typer.echo(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    session.close()

@app.command()
def list_resumes():
    """List all resumes."""
    session = SessionLocal()
    resumes = session.query(Resume).all()
    for resume in resumes:
        typer.echo(f"ID: {resume.id}, User ID: {resume.user_id}, Created: {resume.created_at}, Version: {resume.version}")
    session.close()

@app.command()
def list_jobs():
    """List all job descriptions."""
    session = SessionLocal()
    jobs = session.query(JobDescription).all()
    for job in jobs:
        typer.echo(f"ID: {job.id}, Title: {job.title}")
    session.close()

@app.command()
def analyze_resume(resume_id: int, job_description_id: Optional[int] = None):
    """Analyze a resume's content for grammar, keywords, ATS score, etc."""
    if not GEMINI_API_KEY:
        typer.echo("Error: GEMINI_API_KEY not found in config. Please set it first.")
        return

    session = SessionLocal()
    resume = session.query(Resume).filter_by(id=resume_id).first()
    if not resume:
        typer.echo(f"Error: Resume with ID {resume_id} not found.")
        session.close()
        return

    job_description = None
    if job_description_id:
        job_description = session.query(JobDescription).filter_by(id=job_description_id).first()
        if not job_description:
            typer.echo(f"Error: Job description with ID {job_description_id} not found.")
            session.close()
            return

    # Prepare the analysis prompt
    prompt = """Please analyze this resume against the job description and provide a detailed analysis:

1. ATS Compatibility Score (1-10): Rate how well the resume matches the job requirements
2. Missing Keywords: List important keywords from the job description that are missing from the resume
3. Strengths: Highlight areas where the resume aligns well with the job requirements
4. Areas for Improvement: Suggest specific improvements to better match the job description
5. Overall Feedback: Provide a summary of the resume's effectiveness for this specific role

RESUME CONTENT:
""" + resume.content + "\n\n"

    if job_description:
        prompt += "JOB DESCRIPTION:\n" + job_description.description + "\n\n"
    
    prompt += "Please provide your analysis in a structured format with clear headings for each section."

    try:
        # Configure Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Generate content
        response = model.generate_content(prompt)
        analysis = response.text

        # Create and store the analysis
        new_analysis = Analysis(
            resume_id=resume_id,
            job_description_id=job_description_id if job_description else None,
            score=0,  # Gemini doesn't provide a score directly
            feedback=analysis,
            analysis_type="general",
            keywords="",  # We'll need to parse keywords from the response
            ats_score=0  # Gemini doesn't provide ATS score directly
        )
        session.add(new_analysis)
        session.commit()
        
        typer.echo(f"Analysis completed for resume ID {resume_id}")
        typer.echo(f"Feedback: {analysis}")        
    except Exception as e:
        typer.echo(f"Error during analysis: {str(e)}")
        session.rollback()
    
    finally:
        session.close()

if __name__ == "__main__":
    app()