from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()  # Load from .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # ✅ Correct name

app = Flask(__name__)

# Replace with your Gemini API key from https://makersuite.google.com/app/apikey
genai.configure(api_key=os.getenv("GENAI_API_KEY"))
model_name = "models/gemini-1.5-flash-latest"
model = genai.GenerativeModel(model_name)
chat_session = model.start_chat(history=[])
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json['msg']
    print("User:", user_msg)

    try:
        response = chat_session.send_message(user_msg)
        print("Raw Response:", response)

        reply = ""
        for part in response.parts:
            reply += part.text

        return jsonify({"reply": reply})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Sorry, something went wrong. 🛠️"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
