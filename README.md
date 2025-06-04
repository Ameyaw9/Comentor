
#  CodeMentor

CodeMentor is an AI-powered coding assistant that helps developers write better code by providing code reviews, best practices, and optimization suggestions.



##  Features

- 🤖 AI-powered code analysis and suggestions
- 📝 Code review and best practices recommendations
- 🔍 Bug detection and optimization tips
- 🛠️ Multiple programming language support
- 💡 Interactive chat interface
- 🔒 Security best practices guidance



### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A Replicate API token

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/code-mentor.git
cd code-mentor
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Replicate API token:
```
REPLICATE_API_TOKEN=your_token_here
```

### Running the Application

Start the application with:
```bash
python code_mentor/comentor.py
```

The application will be available at `http://localhost:7861`


## Usage


1. Open your web browser and navigate to `http://localhost:7861`
2. Start a conversation by:
   - Asking for code review
   - Requesting optimization suggestions
   - Seeking best practices advice
   - Getting help with bug fixes

### Example Prompts

- "Review this Python function for me"
- "How can I optimize this JavaScript code?"
- "What are the best practices for this SQL query?"
- "Help me fix this bug in my code"

## 🛠️ Technical Details

- Built with Python and Gradio
- Uses Claude 3.5 Sonnet via Replicate API
- Supports multiple programming languages
- Interactive chat interface for easy communication


