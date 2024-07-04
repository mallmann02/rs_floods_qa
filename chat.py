import ollama
import time

from prompt import PROMPT
from retriever import Retriever

class LLM_RAG:
    def __init__(self):
        self.retriever = Retriever()
        self.prompt = PROMPT

    def chat(self, user_question):
        info = self.retriever.retrieve_info(user_question)
        formatted_prompt = self.prompt.format(user_question=user_question, info=info)

        message = [
            {
                "role": "user",
                "content": formatted_prompt
            }
        ]

        response = ollama.chat(model='llama3', messages=message, stream=True)
        for message in response:
            print(message['message']['content'], end='', flush=True)
        
    def run(self):
        self.print_name()
        is_day = time.localtime().tm_hour >= 6 and time.localtime().tm_hour < 18
        if is_day:
            print("Bom dia! Sou RAGAL, um assistente virtual especializado nas cheias do Rio Grande do Sul. Como posso te ajudar?\n\n")
        else:
            print("Bom Noite! Sou RAGAL, um assistente virtual especializado nas cheias do Rio Grande do Sul. Como posso te ajudar?\n\n")

        while True:
            user_question = input(">>> ")

            print('\n')
            if user_question == "sair":
                print("Até mais!")
                break

            self.chat(user_question)

    def print_name(self):
        print("""

            ┳┓┏┓┏┓┏┓┓ 
            ┣┫┣┫┃┓┣┫┃ 
            ┛┗┛┗┗┛┛┗┗┛
            """, end='\n\n')

chat = LLM_RAG()
chat.run()