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