from typing import List, Dict, Any
import openai, json

EXTRACTION_FUNCTION = {
    "name": "extract_user_info",
    "description": "Extract name, email, phone, location, age from the conversation.",
    "parameters": {
        "type": "object",
        "properties": {
            "name":     {"type": "string"},
            "email":    {"type": "string"},
            "phone":    {"type": "string"},
            "location": {"type": "string"},
            "age":      {"type": "integer"}
        },
        "required": ["name", "email", "phone", "location", "age"]
    }
}

class InformationExtractor:
    def extract_information(self, conversation: List[Dict[str, str]]) -> Dict[str, Any]:
        resp = openai.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation,
            functions=[EXTRACTION_FUNCTION],
            function_call={"name": "extract_user_info"},
            temperature=0
        )
        try:
            args = json.loads(resp.choices[0].message.function_call.arguments)
            return args
        except Exception:
            return {"name": None, "email": None, "phone": None, "location": None, "age": None}