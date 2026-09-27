const micButton =
    document.getElementById("micButton");

const statusText =
    document.getElementById("statusText");

const heardText =
    document.getElementById("heardText");


const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;


let recognition = null;

let listening = false;


if (SpeechRecognition) {

    recognition =
        new SpeechRecognition();


    recognition.continuous = false;

    recognition.interimResults = false;

    recognition.lang = "en-US";


    recognition.onstart = function () {

        listening = true;

        micButton.classList.add(
            "recording"
        );

        statusText.textContent =
            "Listening... Speak now 🎤";
    };


    recognition.onresult =
        function(event) {

            const text =
                event.results[0][0]
                .transcript
                .trim();


            heardText.textContent =
                "You said: " + text;


            statusText.textContent =
                "You said: " + text;


            /*
             * Search commands are opened
             * directly in the browser.
             */

            const lower =
                text.toLowerCase();


            if (
                lower.includes("google") &&
                (
                    lower.includes("search") ||
                    lower.includes("dhoondo") ||
                    lower.includes("find")
                )
            ) {

                let query = text;

                query =
                    query.replace(
                        /google/gi,
                        ""
                    );

                query =
                    query.replace(
                        /search/gi,
                        ""
                    );

                query =
                    query.replace(
                        /dhoondo/gi,
                        ""
                    );

                query =
                    query.replace(
                        /find/gi,
                        ""
                    );

                query =
                    query.replace(
                        /par/gi,
                        ""
                    );

                query =
                    query.replace(
                        /karo/gi,
                        ""
                    );

                query =
                    query.trim();


                const url =
                    "https://www.google.com/search?q=" +
                    encodeURIComponent(query);


                window.open(
                    url,
                    "_blank"
                );


                return;
            }


            if (
                lower.includes("youtube") &&
                (
                    lower.includes("search") ||
                    lower.includes("play") ||
                    lower.includes("dhoondo") ||
                    lower.includes("find")
                )
            ) {

                let query = text;

                query =
                    query.replace(
                        /youtube/gi,
                        ""
                    );

                query =
                    query.replace(
                        /search/gi,
                        ""
                    );

                query =
                    query.replace(
                        /play/gi,
                        ""
                    );

                query =
                    query.replace(
                        /dhoondo/gi,
                        ""
                    );

                query =
                    query.replace(
                        /find/gi,
                        ""
                    );

                query =
                    query.replace(
                        /par/gi,
                        ""
                    );

                query =
                    query.replace(
                        /karo/gi,
                        ""
                    );

                query =
                    query.trim();


                const url =
                    "https://www.youtube.com/results?search_query=" +
                    encodeURIComponent(query);


                window.open(
                    url,
                    "_blank"
                );


                return;
            }


            /*
             * For normal conversation,
             * send the voice text to Streamlit.
             *
             * Streamlit's normal Python
             * interaction will handle it
             * through the text input fallback.
             */

            statusText.textContent =
                "Voice captured: " + text;
        };


    recognition.onerror =
        function(event) {

            console.error(
                event.error
            );


            statusText.textContent =
                "Voice error. Try again.";

            listening = false;

            micButton.classList.remove(
                "recording"
            );
        };


    recognition.onend =
        function() {

            listening = false;

            micButton.classList.remove(
                "recording"
            );
        };


    micButton.addEventListener(
        "click",
        function() {

            if (listening) {

                recognition.stop();

                return;
            }


            try {

                recognition.start();

            } catch (error) {

                console.error(error);

            }

        }
    );

} else {

    statusText.textContent =
        "Please use Google Chrome for voice.";
}
