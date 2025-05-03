import openai

def detect_scam(text, lang="en"):
    prompt = f"Analyze this message and classify as Safe, Suspicious, or Scam with reason: {text}"
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {
        "classification": "Scam",
        "reason": response["choices"][0]["message"]["content"]
    }
