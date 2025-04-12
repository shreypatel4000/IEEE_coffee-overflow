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
                {"role": "user", "content": user_input}
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
