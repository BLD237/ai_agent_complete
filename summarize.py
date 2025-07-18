import requests
# Removed incorrect import and usage of google.generativeai, as the code uses direct HTTP requests instead.
API_KEY = "AIzaSyB3QONMG4PYLDyx2uszOIAjTJnl-CjR7rM"


def summarize_with_gemini(text, api_key):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": api_key
    }
    prompt = (
        "Summarize the following article in a clear, structured, and concise manner. "
        "Your summary should include:\n"
        "1. A brief headline or title for the article.\n"
        "2. The main topic or subject in one sentence.\n"
        "3. 2-4 key points or findings, each as a bullet point.\n"
        "4. A one-sentence conclusion or takeaway.\n\n"
        "Format your response using Markdown with bold for the headline and bullet points for the key points.\n\n"
        " include any 'insights' section or label in your summary.\n\n"
        "Article content:\n"
        f"{text}"
    )
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, params=params, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            return result['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "Error: Unexpected response format."
    else:
        return f"Error: {response.status_code} - {response.text}"

# Directly assign your Gemini API key here

res = summarize_with_gemini("the crypto market is about to rise", API_KEY)
print(res)