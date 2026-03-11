import pyttsx3
import speech_recognition as sr
import datetime as dt
import json
import re
from conv import exit_text

from groq import Groq
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from config import GROQ_API_KEY

# ── MCP Tool Definitions ──────────────────────────────────────────────────────
# Add / remove tools here as your MCP server expands.
MCP_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "open_application",
            "description": "Opens a desktop application by name (e.g. Notepad, Chrome, Spotify).",
            "parameters": {
                "type": "object",
                "properties": {
                    "app_name": {"type": "string", "description": "Name of the application to open."}
                },
                "required": ["app_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Searches the web for a given query and returns a short summary.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query string."}
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Returns the current local date and time.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "set_reminder",
            "description": "Sets a reminder for the user at a specified time.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Reminder message."},
                    "time":    {"type": "string", "description": "Time for the reminder in HH:MM 24h format."},
                },
                "required": ["message", "time"],
            },
        },
    },
]

# ── MCP Tool Executor ─────────────────────────────────────────────────────────



# Wire each tool name to its real implementation below.
def execute_tool(tool_name: str, tool_args: dict) -> str:
    """Dispatch a tool call and return a plain-text result string."""

    if tool_name == "get_current_time":
        now = dt.datetime.now()
        return f"The current date and time is {now.strftime('%A, %B %d %Y at %I:%M %p')}."

    elif tool_name == "open_application":
        app = tool_args.get("app_name", "")
        import subprocess, shutil
        # Basic cross-platform launcher – extend as needed
        try:
            if shutil.which(app.lower()):
                subprocess.Popen([app.lower()])
            else:
                subprocess.Popen(["start", app], shell=True)   # Windows fallback
            return f"{app} has been opened successfully."
        except Exception as e:
            return f"I was unable to open {app}: {e}"

    elif tool_name == "search_web":
        query = tool_args.get("query", "")
        import webbrowser, urllib.parse
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        webbrowser.open(url)
        return f"I have opened a Google search for '{query}' in your browser."

    elif tool_name == "set_reminder":
        message = tool_args.get("message", "")
        time    = tool_args.get("time", "")
        # Placeholder – integrate with your preferred scheduler (e.g. Windows Task Scheduler)
        return f"Reminder set for {time}: '{message}'."

    else:
        return f"Tool '{tool_name}' is not implemented yet."


# ── Voice Agent ───────────────────────────────────────────────────────────────
class Voice_Agent:

    # Conversation history shared across the session (maintains context)
    _conversation_history = [
        {"role": "system", "content": AGENT_INSTRUCTION + "\n\n" + SESSION_INSTRUCTION}
    ]

    # ── TTS ───────────────────────────────────────────────────────────────────
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # Slightly slower rate feels more butler-like
    engine.setProperty('rate', 165)
    
    speaking = False

    def _speak(self, audio: str):
        """Convert text to speech using pyttsx3 (sapi5)."""
        global speaking
        global engine
        # Strip markdown / special characters so TTS sounds natural
        clean = re.sub(r"[*_#`>~]", "", audio).strip()
        print(f"\nBantu: {clean}\n")

        speaking = True 

        engine.say(clean)
        engine.runAndWait()


        speaking = False

    def _stop_speaking():
        global speaking
        if speaking:
            engine.stop()
            speaking = False

    # ── STT ───────────────────────────────────────────────────────────────────
    def _commands(self):
        """Capture microphone input and return a text query."""
        
        Voice_Agent.stop_speaking()
        
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.0               #TODO - edit the Threshold of the AI Listening
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=None)

        try:
            print("Processing...\n")
            query = r.recognize_google(audio, language='en-in')
            print(f"Ravi: {query}\n")

            #TODO - Make it as dynamic as possible with the exit phrase 
            if any(re.search(pattern, query.lower()) for pattern in exit_text):
                hour = dt.datetime.now().hour
                if hour >= 20 or hour < 6:
                    Voice_Agent.speak("Good night, sir. Do try to rest — you've earned it.")
                else:
                    Voice_Agent.speak("Have a splendid day, sir. Try not to get into too much trouble.")
                exit()

        except Exception as e:
            print(f"STT Error: {e}")
            Voice_Agent.speak("My sincerest apologies, sir — I didn't quite catch that. Could you repeat yourself?")
            query = "none"

        return query

    # ── LLM (Groq + MCP tool loop) ────────────────────────────────────────────
    def _reply_groqai(self, query: str):
        """Send query to Groq, handle any MCP tool calls, and return final answer."""

        client = Groq(api_key=GROQ_API_KEY)

        # Append the new user message to rolling history
        Voice_Agent._conversation_history.append({"role": "user", "content": query})

        # ── Agentic tool-call loop ────────────────────────────────────────────
        while True:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",   # tool-use capable model
                messages=Voice_Agent._conversation_history,
                tools=MCP_TOOLS,
                tool_choice="auto",
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=False,                                    # streaming off during tool loop
                stop=None,
            )

            response_message = completion.choices[0].message

            # ── No tool call → final text answer ─────────────────────────────
            if not response_message.tool_calls:
                answer = response_message.content or ""
                Voice_Agent._conversation_history.append({"role": "assistant", "content": answer})
                return answer

            # ── Tool call(s) requested ────────────────────────────────────────
            # Add assistant's tool-call message to history
            Voice_Agent._conversation_history.append(response_message)

            for tool_call in response_message.tool_calls:
                tool_name   = tool_call.function.name
                tool_args   = json.loads(tool_call.function.arguments)

                ## Used for Testing purposes only
                print(f"[MCP] Executing tool: {tool_name}({tool_args})")
                tool_result = execute_tool(tool_name, tool_args)
                print(f"[MCP] Result: {tool_result}\n")

                # Feed the result back into conversation history
                Voice_Agent._conversation_history.append({
                    "role":         "tool",
                    "tool_call_id": tool_call.id,
                    "content":      tool_result,
                })

            # Loop again so the model can formulate its final reply

    # ── Main STT → LLM → TTS loop ─────────────────────────────────────────────
    def run(self):
        """Start Bantu: greet, then enter the continuous listen-think-speak loop."""

        # Opening greeting (SESSION_INSTRUCTION drives the content)
        greeting = Voice_Agent.reply_groqai("Begin the session with your introduction.")
        Voice_Agent.speak(greeting)

        try:
            while True:
                query = Voice_Agent.commands()

                if query == "none":
                    continue

                answer = Voice_Agent.reply_groqai(query)
                Voice_Agent.speak(answer)
                
        except KeyboardInterrupt:
            print("\nSystem Shutting Down...")
            Voice_Agent.speak("System shutting down")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    Voice_Agent.run()