import React, { useState } from 'react';
import { Card } from './ui/card';
import { Progress } from './ui/progress';
import { Check, X, ChevronDown, ChevronUp, Sparkles, AlertTriangle, Lightbulb } from 'lucide-react';

interface AnalysisResultsProps {
  score: number;
  missingKeywords: string[];
  strengths: string[];
  weaknesses: string[];
  feedback: string;
}

export function AnalysisResults({
  score,
  missingKeywords,
  strengths,
  weaknesses,
  feedback,
}: AnalysisResultsProps) {
  const [showFeedback, setShowFeedback] = useState(false);

  return (
    <div className="space-y-8">
      {/* ATS Score */}
      <div className="bg-gradient-to-br from-gray-900 to-gray-800 rounded-2xl p-6 shadow-lg border border-gray-700">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-bold text-white">ATS Score</h2>
          <div className="flex items-center space-x-2 bg-orange-500/20 px-3 py-1 rounded-full">
            <Sparkles className="w-4 h-4 text-orange-400" />
            <span className="text-orange-400 text-sm font-medium">
              {score >= 80 ? 'Strong' : score >= 60 ? 'Moderate' : 'Needs Work'}
            </span>
          </div>
        </div>
        
        <div className="flex items-center space-x-6">
          <div className="relative w-32 h-32">
            <div className="relative w-full h-full">
              <Progress 
                value={score} 
                className="h-full w-full rounded-full transform -rotate-90 bg-gray-700"
              />
              <div 
                className="absolute top-0 left-0 h-full rounded-full bg-gradient-to-b from-orange-500 to-amber-500 transition-all duration-500 ease-in-out"
                style={{ width: `${score}%`, transform: 'rotate(90deg) translateY(-100%)', transformOrigin: 'top left' }}
              />
            </div>
            <div className="absolute inset-0 flex items-center justify-center">
              <span className="text-3xl font-bold bg-gradient-to-r from-orange-400 to-amber-400 bg-clip-text text-transparent">
                {score}%
              </span>
            </div>
          </div>
          
          <div>
            <p className="text-gray-300">
              {score >= 80
                ? "Excellent! Your resume is well-optimized for ATS."
                : score >= 60
                ? "Good, but could use some improvements."
                : "Needs significant improvements to pass ATS screening."}
            </p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Missing Keywords */}
        <div className="bg-gray-800/80 p-6 rounded-xl border border-gray-700/50 backdrop-blur-sm">
          <h3 className="text-lg font-semibold text-white mb-4 flex items-center">
            <AlertTriangle className="w-5 h-5 text-red-400 mr-2" />
            Missing Keywords
          </h3>
          {missingKeywords.length > 0 ? (
            <ul className="space-y-3">
              {missingKeywords.map((keyword, index) => (
                <li key={index} className="flex items-center text-red-300 bg-red-900/30 px-4 py-2 rounded-lg border border-red-900/50">
                  <X className="w-4 h-4 mr-2 text-red-400" />
                  {keyword}
                </li>
              ))}
            </ul>
          ) : (
            <div className="flex items-center space-x-2 text-green-400 bg-green-900/20 px-4 py-3 rounded-lg border border-green-900/30">
              <Check className="w-5 h-5" />
              <span>No missing keywords found!</span>
            </div>
          )}
        </div>

        {/* Strengths */}
        <div className="bg-gray-800/80 p-6 rounded-xl border border-gray-700/50 backdrop-blur-sm">
          <h3 className="text-lg font-semibold text-white mb-4">
            <Lightbulb className="w-5 h-5 text-green-400 inline-block mr-2" />
            Strengths
          </h3>
          <ul className="space-y-3">
            {strengths.map((strength, index) => (
              <li key={index} className="flex items-start text-gray-200">
                <div className="bg-green-500/20 p-1 rounded-full mr-3 mt-0.5">
                  <Check className="w-3 h-3 text-green-400" />
                </div>
                {strength}
              </li>
            ))}
          </ul>
        </div>

        {/* Weaknesses */}
        <div className="md:col-span-2 bg-gray-800/80 p-6 rounded-xl border border-gray-700/50 backdrop-blur-sm">
          <h3 className="text-lg font-semibold text-white mb-4">
            <AlertTriangle className="w-5 h-5 text-amber-400 inline-block mr-2" />
            Areas for Improvement
          </h3>
          <ul className="space-y-3">
            {weaknesses.map((weakness, index) => (
              <li key={index} className="flex items-start text-gray-300">
                <div className="bg-amber-500/20 p-1 rounded-full mr-3 mt-0.5">
                  <X className="w-3 h-3 text-amber-400" />
                </div>
                {weakness}
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Feedback */}
      <div className="bg-gray-800/80 rounded-xl border border-gray-700/50 overflow-hidden">
        <button
          onClick={() => setShowFeedback(!showFeedback)}
          className="w-full px-6 py-4 flex items-center justify-between text-left hover:bg-gray-700/50 transition-colors"
        >
          <h3 className="text-lg font-semibold text-white">
            <Lightbulb className="w-5 h-5 text-orange-400 inline-block mr-2" />
            Detailed Feedback & Suggestions
          </h3>
          {showFeedback ? (
            <ChevronUp className="w-5 h-5 text-gray-400" />
          ) : (
            <ChevronDown className="w-5 h-5 text-gray-400" />
          )}
        </button>
        
        {showFeedback && (
          <div className="p-6 pt-0">
            <div className="prose prose-invert max-w-none text-gray-300">
              <p>{feedback}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
