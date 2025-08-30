<<<<<<< HEAD
from google import genai

# Initialize client (use your actual API key)
client = genai.Client(api_key="AIzaSyDUopVpP-AxBgtkgu2iy9HegxB02TBg9PU")

print("💬 Gemini Chatbot (type 'exit' to quit)\n")

while True:
    # Take user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Goodbye!")
        break

    # Send request to Gemini model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    # Print AI response
    print("AI:", response.text, "\n")
=======
from flask import Flask, request, jsonify, render_template
from google import genai

app = Flask(__name__)

# Configure Google Generative AI
client = genai.Client(api_key='AIzaSyDUopVpP-AxBgtkgu2iy9HegxB02TBg9PU')

@app.route("/")
def home():
    return render_template("home.html")   # homepage

@app.route("/chat.html")
def chat_page():
    return render_template("chat.html")   # chatbot UI

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_msg = request.json.get("message")
        if not user_msg:
            return jsonify({"reply": "⚠ Please enter a message."})

        # Send message to Gemini model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg
        )

        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"⚠ Error: {str(e)}"})

if __name__ == "__main__":   # fixed the typo from _main_
    app.run(debug=True)

>>>>>>> 7fe893bb4a619cedb5fafba19cb9883af3836dcd
