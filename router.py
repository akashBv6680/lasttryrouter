import streamlit as st
import requests

# Configure OpenRouter API key
openrouter_api_key = "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"

def get_openrouter_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "HTTP-Referer": site_url,
        "X-Title": site_name,
        "Content-Type": "application/json",
    }
    data = {
        "model": "openai/gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": user_input,
            },
        ],
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# Streamlit app layout
st.title("Advanced Chatbot")
user_input = st.text_input("What would you like to ask?")
if user_input:
    try:
        chatbot_response = get_openrouter_response(user_input)
        st.write(f"Chatbot: {chatbot_response}")
    except Exception as e:
        st.write(f"Error: {e}")
