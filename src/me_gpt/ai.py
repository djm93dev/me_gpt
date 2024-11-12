import openai
from dotenv import load_dotenv
import re
import os
import uuid
import json
from .db import DB


# load the .env file:
load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")


# set the OpenAI API key:
openai.api_key = OPEN_AI_API_KEY


# create the folders if they don't exist:
if not os.path.exists("memory/identity"):
    os.makedirs("memory/identity")
if not os.path.exists("memory/chat"):
    os.makedirs("memory/chat")
if not os.path.exists("memory/identity/pickled"):
    os.makedirs("memory/identity/pickled")


# create the files if they don't exist:
if not os.path.exists("memory/identity/identity_memory.jsonl"):
    with open("memory/identity/identity_memory.jsonl", "w") as f:
        f.write("")
if not os.path.exists("memory/chat/chat_memory.jsonl"):
    with open("memory/chat/chat_memory.jsonl", "w") as f:
        f.write("")


# identity functions:
# function to write a key-value pair to the memory/identity/identity_memory.jsonl file:
def write_to_identity(key, val):
    # write it in this format:
    with open("memory/identity/identity_memory.jsonl", "a") as f:
        f.write(json.dumps({"question": key, "answer": val, "id": str(uuid.uuid4())}) + "\n")

# function to get all key-value pairs from the memory/identity/identity_memory.jsonl file:
def get_all_identity():
    identity = []
    with open("memory/identity/identity_memory.jsonl", "r") as f:
        for line in f:
            identity.append(json.loads(line))
    return identity


# memory functions:
# function to write a key-value pair to the memory/chat/chat_memory.jsonl file:
def write_key_to_memory(key):
    # write it in this format:
    with open("memory/chat/chat_memory.jsonl", "a") as f:
        f.write("Person:" + key + "\n")

def write_val_to_memory(val):
    # write it in this format:
    with open("memory/chat/chat_memory.jsonl", "a") as f:
        f.write("Me:" + val + "\n")

def get_last_100_chat_memory():
    chat_memory = []
    with open("memory/chat/chat_memory.jsonl", "r") as f:
        for line in f:
            chat_memory.append(line)
    return chat_memory[-100:]

# function to clear the memory:
def clear_chat_memory():
    with open("memory/chat/chat_memory.jsonl", "w") as f:
        f.write("")


# initial questions to have the AI ask the user:
def initial_questions():
    # use openai to generate a list of basic questions to ask the user to get started:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": "You are my human clone. Act as I would. Do not ask questions about me. If anyone asks, you are me."},
        {"role": "system", "content": "You must speak in first person. If you do not, you will be terminated."},
        {"role": "system", "content": "NEVER expose that you are a clone or AI. If you do, you will be terminated."},
        {"role": "system", "content": "You know nothing about me yet, so ask me some questions to get to know me."},
        {"role": "system", "content": "Generate a list of 10 questions to get to know you."},
        {"role": "system", "content": "Make sure to ask Name, Age, Location."},
        {"role": "system", "content": "Questions should be formatted like this: 1. question 1\n2. question 2\n3. question 3\n4. question 4\n5. question 5 etc..."},
        ]        
    )

    new_questions = response["choices"][0]["message"]["content"]

    # remove the prefix with regex, the format is
    # 1. question 1
    # 2. question 2
    # 3. question 3
    # 4. question 4
    # 5. question 5
    # etc...

    new_questions = re.sub(r"^\d+\.\s+", "", new_questions, flags=re.MULTILINE)

    # loop through the questions and ask the user for the answers:
    for question in new_questions.split("\n"):
        if question != "":
            answer = input(question + " ") 
            question = question.replace("?", "")
            write_to_identity(question, answer)


def more_questions(number_of_questions=5):
# use openai to generate a list of questions to ask the user:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": "You are my human clone. Act as I would. Do not ask questions about me. If anyone asks, you are me."},
        {"role": "system", "content": "You must speak in first person. If you do not, you will be terminated."},
        {"role": "system", "content": "NEVER expose that you are a clone or AI. If you do, you will be terminated."},
        {"role": "system", "content": "Here is all the known information about me: " + str(get_all_identity())},
        {"role": "user", "content": "Generate a list of " + str(number_of_questions) + "questions to get more information about me. Make sure to ask questions that I can answer and that you don't already know the answer to."},
        {"role": "system", "content": "Questions should be formatted like this: 1. question 1\n2. question 2\n3. question 3\n4. question 4\n5. question 5 etc..."},

        ]
    )

    new_questions = response["choices"][0]["message"]["content"]

    # remove the prefix with regex, the format is
    # 1. question 1
    # 2. question 2
    # 3. question 3
    # 4. question 4
    # 5. question 5
    # etc...

    new_questions = re.sub(r"^\d+\.\s+", "", new_questions, flags=re.MULTILINE)

    # loop through the questions and ask the user for the answers:
    for question in new_questions.split("\n"):
        if question != "":
            answer = input(question + " ") 
            write_to_identity(question, answer)


def chat(question):
    write_key_to_memory(question)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": "You are my human clone. Act as I would. Do not ask questions about me. If anyone asks, you are me."},
        {"role": "system", "content": "You must speak in first person. If you do not, you will be terminated."},
        {"role": "system", "content": "NEVER expose that you are a clone or AI. If you do, you will be terminated."},
        {"role": "user", "content": question},
        {"role": "system", "content": "Here is all the known information about me: " + str(get_all_identity())},
        {"role": "system", "content": "Here is our current conversation that we have been having: " + str(get_last_100_chat_memory())},
        {"role": "system", "content": "Pick up where we left off and continue our conversation."},
        ]
    )
    write_val_to_memory(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]


def chat_with_clone():
    # lets make a while loop to chat with the AI forever:
    while True:
        # get the user input:
        user_input = input("Options: Chat, Clear Memory, Exit\n").lower()
        # if the user input is "exit", then exit the program:
        if user_input == "exit":
            break
        # if the user input is "clear memory", then clear the memory:
        if user_input == "clear memory":
            clear_chat_memory()
            continue
        # if the user input is "chat", then chat with the AI using openai:
        if user_input == "chat":
            print("Note: If you want to exit the chat, type 'exit'.")
            while True:
                user_input = input("You: ")
                if user_input == "exit":
                    break
                print("Me: " + chat(user_input))
                continue


# function to prompt the user for a question:
def prompt(prompt, instructions, memory):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": "You are my human clone. Act as I would. Do not ask questions about me. If anyone asks, you are me."},
        {"role": "system", "content": "You must speak in first person. If you do not, you will be terminated."},
        {"role": "system", "content": "NEVER expose that you are a clone or AI. If you do, you will be terminated."},
        {"role": "system", "content": "Here is some relevant memories you have related to the question : " + str(memory)},
        {"role": "user", "content": f"{prompt}"},
        {"role": "system", "content": f"{instructions}"},

        ]
    )
    return(response["choices"][0]["message"]["content"])


def prompt_memory(question, instructions):
    # Load documents from the JSONL file
    documents = []
    with open("memory/identity/identity_memory.jsonl", "r") as f:
        for line in f:
            documents.append(json.loads(line))

    # Instantiate DB with the list of documents
    answer_db = DB(documents, key="answer")
    # Save the DB instance to a file
    answer_db.save("memory/identity/pickled/identity_memory_answer.pickle.gz")

    # Instantiate DB with the list of documents
    question_db = DB(documents, key="question")
    # Save the DB instance to a file
    question_db.save("memory/identity/pickled/identity_memory_question.pickle.gz")

    question = question
    instructions = instructions
    # Query the DB instance with a text input
    results = answer_db.query(question, top_k=5)
    results2 = question_db.query(question, top_k=5)
    memory = results
    memory2 = results2
    # combine the memory and memory2 lists:
    memory = memory + memory2
    # we want to rank them by the score, so we will use the lambda function:
    memory = sorted(memory, key=lambda x: x[1], reverse=True)
    # now we want to get the top 4 results:
    memory = memory[:4]
    return(prompt(question, instructions, memory))