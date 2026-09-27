import os

from groq import Groq
from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


if not api_key:

    raise ValueError(
        "GROQ_API_KEY is missing."
    )


client = Groq(
    api_key=api_key
)


def ask_ai(user_message):

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[

            {
                "role": "system",

                "content": """
You are NOVA, a friendly personal voice assistant.

The user may speak English,
Urdu or Roman Urdu.

Respond naturally.

If the user speaks English,
answer in English.

If the user speaks Roman Urdu,
answer naturally in Roman Urdu.

Keep responses short because
your responses are spoken aloud.

Be friendly and helpful.

Do not say "As an AI"
unless the user asks about AI.
"""
            },

            {
                "role": "user",
                "content": user_message
            }

        ],

        temperature=0.4,

        max_tokens=200
    )


    return response.choices[0].message.content.strip()
