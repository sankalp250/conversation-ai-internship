from typing import List, Dict, Any
from config.project_config import config

class ConversationManager:
    def __init__(
        self,
        max_turns: int = config.MAX_CONVERSATION_TURNS,
        summary_interval: int = config.SUMMARY_INTERVAL,
        max_tokens: int = config.MAX_TOKENS,
    ):
        self.max_turns = max_turns
        self.summary_interval = summary_interval
        self.max_tokens = max_tokens
        self.turn_counter = 0
        self.conversation_history: List[Dict[str, str]] = []

    # ---------- core ----------
    def add_message(self, role: str, content: str) -> List[Dict[str, str]]:
        self.conversation_history.append({"role": role, "content": content})
        self.turn_counter += 1
        if self.turn_counter % self.summary_interval == 0:
            self.k_th_run_summarization()
        return self.conversation_history

    def get_summary(self) -> List[Dict[str, str]]:
        return self.conversation_history[-3:]

    # ---------- k-th run ----------
    def k_th_run_summarization(self) -> Dict[str, Any]:
        keep = self.conversation_history[-2:]
        print(f"📈 k-th run: summarised → kept {len(keep)} messages")
        self.conversation_history = keep
        return {"status": "summarised", "kept_messages": len(keep)}