import requests

API_URL = "http://127.0.0.1:8000/chat"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = requests.post(API_URL, json={"message": user_input})

    # Debug print
    # print("Status code:", response.status_code)
    # print("Raw text response:", response.text)

    try:
        print("\n")
        print("Zeno:", response.json().get("reply"))
    except Exception as e:
        print("⚠️ Error decoding JSON:", e)
