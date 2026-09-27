import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
import os
import re
import urllib.parse


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="NOVA Voice Assistant",
    page_icon="🎙️",
    layout="centered"
)


# =========================================================
# GROQ API KEY
# =========================================================

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


if not GROQ_API_KEY:
    st.error("GROQ_API_KEY is missing. Add it in Streamlit Secrets.")
    st.stop()


client = Groq(api_key=GROQ_API_KEY)


# =========================================================
# SESSION STATE
# =========================================================

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "response" not in st.session_state:
    st.session_state.response = ""

if "last_audio_id" not in st.session_state:
    st.session_state.last_audio_id = None

if "action_url" not in st.session_state:
    st.session_state.action_url = None

if "action_name" not in st.session_state:
    st.session_state.action_name = None


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
        radial-gradient(circle at top, #182033 0%, #090b12 45%, #05060a 100%);
    }

    .main-title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        letter-spacing: 5px;
        margin-top: 20px;
        margin-bottom: 0;
        color: white;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 15px;
        margin-bottom: 30px;
    }

    .nova-card {
        background: rgba(20, 24, 35, 0.85);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        padding: 25px;
        margin-top: 15px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.35);
    }

    .label {
        color: #9ca3af;
        font-size: 13px;
        margin-bottom: 7px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .message {
        color: white;
        font-size: 17px;
        line-height: 1.6;
    }

    .status {
        text-align: center;
        color: #22c55e;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .mic-title {
        text-align: center;
        color: white;
        font-size: 20px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 12px;
        margin-top: 35px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">NOVA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI Voice Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="status">● ONLINE</div>',
    unsafe_allow_html=True
)


# =========================================================
# COMMAND HANDLER
# =========================================================

def handle_command(text):

    text_lower = text.lower().strip()

    st.session_state.action_url = None
    st.session_state.action_name = None

    # -----------------------------------------------------
    # GOOGLE
    # -----------------------------------------------------

    if (
        "google kholo" in text_lower
        or "google open" in text_lower
        or text_lower == "google"
    ):

        return (
            "Sure, opening Google.",
            "https://www.google.com",
            "Open Google"
        )


    # -----------------------------------------------------
    # YOUTUBE
    # -----------------------------------------------------

    if (
        "youtube kholo" in text_lower
        or "youtube open" in text_lower
        or text_lower == "youtube"
    ):

        return (
            "Sure, opening YouTube.",
            "https://www.youtube.com",
            "Open YouTube"
        )


    # -----------------------------------------------------
    # GOOGLE SEARCH
    # -----------------------------------------------------

    google_words = [
        "google par",
        "google pe",
        "google mein",
        "google me",
        "google search"
    ]

    if any(word in text_lower for word in google_words):

        query = text_lower

        for word in google_words:
            query = query.replace(word, "")

        query = re.sub(
            r"\b(search|karo|karein|kar do|please|dhoondo|dhoondho|find)\b",
            "",
            query
        ).strip()

        if query:

            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote(query)
            )

            return (
                f"Searching Google for {query}.",
                url,
                f"Search Google: {query}"
            )


    # -----------------------------------------------------
    # YOUTUBE SEARCH
    # -----------------------------------------------------

    youtube_words = [
        "youtube par",
        "youtube pe",
        "youtube mein",
        "youtube me",
        "youtube search"
    ]

    if any(word in text_lower for word in youtube_words):

        query = text_lower

        for word in youtube_words:
            query = query.replace(word, "")

        query = re.sub(
            r"\b(search|karo|karein|kar do|please|dhoondo|dhoondho|find|play|chalao|chala do)\b",
            "",
            query
        ).strip()

        if query:

            url = (
                "https://www.youtube.com/results?search_query="
                + urllib.parse.quote(query)
            )

            return (
                f"Searching YouTube for {query}.",
                url,
                f"Search YouTube: {query}"
            )


    # -----------------------------------------------------
    # WHATSAPP
    # -----------------------------------------------------

    if (
        "whatsapp kholo" in text_lower
        or "whatsapp open" in text_lower
        or text_lower == "whatsapp"
    ):

        return (
            "Opening WhatsApp.",
            "https://web.whatsapp.com",
            "Open WhatsApp"
        )


    # -----------------------------------------------------
    # GMAIL
    # -----------------------------------------------------

    if (
        "gmail kholo" in text_lower
        or "gmail open" in text_lower
        or text_lower == "gmail"
    ):

        return (
            "Opening Gmail.",
            "https://mail.google.com",
            "Open Gmail"
        )


    # -----------------------------------------------------
    # INSTAGRAM
    # -----------------------------------------------------

    if (
        "instagram kholo" in text_lower
        or "instagram open" in text_lower
        or text_lower == "instagram"
    ):

        return (
            "Opening Instagram.",
            "https://www.instagram.com",
            "Open Instagram"
        )


    # -----------------------------------------------------
    # FACEBOOK
    # -----------------------------------------------------

    if (
        "facebook kholo" in text_lower
        or "facebook open" in text_lower
        or text_lower == "facebook"
    ):

        return (
            "Opening Facebook.",
            "https://www.facebook.com",
            "Open Facebook"
        )


    # -----------------------------------------------------
    # GITHUB
    # -----------------------------------------------------

    if (
        "github kholo" in text_lower
        or "github open" in text_lower
        or text_lower == "github"
    ):

        return (
            "Opening GitHub.",
            "https://github.com",
            "Open GitHub"
        )


    # -----------------------------------------------------
    # MAPS
    # -----------------------------------------------------

    if (
        "maps kholo" in text_lower
        or "google maps kholo" in text_lower
        or "maps open" in text_lower
    ):

        return (
            "Opening Google Maps.",
            "https://maps.google.com",
            "Open Google Maps"
        )


    # -----------------------------------------------------
    # CALCULATOR
    # -----------------------------------------------------

    if (
        "calculator kholo" in text_lower
        or "calculator open" in text_lower
    ):

        return (
            "Opening calculator.",
            "https://www.google.com/search?q=calculator",
            "Open Calculator"
        )


    # -----------------------------------------------------
    # NORMAL GROQ AI
    # -----------------------------------------------------

    try:

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[

                {
                    "role": "system",
                    "content": """
You are NOVA, a friendly personal voice assistant.

The user can speak English, Urdu or Roman Urdu.

If the user speaks English, reply in English.

If the user speaks Roman Urdu, reply naturally
in Roman Urdu.

Keep answers short because they are spoken aloud.

Be friendly and natural.

Do not say "As an AI" unless the user asks.

You are a voice assistant, so avoid long answers.
"""
                },

                {
                    "role": "user",
                    "content": text
                }

            ],

            temperature=0.4,

            max_tokens=200
        )

        answer = response.choices[0].message.content.strip()

        return answer, None, None

    except Exception as e:

        return (
            "Sorry, I could not connect to Groq right now.",
            None,
            None
        )


# =========================================================
# SPEAK RESPONSE
# =========================================================

def speak_response(text):

    safe_text = (
        text
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("$", "\\$")
    )

    html = f"""
    <script>

    const text = `{safe_text}`;

    function speak() {{

        if (!window.speechSynthesis) {{
            return;
        }}

        window.speechSynthesis.cancel();

        const speech = new SpeechSynthesisUtterance(text);

        speech.lang = "en-US";
        speech.rate = 0.95;
        speech.pitch = 1.05;
        speech.volume = 1;

        const voices = window.speechSynthesis.getVoices();

        const preferred = voices.find(v =>
            /female|zira|samantha|google uk english female|google us english/i
            .test(v.name)
        );

        if (preferred) {{
            speech.voice = preferred;
        }}

        window.speechSynthesis.speak(speech);
    }}

    setTimeout(speak, 400);

    </script>
    """

    components.html(
        html,
        height=1
    )


# =========================================================
# CONVERSATION DISPLAY
# =========================================================

if st.session_state.transcript:

    st.markdown(
        """
        <div class="nova-card">
            <div class="label">You said</div>
            <div class="message">
        """,
        unsafe_allow_html=True
    )

    st.write(st.session_state.transcript)

    st.markdown(
        """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


if st.session_state.response:

    st.markdown(
        """
        <div class="nova-card">
            <div class="label">NOVA</div>
            <div class="message">
        """,
        unsafe_allow_html=True
    )

    st.write(st.session_state.response)

    st.markdown(
        """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# VOICE INPUT
# =========================================================

st.markdown(
    '<div class="mic-title">🎤 Speak to NOVA</div>',
    unsafe_allow_html=True
)

audio = st.audio_input(
    "Tap the microphone and speak"
)


# =========================================================
# PROCESS AUDIO
# =========================================================

if audio is not None:

    audio_id = str(audio.file_id) if hasattr(audio, "file_id") else str(audio)

    if audio_id != st.session_state.last_audio_id:

        st.session_state.last_audio_id = audio_id

        try:

            with st.spinner("NOVA is listening..."):

                audio_bytes = audio.read()

                transcription = client.audio.transcriptions.create(

                    file=("voice.wav", audio_bytes),

                    model="whisper-large-v3",

                    response_format="text"
                )

                text = transcription.strip()


            if text:

                st.session_state.transcript = text

                with st.spinner("NOVA is thinking..."):

                    answer, url, action_name = handle_command(text)

                st.session_state.response = answer

                st.session_state.action_url = url

                st.session_state.action_name = action_name

                st.rerun()

        except Exception as e:

            st.error(
                "Voice processing error. Please try again."
            )


# =========================================================
# ACTION BUTTON
# =========================================================

if st.session_state.action_url:

    st.markdown("---")

    st.link_button(
        f"🔗 {st.session_state.action_name}",
        st.session_state.action_url,
        use_container_width=True
    )


# =========================================================
# TEXT FALLBACK
# =========================================================

st.markdown("---")

text_input = st.text_input(
    "Or type a command",
    placeholder="Example: YouTube par Python tutorials search karo"
)

if st.button(
    "Send to NOVA",
    use_container_width=True
):

    if text_input.strip():

        st.session_state.transcript = text_input.strip()

        with st.spinner("NOVA is thinking..."):

            answer, url, action_name = handle_command(
                text_input.strip()
            )

        st.session_state.response = answer
        st.session_state.action_url = url
        st.session_state.action_name = action_name

        st.rerun()


# =========================================================
# SPEAK LAST RESPONSE
# =========================================================

if st.session_state.response:

    speak_response(
        st.session_state.response
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">Powered by Groq • NOVA Voice Assistant</div>',
    unsafe_allow_html=True
)
