import requests

# GROQ API Key and Model
API_KEY = "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"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()['choices'][0]['message']['content']
        print("🧠 Groq Response:\n", reply)
    except Exception as e:
        print("[❌ Error]:", e)

# Example use
ask_groq("Explain the importance of fast language models")
