import os
import sys
from pathlib import Path
import google.generativeai as genai
from PyPDF2 import PdfReader
from typing import Optional

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent))

# Import config
from config import GEMINI_API_KEY

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file using PyPDF2."""
    text = []
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def analyze_resume(resume_path: str, job_description: str):
    """Analyze a resume against a job description."""
    # Extract text from PDF
    resume_text = extract_text_from_pdf(resume_path)
    
    # Configure Gemini API
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Initialize the model
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # Create the prompt
    prompt = f"""Please analyze this resume against the job description and provide a detailed analysis:

1. ATS Compatibility Score (1-10): Rate how well the resume matches the job requirements
2. Missing Keywords: List important keywords from the job description that are missing from the resume
3. Strengths: Highlight areas where the resume aligns well with the job requirements
4. Areas for Improvement: Suggest specific improvements to better match the job description
5. Overall Feedback: Provide a summary of the resume's effectiveness for this specific role

RESUME CONTENT:
{resume_text}

JOB DESCRIPTION:
{job_description}

Please provide your analysis in a structured format with clear headings for each section."""
    
    # Generate content
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze a resume against a job description')
    parser.add_argument('resume', type=str, help='Path to the resume PDF file')
    parser.add_argument('--job-description', type=str, help='Job description text (or path to a .txt file containing job description)', required=True)
    
    args = parser.parse_args()
    
    # Check if job description is a file path
    job_desc = args.job_description
    if os.path.exists(args.job_description):
        with open(args.job_description, 'r', encoding='utf-8') as f:
            job_desc = f.read()
    
    # Run the analysis
    try:
        analysis = analyze_resume(args.resume, job_desc)
        print("\n" + "="*80)
        print("RESUME ANALYSIS REPORT")
        print("="*80)
        print(analysis)
        print("="*80)
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
