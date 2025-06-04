import replicate
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    raise ValueError("Please add REPLICATE_API_TOKEN to your .env file")

def chat_with_ai(message, history):
    """Simple chat function that returns AI response"""
    
    # System prompt for coding help
    system_prompt = """You are CodeMentor, a helpful coding assistant. Help users with:
    - Code reviews and best practices
    - Bug fixes and optimizations  
    - Clear explanations with examples
    - Security and performance tips
    
    Be helpful, clear, and practical."""
    
    # Create full prompt
    full_prompt = f"{system_prompt}\n\nUser: {message}"
    
    try:
        # Get AI response
        output = replicate.run(
            "anthropic/claude-3.5-sonnet",
            input={
                "prompt": full_prompt,
                "max_tokens": 4000,
                "temperature": 0.7
            }
        )
        
        # Join the response and return it
        response = "".join(output)
        return response
        
    except Exception as e:
        return f"Sorry, there was an error: {str(e)}"

# Create the interface
demo = gr.ChatInterface(
    chat_with_ai,
    title="🎯 CodeMentor",
    description="Your simple AI coding assistant for best practices and suggestions",
    examples=[
        "Review this Python function for me",
        "How can I optimize this JavaScript code?",
        "What are the best practices for this SQL query?",
        "Help me fix this bug in my code"
    ],
    retry_btn=None,
    undo_btn=None,
    clear_btn="Clear Chat"
)

# Launch the app
if __name__ == "__main__":
    demo.launch(server_name="localhost", server_port=7861)