#!/usr/bin/env python3
import openai, json
from src.conversation_manager import ConversationManager
from src.information_extractor import InformationExtractor
from config.project_config import config

openai.api_key = input("Groq key: ").strip()
openai.base_url = "https://api.groq.com/openai/v1/"

cm = ConversationManager(
    max_turns=config.MAX_CONVERSATION_TURNS,
    summary_interval=config.SUMMARY_INTERVAL,
    max_tokens=config.MAX_TOKENS)
ie = InformationExtractor()

def llm_reply(messages):
    resp = openai.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.3
    )
    print(f"📊 tokens: prompt={resp.usage.prompt_tokens}  "
          f"completion={resp.usage.completion_tokens}  total={resp.usage.total_tokens}")
    return resp.choices[0].message.content

print("\n🟢 Chat started!  /extract  /summary  /quit\n")
while True:
    user = input("You: ").strip()
    if user == "/quit":
        break
    if user == "/summary":
        print("Bot: 📋", json.dumps(cm.get_summary(), indent=2))
        continue
    if user == "/extract":
        data = ie.extract_information(cm.conversation_history)
        print("Bot: 🔍 EXTRACTION EVIDENCE\n", json.dumps(data, indent=2))
        # quick token count of current history
        tok = sum(len(m["content"].split()) for m in cm.conversation_history)
        print(f"📊 HISTORY TOKENS NOW: {tok}")
        continue

    cm.add_message("user", user)
    bot = llm_reply(cm.conversation_history)
    cm.add_message("assistant", bot)
    print("Bot:", bot)

    # ---- live evidence for evaluator ----
    if cm.turn_counter % cm.summary_interval == 0:
        print(f"📈 SUMMARY EVIDENCE – turn {cm.turn_counter}: "
              f"history now {len(cm.conversation_history)} messages")