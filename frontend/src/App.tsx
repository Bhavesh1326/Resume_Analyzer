import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Loader2, Check, Upload } from 'lucide-react';
import NLPAnalysis from './components/NLPAnalysis';

interface AnalysisResults {
  success: boolean;
  analysis: {
    match_score: number;
    missing_skills: string[];
    key_skills_matched: string[];
    strengths: string[];
    improvement_areas: string[];
    suggestions: string[];
    summary: string;
    nlp_analysis: {
      keywords: {
        resume: string[];
        jobDescription: string[];
      };
      keywordMatch: {
        keywords: string[];
        scores: number[];
      };
      skillAnalysis: {
        missingSkills: string[];
        matchedSkills: string[];
        matchPercentage: number;
      };
      formattingIssues: string[];
      recommendations: string[];
    };
  };
}

function App() {
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisResults, setAnalysisResults] = useState<AnalysisResults | null>(null);

  const handleFileSelect = (file: File | null) => {
    setResumeFile(file);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!resumeFile || !jobDescription) return;

    console.log('Starting resume analysis...');
    console.log('Resume file:', resumeFile.name);
    console.log('Job description length:', jobDescription.length, 'characters');

    setIsAnalyzing(true);

    try {
      const formData = new FormData();
      formData.append('resume', resumeFile);
      formData.append('job_description', jobDescription);

      const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
      console.log('Sending request to:', `${apiUrl}/api/analyze`);

      const response = await fetch(`${apiUrl}/api/analyze`, {
        method: 'POST',
        body: formData,
      });

      console.log('Response status:', response.status, response.statusText);

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText);
        throw new Error(`HTTP error! status: ${response.status}, body: ${errorText}`);
      }

      const results = await response.json();
      console.log('API Response:', JSON.stringify(results, null, 2));

      if (!results.success) {
        console.error('API returned error:', results.error);
        throw new Error(results.error || 'Failed to analyze resume');
      }

      setAnalysisResults(results);
      console.log('Analysis completed successfully');
    } catch (error) {
      console.error('Error analyzing resume:', error);
      alert(`Failed to analyze resume: ${error instanceof Error ? error.message : 'Unknown error'}`);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold text-gray-900">Resume Analyzer</h1>
        </div>
      </header>
      <main className="flex-1">
        <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label htmlFor="resume" className="block text-sm font-medium text-gray-700">
                  Upload Resume (PDF only)
                </label>
                <div className="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-lg">
                  <div className="space-y-1 text-center">
                    <Upload className="mx-auto h-12 w-12 text-gray-400" />
                    <div className="flex text-sm text-gray-600">
                      <label htmlFor="resume" className="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500">
                        <span>Upload a file</span>
                        <input id="resume" name="resume" type="file" accept=".pdf" onChange={(e) => handleFileSelect(e.target.files?.[0] || null)} className="sr-only" />
                      </label>
                      <p className="pl-1">or drag and drop</p>
                    </div>
                    <p className="text-xs text-gray-500">
                      PDF up to 10MB
                    </p>
                  </div>
                </div>
              </div>
              <div>
                <label htmlFor="jobDescription" className="block text-sm font-medium text-gray-700">
                  Job Description
                </label>
                <div className="mt-1">
                  <textarea
                    id="jobDescription"
                    name="jobDescription"
                    rows={4}
                    className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                    placeholder="Paste the job description here..."
                    value={jobDescription}
                    onChange={(e) => setJobDescription(e.target.value)}
                  />
                </div>
              </div>
              <div>
                <button
                  type="submit"
                  disabled={isAnalyzing || !resumeFile || !jobDescription}
                  className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isAnalyzing ? (
                    <>
                      <Loader2 className="animate-spin mr-2 h-4 w-4" />
                      Analyzing...
                    </>
                  ) : (
                    'Analyze Resume'
                  )}
                </button>
              </div>
            </form>

            {analysisResults && (
              <div className="mt-8">
                <div className="bg-white p-6 rounded-lg shadow">
                  <h2 className="text-xl font-semibold mb-4">Analysis Results</h2>
                  <div className="space-y-6">
                    <div>
                      <h3 className="font-medium mb-2">ATS Score</h3>
                      <div className="flex items-center">
                        <div className="w-32 h-32 rounded-full bg-indigo-100 flex items-center justify-center">
                          <span className="text-3xl font-bold text-indigo-600">
                            {analysisResults.analysis.match_score}%
                          </span>
                        </div>
                        <div className="ml-4">
                          <p className="text-sm text-gray-600">
                            Based on your resume's match with the job description
                          </p>
                        </div>
                      </div>
                    </div>
                    <div>
                      <h3 className="font-medium mb-2">Missing Keywords</h3>
                      <ul className="list-disc pl-5 space-y-1">
                        {analysisResults.analysis.missing_skills.map((keyword, i) => (
                          <li key={i} className="text-red-600">
                            {keyword}
                          </li>
                        ))}
                      </ul>
                    </div>
                    <div>
                      <h3 className="font-medium mb-2">Strengths</h3>
                      <ul className="list-disc pl-5 space-y-1">
                        {analysisResults.analysis.strengths.map((strength, i) => (
                          <li key={i} className="text-green-600">
                            {strength}
                          </li>
                        ))}
                      </ul>
                    </div>
                    <div>
                      <h3 className="font-medium mb-2">Areas for Improvement</h3>
                      <ul className="list-disc pl-5 space-y-1">
                        {analysisResults.analysis.improvement_areas.map((weakness, i) => (
                          <li key={i} className="text-yellow-600">
                            {weakness}
                          </li>
                        ))}
                      </ul>
                    </div>
                    <div>
                      <h3 className="font-medium mb-2">Feedback</h3>
                      <p className="text-gray-600">
                        {analysisResults.analysis.summary}
                      </p>
                    </div>
                    <div>
                      <h3 className="font-medium mb-2">Suggestions</h3>
                      <ul className="list-disc pl-5 space-y-1">
                        {analysisResults.analysis.suggestions.map((suggestion, i) => (
                          <li key={i} className="text-blue-600">
                            {suggestion}
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </div>
                <NLPAnalysis analysis={analysisResults.analysis.nlp_analysis} />
              </div>
            )}
          </div>
        </div>
      </main>
      <footer className="bg-gray-900 border-t border-gray-800 mt-12">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <p className="text-center text-gray-500 text-sm">
            @Bhavesh
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
