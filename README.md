# 🤖 Conversation AI Internship Project

A production-ready AI conversation management system with intelligent summarization and automatic information extraction, built using Groq's high-speed inference API.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-API-green.svg)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Project Overview

This project demonstrates advanced conversation management capabilities with two core features:

1. **Intelligent Conversation Management**: Multi-strategy truncation and K-th run summarization
2. **Automatic Information Extraction**: JSON schema-based data extraction with confidence scoring

Built for an internship assignment, showcasing production-ready code with proper configuration management, error handling, and performance optimization.

## 🎯 Assignment Tasks

### Task 1: Conversation Management & Summarization
- ✅ **Multi-Strategy Truncation**: Turn-based, length-based, and token-aware truncation
- ✅ **K-th Run Summarization**: Configurable interval-based summarization (default: every 3 turns)
- ✅ **Performance Optimization**: Real-time token usage tracking and efficiency metrics
- ✅ **Context Preservation**: Maintains important conversation elements during truncation
- ✅ **Live Monitoring**: Real-time evidence display for evaluation

### Task 2: JSON Schema Information Extraction
- ✅ **Comprehensive Schema**: Extracts 5+ fields (name, email, phone, location, age)
- ✅ **Function Calling**: OpenAI-compatible function calling with Groq API
- ✅ **Multi-Chat Processing**: Handles various conversation types and formats
- ✅ **Confidence Scoring**: Reliability metrics for extracted data (threshold: 0.7)
- ✅ **Validation**: Pydantic-based data validation and error handling

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sankalp250/conversation-ai-internship.git
   cd conversation-ai-internship
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the template and add your API key
   cp .env.template .env
   # Edit .env and add your Groq API key
   ```

4. **Run the interactive chat**
   ```bash
   python run_chat.py
   ```

### Usage

#### Interactive Chat Commands
- **Normal conversation**: Just type your message
- **`/summary`**: Get conversation summary
- **`/extract`**: Extract structured information from conversation
- **`/quit`**: Exit the chat

#### Example Session
```
🟢 Chat started!  /extract  /summary  /quit

You: Hi, I'm John Smith, 25 years old from New York. My email is john@example.com and phone is 555-1234.
Bot: Hello John! Nice to meet you. How can I help you today?
📊 tokens: prompt=45  completion=12  total=57

You: /extract
Bot: 🔍 EXTRACTION EVIDENCE
{
  "name": "John Smith",
  "email": "john@example.com", 
  "phone": "555-1234",
  "location": "New York",
  "age": 25,
  "confidence": 0.95
}
📊 HISTORY TOKENS NOW: 67
```

## 🏗️ Project Structure

```
conversation-ai-internship/
├── src/
│   ├── conversation_manager.py    # Task 1: Conversation management
│   └── information_extractor.py   # Task 2: Information extraction
├── config/
│   └── project_config.py          # Centralized configuration
├── data/
│   └── sample_conversations.json  # Sample data for testing
├── outputs/                       # Generated outputs (gitignored)
├── run_chat.py                    # Main interactive application
├── requirements.txt               # Python dependencies
├── .env.template                  # Environment variables template
└── README.md                     # This file
```

## ⚙️ Configuration

The system uses centralized configuration in `config/project_config.py`:

### Key Settings
- **MAX_CONVERSATION_TURNS**: Maximum conversation length (default: 10)
- **SUMMARY_INTERVAL**: K-value for summarization (default: 3)
- **MAX_TOKENS**: Token limit for truncation (default: 4000)
- **CONFIDENCE_THRESHOLD**: Minimum confidence for extraction (default: 0.7)
- **MODEL_NAME**: Groq model to use (default: "llama3-8b-8192")

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key (required)

## 🔧 Development

### Running Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black src/ config/ run_chat.py
flake8 src/ config/ run_chat.py
```

### Adding New Features
1. Update configuration in `config/project_config.py`
2. Implement features in appropriate `src/` modules
3. Add tests in `tests/` directory
4. Update this README

## 📊 Performance Features

- **Real-time Token Tracking**: Monitor API usage during conversations
- **Efficient Summarization**: Configurable K-th run summarization
- **Smart Truncation**: Multiple strategies to maintain context
- **Confidence Scoring**: Reliability metrics for extracted data

## 🔒 Security

- API keys are managed through environment variables
- `.env` files are gitignored to prevent accidental exposure
- No hardcoded secrets in the codebase

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

- **Author**: Sankalp
- **Repository**: [conversation-ai-internship](https://github.com/sankalp250/conversation-ai-internship)

---

*Built with ❤️ for AI conversation management*
