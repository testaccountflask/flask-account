from flask import Flask,request,jsonify, send_file
from flask_cors import CORS
import time
import os
import openai
class ChatApp:
    def __init__(self):
        # Setting the API key to use the OpenAI API
        openai.api_key = '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'
        self.messages = [
            {"role": "system", "content": "you are an effective HR executive capable of seeking specific actionable feedback from employees by asking them questions and asking follow-up questions when employee answers are too vague."},
            {"role": "assistant", "content": "Do you have any feedback to give"},
        {"role": "user", "content": "My teammates are holding me back from completing my deliverables"},
        {"role": "assistant", "content": "I am sorry to hear that, I will let the manager know about it. Could you please elaborate on the specific instances when your teammates held you back?"},
        {"role": "user", "content": "Sure, they are unavailable most of the time."},
        {"role": "assistant", "content": "Thank you so much for bringing this to our attention. This matter will be addressed at the earliest. Is there anything else you would like to add?"},
        {"role": "user", "content": "If you feel like the conversatin has ended,after saying the last message by thanking them for their time, then immediately send another message saying \"Chat Ended\""},
        {"role": "user", "content": "Now start a new conversation by asking them their name, ensure you get the name. Start taking their feedback next by asking them if they have any problem at work. Remember ask them one question at a time.Always the text starting text should be \"Hello, I am your HR assistant. I am here to help you with your feedback. Can you start by telling me your name?\""}
        ]

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        print(response['choices'][0]['message']['content'])
        return response['choices'][0]['message']['content']
    
    def Savereturn(self) :
      return self.messages
ch = ChatApp()
msg = " "
a = ch.chat(msg)
# print(a)
# while True :
#     msg = input('[User] ')
#     if msg.lower() == "quit" :
#           break
#     a = ch.chat(msg)
b = ch.Savereturn()
# print(*b[6::])

app = Flask(__name__)
# CORS(app, origin='http://localhost:3000/')
app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def get_answer():
    answer = request.json['answer']
    answer = answer.lower()
    return ch.chat(answer)

@app.route('/question', methods=['GET'])
def get_question():
    # if b[-1]['role'] == 'user':
    #     return jsonify("Loading.....")
    #     get_question()
    # else:
    return jsonify(b[-1]['content'])


    


