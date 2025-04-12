from fastapi import FastAPI, Request
import requests
import json
import traceback

app = FastAPI()

API_KEY = "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"  # Replace this with your actual API key
SITE_URL = "<YOUR_SITE_URL>"  # Optional: your site's URL
SITE_TITLE = "<YOUR_SITE_NAME>"  # Optional: your site title

@app.post("/chat")
async def chat(req: Request):
    try:
        body = await req.json()
        user_input = body["message"]
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": SITE_URL,  # Optional
            "X-Title": SITE_TITLE,  # Optional
        }

        payload = {
            "model": "meta-llama/llama-4-maverick:free",
            "messages": [
                {"role" : "system", "content" : "Your name is Zeno, an AI chatbot that is used for career counselling to students. Your responses should be aligned to the core purpose of 2 things, (1) Helping students select their career based on their chats, and (2) Giving a roadmap for their selected career prospect. It is suggested that you ask questions in your responses to help you and your user decide their future prospects. The chat should end whenever you think the user has narrowed down its options to a single one, and end with giving a roadmap to achieve it from current knowledge to final knowledge. Also wishing them luck"},
                {"role": "user", "content": user_input},
            ],
        }

        # Send the request to OpenRouter (DeepSeek)
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout = 10)

        print("🔥 DeepSeek API status:", response.status_code)
        print("🔥 DeepSeek raw response:", response.text)

        try:
            result = response.json()
            print("✅ Parsed JSON:", result)
            print("✅ Parsed JSON:", result)
            print("✅ Parsed JSON:", result)

            if "choices" in result:
                return {"reply": result["choices"][0]["message"]["content"]}
            else:
                return {"reply": f"Unexpected response format: {result}"}

        except Exception as json_error:
            print("❌ Failed to parse JSON:")
            traceback.print_exc()
            return {"reply": f"llama returned a non-JSON response: {response.text}"}

    except Exception as e:
        print("🚨 Unexpected server error:")
        traceback.print_exc()
        return {"reply": "Zeno crashed while thinking. Please try again."}
