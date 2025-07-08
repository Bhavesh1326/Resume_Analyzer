# Add to backend/main.py
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from fastapi import FastAPI, UploadFile, File, HTTPException, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from pathlib import Path
import json
import google.generativeai as genai
from PyPDF2 import PdfReader
from typing import Dict, Any
from nlp_utils import (
    extract_keywords,
    calculate_keyword_match,
    analyze_skill_gap,
    check_formatting_issues,
    generate_recommendations
)

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, top_n=20):
    doc = nlp(text.lower())
    keywords = [token.lemma_ for token in doc 
               if not token.is_stop 
               and not token.is_punct 
               and token.pos_ in ['NOUN', 'PROPN']]
    return Counter(keywords).most_common(top_n)

def calculate_keyword_match(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    feature_names = vectorizer.get_feature_names_out()
    return dict(zip(feature_names, (tfidf[1] - tfidf[0]).toarray()[0]))

def analyze_skill_gap(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)  # Existing function
    jd_skills = extract_skills(jd_text)
    
    missing_skills = set(jd_skills) - set(resume_skills)
    strong_matches = set(jd_skills) & set(resume_skills)
    
    return {
        "missing_skills": list(missing_skills),
        "matched_skills": list(strong_matches),
        "match_percentage": len(strong_matches) / len(jd_skills) * 100
    }

def get_nlp_analysis(resume_text, job_description):
    # Initialize the Gemini model
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Use the recommended gemini-1.5-flash model
    model_name = 'gemini-1.5-flash'
    print(f"Using model: {model_name}")
    model = genai.GenerativeModel(model_name)
    
    # Perform NLP analysis
    print("Performing NLP analysis...")
    
    # Extract keywords
    resume_keywords = extract_keywords(resume_text, top_n=20)
    jd_keywords = extract_keywords(job_description, top_n=20)
    
    # Calculate keyword match
    keyword_match = calculate_keyword_match(resume_text, job_description)
    
    # Analyze skill gaps
    skill_analysis = analyze_skill_gap(resume_text, job_description)
    
    # Check formatting
    formatting_issues = check_formatting_issues(resume_text)
    
    # Generate recommendations
    recommendations = generate_recommendations(skill_analysis, formatting_issues)
    
    # Create the prompt with additional analysis
    prompt = f"""
    You are an expert resume reviewer. Analyze the following resume against the provided job description and provide a detailed, structured analysis.
    
    JOB DESCRIPTION:
    {job_description}
    
    RESUME:
    {resume_text}
    
    NLP ANALYSIS:
    - Resume Keywords: {', '.join([k[0] for k in resume_keywords[:5]])}
    - Job Description Keywords: {', '.join([k[0] for k in jd_keywords[:5]])}
    - Skill Match Percentage: {skill_analysis['match_percentage']}%
    - Missing Skills: {', '.join(skill_analysis['missing_skills'][:3])}
    
    Provide a detailed analysis in the following JSON format (only output the JSON, no additional text):
    {{
        "match_score": 0-100,  # Numerical score based on how well the resume matches the job description
        "key_skills_matched": ["list", "of", "matching", "skills"],
        "missing_skills": ["list", "of", "missing", "skills"],
        "strengths": ["list", "of", "strengths"],
        "improvement_areas": ["list", "of", "areas", "to", "improve"],
        "suggestions": ["specific", "suggestions", "for", "improvement"],
        "summary": "A brief summary of the overall fit",
        "nlp_analysis": {{
            "keyword_match": {json.dumps(keyword_match)},
            "skill_analysis": {json.dumps(skill_analysis)},
            "formatting_issues": {json.dumps(formatting_issues)},
            "recommendations": {json.dumps(recommendations)}
        }}
    }}
    
    Be specific and provide concrete examples from the resume and job description. 
    Focus on matching skills, experience, and qualifications mentioned in the job description.
    If the resume is a good match, explain why. If not, provide specific, actionable feedback.
    """
    
    # Generate the response
    response = model.generate(prompt)
    
    # Parse the response
    response_json = json.loads(response)
    
    return response_json