# Personal Career Navigator 🧭

An AI-powered career development platform that analyzes your skills, identifies gaps, and creates personalized 30-day learning roadmaps for your dream tech role.

## ✨ Features

- **🤖 AI Skill Analysis**: Upload your resume and get instant skill detection
- **📊 Gap Identification**: See what's missing for your target role (ML Engineer, Full Stack, Data Scientist, etc.)
- **🗺️ 30-Day Roadmap**: Personalized daily tasks with learning resources
- **📄 Resume Parsing**: Support for PDF, DOCX, and TXT files
- **📈 Progress Tracking**: Check off tasks and watch your progress
- **🔄 Adaptive Learning**: AI adjusts your plan based on completion rate
- **📱 Modern UI**: Glassmorphism design with animated particles

## 🛠️ Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **PyPDF2/pdfplumber** - PDF text extraction
- **python-docx** - Word document parsing
- **Pydantic** - Data validation

### Frontend
- **HTML5/CSS3** - Modern responsive design
- **JavaScript (ES6)** - Dynamic interactions
- **Font Awesome** - Icons
- **Google Fonts** - Space Grotesk typography

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/basilbaby3007-cpu/personal-career-navigator.git
   cd personal-career-navigator
   python -m venv .venv
.venv\Scripts\activate
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd backend
python app.py
