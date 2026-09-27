import os

from groq import Groq
from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


client = Groq(
    api_key=api_key
)


def transcribe_audio(audio_file):

    with open(audio_file, "rb") as file:

        result = client.audio.transcriptions.create(

            file=file,

            model="whisper-large-v3",

            response_format="text"
        )


    return result.strip()
