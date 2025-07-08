# YouTube Bot RAG 🤖

A powerful YouTube content analysis bot powered by RAG (Retrieval-Augmented Generation) technology. This bot helps process and analyze YouTube content using advanced NLP techniques and embeddings.

## 🌟 Features

- YouTube content processing and analysis
- RAG-based information retrieval
- Embedding generation and management
- Advanced prompt templating
- API integration with various services

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager
- YouTube API credentials
- Required API keys (check config section)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Palak-Gangwani-10/YouTube_Bot_RAG.git
cd YouTube_Bot_RAG
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your environment:
   - Copy `config/config.example.py` to `config/config.py`
   - Add your API keys and configurations

## 🛠️ Project Structure

```
YouTube_BOT_RAG/
├── app.py              # Main application entry point
├── config/
│   └── config.py      # Configuration settings
├── main.py            # Core functionality
├── utils/
│   ├── api_helpers.py       # API integration utilities
│   ├── embedding_utils.py   # Embedding generation tools
│   ├── prompt_templates.py  # Prompt management
│   ├── rag_pipeline.py     # RAG implementation
│   └── retriever_utils.py  # Content retrieval utilities
└── test_cohere.py     # Testing module
```

## 💻 Usage

1. Start the bot:
```bash
python app.py
```

2. Process YouTube content:
```python
from main import process_content

results = process_content("VIDEO_ID")
```

## 🔧 Configuration

The project uses a configuration file located at `config/config.py`. Required settings include:

- YouTube API credentials
- Embedding model configurations
- RAG parameters
- API endpoints and keys

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by modern RAG implementations
- Built with powerful open-source tools

## 🔮 Future Improvements

- [ ] Add support for multiple video processing
- [ ] Implement batch processing
- [ ] Enhance embedding models
- [ ] Add more analysis features
- [ ] Improve documentation
