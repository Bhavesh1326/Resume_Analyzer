import React from 'react';

interface NLPAnalysisProps {
  analysis: {
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
}

const NLPAnalysis: React.FC<NLPAnalysisProps> = ({ analysis }) => {
  return (
    <div className="space-y-6">
      {/* Keyword Analysis */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold mb-4">Keyword Analysis</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-medium mb-2">Resume Keywords</h4>
            <ul className="list-disc pl-5 space-y-1">
              {analysis.keywords.resume.map((keyword, i) => (
                <li key={i}>{keyword}</li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="font-medium mb-2">Job Description Keywords</h4>
            <ul className="list-disc pl-5 space-y-1">
              {analysis.keywords.jobDescription.map((keyword, i) => (
                <li key={i}>{keyword}</li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {/* Skill Gap Analysis */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold mb-4">Skill Gap Analysis</h3>
        <div className="space-y-4">
          <div>
            <h4 className="font-medium mb-2">Matched Skills</h4>
            <ul className="list-disc pl-5 space-y-1">
              {analysis.skillAnalysis.matchedSkills.map((skill, i) => (
                <li key={i} className="text-green-600">{skill}</li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="font-medium mb-2">Missing Skills</h4>
            <ul className="list-disc pl-5 space-y-1">
              {analysis.skillAnalysis.missingSkills.map((skill, i) => (
                <li key={i} className="text-red-600">{skill}</li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="font-medium mb-2">Skill Match Percentage</h4>
            <div className="w-full bg-gray-200 rounded-full h-2.5">
              <div 
                className="bg-blue-600 h-2.5 rounded-full"
                style={{ width: `${analysis.skillAnalysis.matchPercentage}%` }}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Formatting Issues */}
      {analysis.formattingIssues.length > 0 && (
        <div className="bg-red-50 rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4">ATS Formatting Issues</h3>
          <ul className="list-disc pl-5 space-y-1">
            {analysis.formattingIssues.map((issue, i) => (
              <li key={i} className="text-red-600">{issue}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Recommendations */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold mb-4">Improvement Recommendations</h3>
        <ul className="list-disc pl-5 space-y-2">
          {analysis.recommendations.map((recommendation, i) => (
            <li key={i} className="text-blue-600">{recommendation}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default NLPAnalysis;
