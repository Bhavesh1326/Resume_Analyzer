# AutoResume - Intelligent Resume Analyzer

AutoResume is a modern web application that uses advanced NLP and AI techniques to analyze resumes against job descriptions. It provides detailed feedback on ATS compatibility, keyword matching, skill gaps, and formatting issues.

## Environment Setup

### Prerequisites
- Python 3.10 or higher
- Node.js 18 or higher
- Docker (optional, for containerized deployment)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Resume_Analyzer.git
cd Resume_Analyzer
```

### 2. Environment Variables Setup

#### For Local Development
1. Create a `.env` file in the project root:
   ```bash
   # On Windows
   copy .env.example .env
   
   # On Linux/Mac
   cp .env.example .env
   ```

2. Edit the `.env` file and update the following required configurations:
   ```
   # Required: Get your API key from Google AI Studio
   GEMINI_API_KEY=your_gemini_api_key_here
   
   # Backend Configuration
   PORT=8000
   DEBUG=True
   
   # Frontend Configuration
   VITE_API_BASE_URL=http://localhost:8000
   ```

#### Important Security Notes
- 🔒 **Never commit your `.env` file** - It's already added to `.gitignore`
- 🔑 Keep your API keys secure and never share them publicly
- 📝 Use `.env.example` as a reference for required environment variables
- 🌐 For production, use environment-specific configuration management

### 3. Install Dependencies

#### Option A: Using Docker (Recommended)
```bash
# Build and start all services
docker-compose up --build

# To run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f
```

#### Option B: Manual Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
cd frontend
npm install
cd ..
```

### 4. Running the Application

#### Development Mode
```bash
# Start backend server (in project root)
uvicorn backend.main:app --reload

# In a new terminal, start frontend
cd frontend
npm run dev
```

#### Production Mode
```bash
# Build frontend for production
cd frontend
npm run build

# Start production server (from project root)
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### 5. Verifying the Setup
1. Frontend should be available at: http://localhost:3000
2. Backend API should be available at: http://localhost:8000
3. API documentation (Swagger UI) at: http://localhost:8000/docs

## Configuration Reference

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GEMINI_API_KEY` | Google AI Studio API key | Yes | - |
| `PORT` | Backend server port | No | 8000 |
| `DEBUG` | Enable debug mode | No | True |
| `VITE_API_BASE_URL` | Frontend API base URL | No | http://localhost:8000 |

### Troubleshooting

#### Common Issues
1. **Missing Environment Variables**
   - Ensure all required variables are set in your `.env` file
   - Compare with `.env.example` for reference

2. **Port Conflicts**
   - Check if ports 3000 (frontend) and 8000 (backend) are available
   - Update ports in `.env` if needed

3. **Docker Issues**
   - Make sure Docker is running
   - Try rebuilding containers: `docker-compose build --no-cache`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Google Gemini API](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)

---

<div align="center">
  Made with ❤️ for better job applications
</div>

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