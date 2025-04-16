from openai import OpenAI
import os


client = OpenAI(api_key="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")  # 🔑 Вставь сюда свой ключ

def summarize_email(email_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes emails."},
            {"role": "user", "content": f"Summarize the following email in 1-2 sentences:\n\n{email_text}"}
        ],
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].message.content.strip()