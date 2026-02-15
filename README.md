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

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Mac/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt


4. **Run the backend server**
   ```bash
   python main.py

   ```
   The API will start at `http://localhost:8888`

5. **Open the frontend**
   - Open `index.html` in your browser
   - Or use Live Server in VS Code

## 🎯 How It Works

1. **Upload your resume** or paste your skills
2. **Select your dream role** from 6 career paths
3. **Set your weekly hours** (5-40 hours)
4. **Get instant analysis**:
   - Skills detected from your resume
   - Gap analysis (required vs preferred)
   - 30-day personalized roadmap
5. **Track progress** by checking off daily tasks
6. **Export your plan** for offline use

## 🧠 Supported Career Roles

- 🤖 AI/ML Engineer
- 💻 Full Stack Architect
- 📊 Data Scientist
- 🚀 DevOps Engineer
- 🔒 Security Analyst
- 📱 Product Lead

## 📁 Project Structure

```
personal-career-navigator/
├── main.py              # FastAPI backend
├── index.html           # Frontend UI
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact

BASIL BABY - basilbaby3007@gmail.com

Project Link: [https://github.com/basilbaby3007-cpu/personal-career-navigator](https://github.com/basilbaby3007-cpu/personal-career-navigator)

## 🙏 Acknowledgments

- FastAPI documentation
- Font Awesome for icons
- Google Fonts for Space Grotesk
