from google import genai

# Initialize client (use your actual API key)
client = genai.Client(api_key="AIzaSyDUopVpP-AxBgtkgu2iy9HegxB02TBg9PU")

print("💬 finance Chatbot (type 'exit' to quit)\n")

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
