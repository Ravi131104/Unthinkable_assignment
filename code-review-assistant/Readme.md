🚀 Code Review Assistant

An automated code analysis tool that uses **Google Gemini 2.0 Flash** to provide instant feedback on code structure, readability, and potential bugs. This project features a high-performance **FastAPI** backend and a modern **Dark Mode** dashboard.

---

 🎥 Demo Video
(https://drive.google.com/file/d/1YeHX1OeCC1N0UIwBQaCOt15ykHHvK7LV/view?usp=sharing)

*(Please watch the video to see the live AI analysis and UI features)*

---

✨ Features
📂 File Upload:** Supports uploading raw source code files via a secure REST API.
 AI-Powered Analysis:** Integrated with **Gemini 2.0 Flash** to generate deep insights on modularity and best practices.
📊 Smart Reporting:** Returns a structured **Markdown report** containing readability checks, bug detection, and refactoring suggestions.
🎨 Modern UI:** A responsive **Dark Mode** dashboard with real-time loading states and Markdown rendering.

---

🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **AI Model:** Google Gemini 2.0 Flash (`google-generativeai`)
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript, Marked.js
* **Environment Management:** Python-dotenv

---

⚙️ Installation & Setup

1. Clone the Repository
```bash
git clone [https://github.com/Ravi131104/Unthinkable_assignment](https://github.com/Ravi131104/Unthinkable_assignment)
cd code-review-assistant

2. Create a Virtual Environment
Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Configure API Key
Create a file named .env in the root directory and add your Google Gemini API key:

Code snippet

GEMINI_API_KEY=your_actual_api_key_here

🚀 How to Run
Start the Backend Server:

Bash

uvicorn main:app --reload
The API will run at http://127.0.0.1:8000.

Launch the Dashboard:

Open the index.html file in your browser (or use "Live Server" in VS Code).

Usage:

Click "Select Source Code File".

Choose a Python, JS, or C++ file.

Click "Analyze Code".

Wait for the AI to generate the improvement report.

📂 Project Structure
code-review-assistant/
│
├── main.py              # FastAPI Backend & LLM Logic
├── index.html           # Frontend Dashboard
├── requirements.txt     # Python Dependencies
├── .env                 # API Key (Not uploaded to GitHub)
├── .gitignore           # Git ignore rules
└── README.md            # Project Documentation

🛡️ Disclaimer
This tool uses an LLM to analyze code. While it is highly effective at finding structural issues, always verify critical bug reports manually.
