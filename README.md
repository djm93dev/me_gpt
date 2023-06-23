# ME_GPT

ME_GPT revolutionizes the way you interact with Chat GPT by introducing a powerful memory storage system and self-cloning functionality. With ME_GPT, you can store your cherished memories in a local vector database and leverage them to give Chat GPT the extraordinary ability to clone your unique personality and knowledge.

## Quickstart:

### 1. Pip install the library
```
pip install me-gpt
```

### 2. Create a new .env file
```
cp .env.example .env
```

### 3. Add your OpenAI API key to the .env file
```
OPEN_AI_API_KEY = "API_KEY"
```

**OpenAI API key**

Visit https://platform.openai.com/account/api-keys to get your OpenAI API key

### 4. Test the library
```python
from me_gpt.ai import *

# initial questions to help your clone get started:
initial_questions()

# have your clone ask you more questions:
more_questions(number_of_questions=3)

# ask your clone a question and any instructions you'd like to give:
question = "What is your Name?"
instructions = "Give your answer with a pirate accent."
print(prompt_memory(question, instructions))

# chat with your clone in the terminal:
chat_with_clone()
```

## Key Features:

1. Memory Storage: Store memories, experiences, and information in a local vector database with ease. Capture the essence of your persona and knowledge, creating a treasure trove of data for Chat GPT to tap into.

2. Self-Cloning Capability: Empower Chat GPT to clone your personality and knowledge using the memories stored in the vector database. Witness the remarkable transformation as Chat GPT adapts to your unique style, preferences, and expertise.

3. Efficient Retrieval: Experience blazing-fast memory retrieval thanks to the vectorized storage system. Retrieve memories seamlessly, ensuring smooth and uninterrupted conversations with your cloned agent.

4. User-Friendly Integration: The repository offers a simple and intuitive integration process, allowing developers and enthusiasts to effortlessly incorporate ME_GPT into their existing Chat GPT projects.

Whether you're looking to personalize your conversational AI interactions, create virtual replicas, or explore the potential of memory-enhanced language models, ME_GPT is your go-to solution. Unlock the power of memories and witness the fascinating capabilities of Chat GPT clones with this cutting-edge repository. Embark on a journey of unparalleled dialogue experiences and reshape the future of conversational AI.

## Contributing

If you want to contribute, please check out the [roadmap](https://github.com/djm93dev/me_gpt/blob/main/ROADMAP.md), in the GitHub repo. You are welcome to read the [contributing document](https://github.com/djm93dev/me_gpt/blob/main/.github/CONTRIBUTING.md) for more information.

We are currently looking for more maintainers and community organizers to help us build the community around this project. If you are interested, email - daniel@danielmcdonald.dev if you are interested in an official role.