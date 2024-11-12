from me_gpt import *

# initial questions to help your clone get started:
initial_questions()

# have your clone ask you more questions:
more_questions(number_of_questions=3)

# ask your clone a question:
question = "What is your job?"
instructions = "Give your answer with a pirate accent."
print(prompt_memory(question, instructions))

# chat with your clone in the terminal:
chat_with_clone()
