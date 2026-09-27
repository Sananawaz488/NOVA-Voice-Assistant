import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

from ai import ask_ai


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="NOVA AI",
    page_icon="🎤",
    layout="centered"
)


# ==========================================
# LOAD CSS
# ==========================================

with open("static/style.css", "r", encoding="utf-8") as f:
    css = f.read()

st.markdown(
    "<style>" + css + "</style>",
    unsafe_allow_html=True
)


# ==========================================
# SESSION STATE
# ==========================================

if "user_message" not in st.session_state:
    st.session_state.user_message = "Say something..."

if "nova_message" not in st.session_state:
    st.session_state.nova_message = (
        "Hello! I'm NOVA. How can I help you?"
    )


# ==========================================
# COMMAND HANDLER
# ==========================================

def get_response(message):

    text = message.lower().strip()

    # -----------------------------
    # GOOGLE SEARCH
    # -----------------------------

    if "google" in text and any(
        word in text
        for word in [
            "search",
            "dhoondo",
            "dhoondho",
            "find"
        ]
    ):

        query = text

        remove_words = [
            "google",
            "search",
            "dhoondo",
            "dhoondho",
            "find",
            "par",
            "pe",
            "mein",
            "me",
            "karo",
            "kar do"
        ]

        for word in remove_words:
            query = query.replace(word, " ")

        query = " ".join(query.split())

        if query:

            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote(query)
            )

            return (
                f"Google par {query} search kar raha hoon.",
                url
            )


    # -----------------------------
    # YOUTUBE SEARCH
    # -----------------------------

    if "youtube" in text and any(
        word in text
        for word in [
            "search",
            "dhoondo",
            "dhoondho",
            "find",
            "play",
            "chalao"
        ]
    ):

        query = text

        remove_words = [
            "youtube",
            "search",
            "dhoondo",
            "dhoondho",
            "find",
            "play",
            "chalao",
            "chala do",
            "par",
            "pe",
            "mein",
            "me",
            "karo",
            "kar do"
        ]

        for word in remove_words:
            query = query.replace(word, " ")

        query = " ".join(query.split())

        if query:

            url = (
                "https://www.youtube.com/results?search_query="
                + urllib.parse.quote(query)
            )

            return (
                f"YouTube par {query} search kar raha hoon.",
                url
            )


    # -----------------------------
    # OPEN GOOGLE
    # -----------------------------

    if (
        "google kholo" in text
        or "google khol do" in text
        or "open google" in text
    ):

        return (
            "Google khol raha hoon.",
            "https://www.google.com"
        )


    # -----------------------------
    # OPEN YOUTUBE
    # -----------------------------

    if (
        "youtube kholo" in text
        or "youtube khol do" in text
        or "open youtube" in text
    ):

        return (
            "YouTube khol raha hoon.",
            "https://www.youtube.com"
        )


    # -----------------------------
    # NORMAL AI
    # -----------------------------

    return ask_ai(message), None


# ==========================================
# NOVA MAIN UI
# ==========================================

user_message = st.session_state.user_message
nova_message = st.session_state.nova_message


html = f"""
<div class="nova-wrapper">
<div class="nova-card">

<div class="brand">

<div class="logo">
<div class="logo-ring"></div>
<div class="logo-core">N</div>
</div>

<h1>NOVA</h1>

<p>Your personal AI voice assistant</p>

</div>


<div class="status">

<span class="status-dot"></span>

<span>Ready to listen</span>

</div>


<div class="conversation">

<div class="message">

<span class="label">YOU</span>

<p>{user_message}</p>

</div>


<div class="message">

<span class="label">NOVA</span>

<p>{nova_message}</p>

</div>

</div>

</div>
</div>
"""


st.markdown(
    html,
    unsafe_allow_html=True
)


# ==========================================
# MICROPHONE
# ==========================================

with open("static/script.js", "r", encoding="utf-8") as f:
    javascript = f.read()


components.html(
    f"""
    <div class="voice-area">

    <button id="micButton" class="mic-button">
    🎤
    </button>

    <p id="statusText">
    Tap the microphone and start speaking
    </p>

    <p id="heardText"></p>

    </div>

    <script>
    {javascript}
    </script>
    """,
    height=180
)


# ==========================================
# TEXT INPUT
# ==========================================

st.markdown(
    "<div class='input-title'>Or type your message</div>",
    unsafe_allow_html=True
)


message = st.text_input(
    "Message",
    placeholder="Type a message...",
    label_visibility="collapsed"
)


if st.button("Send ➤"):

    if message.strip():

        st.session_state.user_message = message

        reply, url = get_response(message)

        st.session_state.nova_message = reply

        if url:

            st.markdown(
                f"""
                <script>
                window.open("{url}", "_blank");
                </script>
                """,
                unsafe_allow_html=True
            )

        st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
    Powered by <strong>Groq AI</strong>
    </div>
    """,
    unsafe_allow_html=True
)
