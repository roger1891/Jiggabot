import IPython
from IPython.display import clear_output, HTML, display
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

interpreter = RasaNLUInterpreter('models/default/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('models/dialogue', interpreter=interpreter)

def chatlogs_html(messages):
    messages_html = "".join(["<p>{}</p>".format(m) for m in messages])
    chatbot_html = """<div class="chat-window" {}</div>""".format(messages_html)
    return chatbot_html

"""
while True:
    clear_output()
    display(HTML(chatlogs_html(messages)))
    time.sleep(0.3)
    a = input()
    messages.append(a)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for r in responses:
        messages.append(r.get("text"))
 """      
print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    clear_output()
    time.sleep(0.3)
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for response in responses:
        #print(response["text"])
        print(response.get("text"))
 
from IPython.display import IFrame

agent = Agent.load('models/dialogue')
agent.visualize("stories.md", "story_graph.html", max_history=2)

IFrame(src="./story_graph.html", width=1000, height=800)