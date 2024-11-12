# ME_GPT

ME_GPT revolutionizes the way you interact with Chat GPT by introducing a powerful memory storage system and self-cloning functionality. With ME_GPT, you can store your cherished memories in a local vector database and leverage them to give Chat GPT the extraordinary ability to clone your unique personality and knowledge.

## Installation & Setup:

### 1. Create and activate a Python virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install the library
```bash
pip install me-gpt
```

### 3. Create a .env file in your project directory
Create a new file named `.env` and add your OpenAI API key:
```
OPEN_AI_API_KEY=your_api_key_here
```

To get your OpenAI API key, visit: https://platform.openai.com/account/api-keys

### 4. Test the library
```python
from me_gpt import *

# Initial questions to help your clone get started:
initial_questions()

# Have your clone ask you more questions:
more_questions(number_of_questions=3)

# Ask your clone a question with custom instructions:
question = "What is your Name?"
instructions = "Give your answer with a pirate accent."
print(prompt_memory(question, instructions))

# Chat with your clone in the terminal:
chat_with_clone()
```

## Key Features:

1. **Memory Storage**: Store memories, experiences, and information in a local vector database. Capture the essence of your persona and knowledge, creating a comprehensive data repository for Chat GPT to utilize.

2. **Self-Cloning Capability**: Enable Chat GPT to clone your personality and knowledge using the stored memories. Watch as Chat GPT adapts to your unique style, preferences, and expertise.

3. **Efficient Retrieval**: Experience fast memory retrieval through the vectorized storage system. Retrieve memories seamlessly for smooth and natural conversations with your cloned agent.

4. **User-Friendly Integration**: Simple and intuitive integration process for both developers and enthusiasts to incorporate ME_GPT into their Chat GPT projects.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/djm93dev/me_gpt.git
cd me_gpt
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Run the example script:
```bash
python examples/example.py
```

## Contributing

We welcome contributions! Please check out our [roadmap](https://github.com/djm93dev/me_gpt/blob/main/ROADMAP.md) for planned features and areas where you can help. Read our [contributing document](https://github.com/djm93dev/me_gpt/blob/main/.github/CONTRIBUTING.md) for more information.

We're currently seeking maintainers and community organizers to help build the community around this project. If you're interested in an official role, please email daniel@danielmcdonald.dev.