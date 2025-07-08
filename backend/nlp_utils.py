import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, top_n=20):
    """Extract important keywords from text using spaCy."""
    doc = nlp(text.lower())
    keywords = [token.lemma_ for token in doc 
               if not token.is_stop 
               and not token.is_punct 
               and token.pos_ in ['NOUN', 'PROPN', 'ADJ']]
    return Counter(keywords).most_common(top_n)

def calculate_keyword_match(resume_text, jd_text):
    """Calculate keyword similarity between resume and job description."""
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    feature_names = vectorizer.get_feature_names_out()
    scores = (tfidf[1] - tfidf[0]).toarray()[0]
    
    # Get top 20 keywords and their scores
    top_keywords = sorted(
        dict(zip(feature_names, scores)).items(),
        key=lambda x: abs(x[1]),
        reverse=True
    )[:20]
    
    return {
        "keywords": [k for k, s in top_keywords],
        "scores": [s for k, s in top_keywords]
    }

def extract_skills(text):
    """Extract skills from text using regex patterns."""
    # Common skill patterns
    skill_patterns = [
        r'\b(?:aws|azure|gcp|kubernetes|docker|k8s|terraform|ansible|jenkins)\b',
        r'\b(?:python|java|javascript|go|golang|node\.js|typescript)\b',
        r'\b(?:sql|postgresql|mysql|mongodb|redis)\b',
        r'\b(?:react|vue|angular|node\.js|express|flask)\b',
        r'\b(?:aws|azure|gcp|terraform|ansible|jenkins|kubernetes|docker)\b',
        r'\b(?:git|github|gitlab|bitbucket)\b',
        r'\b(?:ci/cd|cicd|continuous integration|continuous deployment)\b'
    ]
    
    skills = set()
    for pattern in skill_patterns:
        matches = re.findall(pattern, text.lower())
        skills.update(matches)
    
    return list(skills)

def analyze_skill_gap(resume_text, jd_text):
    """Analyze skill gaps between resume and job description."""
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    
    missing_skills = set(jd_skills) - set(resume_skills)
    strong_matches = set(jd_skills) & set(resume_skills)
    
    return {
        "missing_skills": list(missing_skills),
        "matched_skills": list(strong_matches),
        "match_percentage": len(strong_matches) / len(jd_skills) * 100 if jd_skills else 0
    }

def check_formatting_issues(text):
    """Check for ATS formatting issues."""
    issues = []
    
    # Check for common ATS issues
    if '\t' in text:
        issues.append("Avoid using tabs - use spaces instead")
    if '  ' in text:
        issues.append("Multiple spaces detected - use single spaces")
    if any(char in text for char in ['#', '~', '|']):
        issues.append("Avoid special characters that might confuse ATS")
    if '\n\n\n' in text:
        issues.append("Too many blank lines between sections")
    
    return issues

def generate_recommendations(skill_gap_analysis, formatting_issues):
    """Generate recommendations based on analysis."""
    recommendations = []
    
    # Add skill recommendations
    if skill_gap_analysis['missing_skills']:
        recommendations.append(f"Add sections highlighting experience with: 
        {', '.join(skill_gap_analysis['missing_skills'][:3])}")
    
    # Add formatting recommendations
    if formatting_issues:
        recommendations.extend([
            f"Fix formatting: {issue}" for issue in formatting_issues
        ])
    
    return recommendations
