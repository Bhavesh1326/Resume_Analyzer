# AutoResume - Intelligent Resume Analyzer

AutoResume is a modern web application that uses advanced NLP and AI techniques to analyze resumes against job descriptions. It provides detailed feedback on ATS compatibility, keyword matching, skill gaps, and formatting issues.

## Features

### ATS Compatibility Analysis
- ATS score calculation
- Keyword matching against job description
- Formatting issue detection
- Skill gap analysis

### NLP-Based Analysis
- Advanced keyword extraction
- Skill identification and matching
- Content quality analysis
- Actionable improvement suggestions

### Modern UI
- Clean and intuitive interface
- Real-time feedback
- Detailed visualization of analysis results
- Responsive design
- Drag-and-drop file upload
- Interactive analysis display

## Tech Stack

### Backend
- FastAPI
- Google Gemini AI
- spaCy for NLP
- scikit-learn
- Python 3.10+

### Frontend
- React 18 + TypeScript
- Vite
- Tailwind CSS
- Framer Motion
- Lucide React Icons

## Project Structure

```
AutoResume
├── backend                   # Backend service
│   ├── main.py              # FastAPI application
│   ├── nlp_utils.py         # NLP utility functions
│   ├── analyze_resume.py    # Resume analysis logic
│   ├── config.py            # Configuration settings
│   ├── test_gemini.py       # Gemini API test script
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Backend environment variables
│
├── frontend                 # Frontend application
│   ├── src
│   │   ├── App.tsx         # Main application component
│   │   ├── components      # React components
│   │   └── index.css       # Global styles
│   ├── vite.config.ts      # Vite configuration
│   ├── package.json        # Frontend dependencies
│   └── .env                # Frontend environment variables
│
├── docker                   # Docker configuration
│   └── nginx.conf          # Nginx configuration
│
├── .dockerignore           # Docker ignore file
├── Dockerfile              # Docker multi-stage build
├── docker-compose.yml      # Docker Compose configuration
└── README.md              # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker (optional)
- PostgreSQL (for database)

### Environment Variables

Create a `.env` file in both frontend and backend directories:

#### Backend `.env`
```
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/autoresume
```

#### Frontend `.env`
```
VITE_API_URL=http://localhost:8000
```

### Running the Application

#### Using Docker

1. Build the Docker images:
   ```bash
   docker build -t autoresume .
   ```

2. Run the containers:
   ```bash
   docker run -d -p 80:80 -p 8000:8000 autoresume
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost:8000

#### Manual Setup

1. Backend Setup:
   ```bash
   # Install dependencies
   pip install -r backend/requirements.txt
   
   # Run backend server
   cd backend
   uvicorn main:app --reload
   ```

2. Frontend Setup:
   ```bash
   # Install dependencies
   cd frontend
   npm install
   
   # Run development server
   npm run dev
   ```

### Database Setup

1. Create PostgreSQL database:
   ```sql
   CREATE DATABASE autoresume;
   ```

2. Update backend/.env with correct database credentials

## Deployment

### Using Docker

#### Building the Docker Images

1. Build the Docker images:
   ```bash
   docker build -t autoresume .
   ```

2. Build with cache disabled (for fresh build):
   ```bash
   docker build --no-cache -t autoresume .
   ```

#### Running the Application

1. Run in detached mode:
   ```bash
   docker run -d -p 80:80 -p 8000:8000 autoresume
   ```

2. Run in interactive mode (for debugging):
   ```bash
   docker run -it -p 80:80 -p 8000:8000 autoresume
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost:8000

4. View container logs:
   ```bash
   docker logs <container_id>
   ```

5. Stop the container:
   ```bash
   docker stop <container_id>
   ```

#### Docker Compose (Alternative)

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Run in detached mode:
   ```bash
   docker-compose up -d
   ```

3. View logs:
   ```bash
   docker-compose logs
   ```

4. Stop services:
   ```bash
   docker-compose down
   ```

#### Environment Variables

Create a `.env` file in the root directory:
```bash
GEMINI_API_KEY=your_api_key_here
VITE_API_URL=http://localhost:8000
```

#### Docker Commands Reference

Common Docker commands:
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Remove a container
docker rm <container_id>

# Remove an image
docker rmi autoresume

# Remove unused images
docker image prune

# Remove unused containers
docker container prune
```

### Manual Installation

#### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env`:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables in `.env`:
   ```
   VITE_API_URL=http://localhost:8000
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

### Resume Analysis
`POST /api/analyze`
- Accepts: PDF file and job description text
- Returns: Detailed analysis including:
  - ATS score
  - Keyword matches
  - Skill gaps
  - Formatting issues
  - Recommendations

## NLP Analysis Flow

1. Text Extraction
   - Extract text from PDF using PyPDF2
   - Clean and preprocess text

2. Keyword Analysis
   - Extract keywords using spaCy
   - Calculate keyword importance using TF-IDF
   - Compare with job description keywords

3. Skill Gap Analysis
   - Extract skills using regex patterns
   - Match against job requirements
   - Calculate skill coverage

4. Formatting Checks
   - Check for ATS-friendly formatting
   - Validate section structure
   - Check for common formatting issues

## Usage

1. Upload your resume (PDF format)
2. Paste the job description
3. Click "Analyze Resume"
4. View detailed analysis including:
   - ATS Score
   - Missing Keywords
   - Strengths and Weaknesses
   - Formatting Issues
   - Skill Gap Analysis
   - Actionable Recommendations

## Important Notes

- Ensure your resume is in PDF format (max 10MB)
- The application requires a stable internet connection for AI analysis
- Keep your API keys secure and never commit them to version control
- The analysis results are based on NLP techniques and may not be 100% accurate

## Error Handling

- Input validation
- File format checking
- API rate limiting
- Error logging

## Security

- API key validation
- Input sanitization
- Rate limiting
- Error masking

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Update documentation
5. Submit pull request

## License

MIT License - see LICENSE file for details