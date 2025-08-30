from flask import Flask, render_template, request, jsonify
import time

# --- 1. SETUP ---
# Initialize the Flask app
# The 'template_folder' and 'static_folder' arguments tell Flask where to find your files.
app = Flask(__name__, template_folder='templates', static_folder='static')

# --- 2. YOUR ORIGINAL AI LOGIC (COPIED FROM YOUR STREAMLIT SCRIPT) ---
# No changes are needed in these functions.
def get_ibm_model_response(user_input, demographic, chat_history):
    """
    (Placeholder) Simulates a call to an IBM generative AI model like Granite.
    """
    if demographic == 'Student':
        if "investing" in user_input.lower():
            return "That's a great question! Think of investing like planting a tree. You start with a small seed (your initial investment), and over time, it can grow into something big! A good first step for students is to look into 'micro-investing' apps. They let you start with just a few dollars, like your spare change from buying coffee. It's a fantastic way to learn without needing a lot of money upfront!"
        elif "budget" in user_input.lower():
            return "Budgeting is super important, even with a student income! Let's make it simple. Try the 50/30/20 rule: 50% of your income for needs (like rent and groceries), 30% for wants (like going out with friends), and 20% for savings. We can create a sample budget based on your part-time job or allowance if you'd like!"
        else:
            return "I'm here to help you with your financial questions! As a student, understanding money is a real superpower. What's on your mind?"

    elif demographic == 'Professional':
        if "investing" in user_input.lower():
            return "Certainly. For a professional, a diversified investment strategy is key. Based on your risk tolerance, we could explore a portfolio mix of ETFs (like those tracking the S&P 500), blue-chip stocks, and potentially some allocation to bonds for stability. Have you considered maximizing your tax-advantaged retirement accounts, such as a 401(k) or IRA, as a primary vehicle for long-term growth?"
        elif "tax" in user_input.lower():
            return "Navigating tax obligations is a critical component of financial planning. To provide accurate guidance, I would need to know more about your income sources, filing status, and any deductions or credits you might be eligible for. Key areas to consider for tax optimization include maximizing retirement contributions, leveraging tax-loss harvesting, and ensuring all eligible business expenses are deducted if you're self-employed."
        else:
            return "Welcome. I am ready to assist with your financial inquiries. How can I help you optimize your financial strategy today? We can discuss portfolio management, tax efficiency, or long-term savings goals."
    return "I am a personal finance chatbot. Please select a profile to get started."


# --- 3. FLASK ROUTES (THE "API") ---

# This route serves your main landing page (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# This route will serve the new chat page
@app.route('/chat')
def chat_page():
    return render_template('chat.html')

# This is the API endpoint for the chatbot logic.
# The frontend will send requests here.
@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data.get('message')
    demographic = data.get('demographic', 'Professional') # Default to Professional if not provided
    chat_history = data.get('history', [])

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Get the AI response from your function
    ai_response = get_ibm_model_response(user_message, demographic, chat_history)

    # Return the response to the frontend as JSON
    return jsonify({'response': ai_response})

# --- 4. RUN THE APP ---
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you save changes
    app.run(debug=True)
