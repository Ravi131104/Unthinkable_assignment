import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

@app.post("/review")
async def review_code(file: UploadFile = File(...)):
    try:
        # 1. Read the file content [cite: 6]
        content = await file.read()
        code_str = content.decode("utf-8")

        # 2. Initialize the specific model found in your debug list
        # We are using the 2.0 Flash model which appeared in your logs
        model = genai.GenerativeModel("models/gemini-2.0-flash")

        # 3. Create the Prompt [cite: 14]
        prompt = (
            "You are a code review assistant. Review this code for readability, "
            "modularity, and potential bugs, then provide improvement suggestions.\n\n"
            f"Code:\n{code_str}"
        )

        # 4. Generate the Analysis 
        response = model.generate_content(prompt)
        
        # 5. Return the Report [cite: 7]
        if response.text:
            return {"filename": file.filename, "review": response.text}
        else:
            return {"filename": file.filename, "review": "The AI analyzed the code but returned no text."}

    except Exception as e:
        print(f"CRITICAL ERROR: {e}") # This prints to your terminal
        raise HTTPException(status_code=500, detail=str(e))