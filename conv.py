import re

exit_text = [
    r"\bbye\b",
    r"\bgood\s?bye\b",
    r"\bsee you later\b",
    r"\btalk to you later\b",
    r"\bcatch you later\b",
    r"\bhave a (great|nice|good) day\b",
    r"\bhave a good night\b",
    r"\bgood ?night\b",
    r"\bthanks?\b.*\bbye\b",
    r"\bthank you\b.*\bgoodbye\b",
    r"\b(that'?s all|that'?s it)\b",
    r"\bnothing else\b",
    r"\bi'?m done\b",
    r"\bi am done\b",
    r"\bstop (listening|bantu)\b",
    r"\bmute bantu\b",
    r"\bshutdown bantu\b",
    r"\bshut ?down bantu\b",
    r"\bturn off bantu\b",
    r"\bsleep bantu\b",
    r"\bgo to sleep bantu\b",
    r"\bpower down bantu\b",
    r"\bbantu mute\b",
    r"\bexit\b",
    r"\bquit\b"
]