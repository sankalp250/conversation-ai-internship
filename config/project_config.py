
"""
Configuration settings for the Conversation AI System
Internship Assignment Project
"""

import os
from typing import Dict, Any

class ProjectConfig:
    """
    Centralized configuration management for the project
    Handles all settings for both Task 1 and Task 2
    """
    
    # API Configuration
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "your-groq-api-key-here")  
    GROQ_BASE_URL: str = "https://api.groq.com/openai/v1"
    
    # Task 1: Conversation Management Settings
    MAX_CONVERSATION_TURNS: int = 10
    SUMMARY_INTERVAL: int = 3  # K-value for k-th run summarization
    MAX_TOKENS: int = 4000
    TRUNCATION_METHODS = ["turns", "length", "tokens"]
    
    # Task 2: Information Extraction Settings
    EXTRACTION_FIELDS = ["name", "email", "phone", "location", "age"]
    CONFIDENCE_THRESHOLD: float = 0.7
    
    # File Paths
    PROJECT_ROOT = "/content/drive/MyDrive/conversation-ai-internship"
    DATA_PATH = f"{PROJECT_ROOT}/data"
    OUTPUT_PATH = f"{PROJECT_ROOT}/outputs"
    
    # Model Settings
    MODEL_NAME: str = "llama3-8b-8192"  # Groq's fastest model
    TEMPERATURE: float = 0.3
    MAX_RETRIES: int = 3
    
    @classmethod
    def get_all_settings(cls) -> Dict[str, Any]:
        """Return all configuration settings as a dictionary"""
        return {
            attr: getattr(cls, attr) 
            for attr in dir(cls) 
            if not attr.startswith('_') and not callable(getattr(cls, attr))
        }

# Create configuration instance
config = ProjectConfig()
