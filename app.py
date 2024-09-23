
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
import os
gemini_api_key="AIzaSyB2ILnUXepfWGQ62jFcSx6MlwCmbqW59kI"

genai.configure(api_key=gemini_api_key)


model = genai.GenerativeModel(
    model_name="gemini-pro",  # Replace with the desired Gemini model
)

# Define a function to handle user queries
def handle_query(query):
    try:
        response_data = llm.invoke(query)
        if isinstance(response_data, dict):
            response = response_data["content"]
        else:
            response = response_data
        return response
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred. Please try again later."

# Implement basic conversation flow
def chatbot_flow():
    print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end the conversation)")
    while True:
        user_query = input("User: ")
        if user_query.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = model.generate_content(user_query)
        print("Chatbot:", response.text)

# Run the chatbot
chatbot_flow()
