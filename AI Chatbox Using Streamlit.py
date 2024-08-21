pip install streamlit openai
streamlit run chatbot.py

import streamlit as st
import openai

# Replace with your OpenAI API key
openai.api_key = "your-openai-api-key"

# Function to get response from the AI model
def get_bot_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can change this to the engine you prefer
        prompt=user_input,
        max_tokens=150,
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("AI Chatbot")

    # Create a sidebar for user input
    st.sidebar.header("User Input")
    user_input = st.sidebar.text_input("You: ", "")

    # When user enters a message
    if st.sidebar.button("Send"):
        if user_input:
            response = get_bot_response(user_input)
            st.text_area("Chatbot Response", value=response, height=200)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
