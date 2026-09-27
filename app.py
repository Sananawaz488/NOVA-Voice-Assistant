import streamlit as st
import streamlit.components.v1 as components

from ai import ask_ai


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
    f"<style>{css}</style>",
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
# AI RESPONSE
# ==========================================

def get_response(message):

    message_lower = message.lower().strip()


    # Google search
    if "google" in message_lower and any(
        word in message_lower
        for word in [
            "search",
            "dhoondo",
            "dhoondho",
            "find"
        ]
    ):

        query = message_lower

        for word in [
            "google",
            "search",
            "dhoondo",
            "dhoondho",
            "find",
            "par",
            "pe",
            "karo",
            "kar do"
        ]:
            query = query.replace(word, " ")

        query = " ".join(query.split())


        if query:

            import urllib.parse

            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote(query)
            )

            return (
                f"Google par {query} search kar raha hoon.",
                url
            )


    # YouTube search
    if "youtube" in message_lower and any(
        word in message_lower
        for word in [
            "search",
            "dhoondo",
            "dhoondho",
            "find",
            "play",
            "chalao"
        ]
    ):

        query = message_lower

        for word in [
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
            "karo",
            "kar do"
        ]:
            query = query.replace(word, " ")

        query = " ".join(query.split())


        if query:

            import urllib.parse

            url = (
                "https://www.youtube.com/results?search_query="
                + urllib.parse.quote(query)
            )

            return (
                f"YouTube par {query} search kar raha hoon.",
                url
            )


    # Normal AI conversation
    return ask_ai(message), None


# ==========================================
# NOVA UI
# ==========================================

st.markdown(
    """
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

                <span>
                    Ready to listen
                </span>

            </div>


            <div class="conversation">

                <div class="message">

                    <span class="label">
                        YOU
                    </span>

                    <p>
    """
    + st.session_state.user_message
    + """
                    </p>

                </div>


                <div class="message">

                    <span class="label">
                        NOVA
                    </span>

                    <p>
    """
    + st.session_state.nova_message
    + """
                    </p>

                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# VOICE + JAVASCRIPT
# ==========================================

with open("static/script.js", "r", encoding="utf-8") as f:
    javascript = f.read()


components.html(
    f"""
    <div class="voice-area">

        <button
            id="micButton"
            class="mic-button"
        >
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
# TEXT INPUT FALLBACK
# ==========================================

st.markdown(
    "<div class='input-title'>Or type your message</div>",
    unsafe_allow_html=True
)


message = st.text_input(
    "",
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


st.markdown(
    """
    <div class="footer">
        Powered by <strong>Groq AI</strong>
    </div>
    """,
    unsafe_allow_html=True
)
