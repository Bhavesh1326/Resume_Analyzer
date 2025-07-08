# AutoResume - Intelligent Resume Analyzer and Generator

AutoResume is an AI-powered application designed to analyze and generate resumes using advanced Natural Language Processing (NLP) techniques. This project leverages PostgreSQL for data storage and provides a user-friendly interface for both resume analysis and generation.

## Features

- **Resume Analysis**: Evaluate resumes for clarity, tone, grammar, keyword effectiveness, and formatting.
- **Resume Generation**: Create tailored resumes based on job titles and descriptions using AI/NLP techniques.
- **Database Integration**: Store and manage user data, resumes, analyses, and job descriptions using PostgreSQL.
- **Utility Functions**: Includes functions for PDF parsing, text extraction, and keyword matching.

## Project Structure

```
AutoResume
├── src
│   ├── main.py               # Entry point for the application
│   ├── analyzer
│   │   └── __init__.py       # Contains ResumeAnalyzer class
│   ├── generator
│   │   └── __init__.py       # Contains ResumeGenerator class
│   ├── db
│   │   └── models.py         # Defines database schema using SQLAlchemy
│   └── utils
│       └── __init__.py       # Utility functions for various tasks
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AutoResume.git
   cd AutoResume
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL and configure the database connection in `src/db/models.py`.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the prompts to analyze or generate resumes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.