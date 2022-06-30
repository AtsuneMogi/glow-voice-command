const message = document.getElementById("message");
const content = document.getElementById("content");

function main() {
    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    var speech = new SpeechRecognition();
    speech.lang = "en-US";
    speech.interimResults = true;
    speech.continuous = true;

    speech.onsoundstart = function() {
        speech.start();
    };
    speech.onerror = function() {
        if(speeching == 0) {
            main();
        }
    };
    speech.onsoundend = function() {
        main();
    };
    speech.onresult = function(e) {
        var results = e.results;
        for (var i = e.resultIndex; i < results.length; i++) {
            var result = results[i][0].transcript;
            if (results[i].isFinal) {
                content.textContent = result;
                main();
            } else {
                content.textContent = result;
                speeching = 1;
            }
        }
    }
    speeching = 0;
    speech.start();
}
