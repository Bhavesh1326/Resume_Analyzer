from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    resumes = relationship('Resume', back_populates='user')

class Resume(Base):
    __tablename__ = 'resumes'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    version = Column(Integer, default=1)
    user = relationship('User', back_populates='resumes')
    analyses = relationship('Analysis', back_populates='resume')

class Analysis(Base):
    __tablename__ = 'analyses'
    
    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'), nullable=False)
    job_description_id = Column(Integer, ForeignKey('job_descriptions.id'), nullable=True)
    score = Column(Float, nullable=False)
    feedback = Column(Text)
    analysis_type = Column(String(50), default="general")  # e.g., grammar, ATS, etc.
    keywords = Column(Text)  # comma-separated or JSON
    ats_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    resume = relationship('Resume', back_populates='analyses')
    job_description = relationship('JobDescription', back_populates='analyses')

class JobDescription(Base):
    __tablename__ = 'job_descriptions'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    analyses = relationship('Analysis', back_populates='job_description')