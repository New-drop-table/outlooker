from openai import OpenAI
import os


client = OpenAI(api_key="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")  # 🔑 Вставь сюда свой ключ

def summarize_email(email_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant, who creates a short form of email"},
            {"role": "user", "content": f"Summarize the following email in 1-2 sentences, write from first pov:\n\n{email_text}"}
        ],
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].message.content.strip()


# print(summarize_email("""
# from: Jelena Vasic
# to: Valerii Kaspruk
#
# Dear students,
#
# I have noticed that many of you did not push your work to GitHub yesterday before leaving the lab (see the first picture below for the requirement listed in the instructions). If I am not able to see the differences between what you did in the lab and what is in the final submission, your grade will be affected. You can somewhat reduce the impact of this omission by making  your first submission as soon as possible.
#
# Those of you who have not been able to solve the problem of unresolved references in VS Code can download a flat collection of given files, now modified to remove all packages (see link circled in red in the second picture below).
#
# Suppliers and Customers have an add() method (see blue-circled text in second picture below), which was not shown yesterday. If you have completed your solution without this, that is fine, but if you want to use it, that is also ok.
#
# Regards,
# Jelena"""))