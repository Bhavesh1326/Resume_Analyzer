import { Textarea } from './ui/textarea';

interface JobDescriptionProps {
  value: string;
  onChange: (value: string) => void;
}

export function JobDescription({ value, onChange }: JobDescriptionProps) {
  return (
    <div className="w-full space-y-2">
      <label htmlFor="job-description" className="block text-sm font-medium text-gray-300">
        Job Description
      </label>
      <Textarea
        id="job-description"
        placeholder="Paste the job description here..."
        className="min-h-[200px] w-full bg-gray-800 border-gray-700 text-gray-200 focus:border-orange-500 focus:ring-orange-500"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}
