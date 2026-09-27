from groq import Groq
import os


def get_client():

    try:
        api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            return None

        return Groq(api_key=api_key)

    except Exception:
        return None
