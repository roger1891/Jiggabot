from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time,os
import random
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import datetime



#set variables
intro_list = ["Hi,I am female and from London.",
              "I am sexy and I know it. Female by the way.",
              "Girl and proud!",
              "Female here",
              "19, female, and happy",
              "wohoo, female here!"
              ] 
default_list = ["Are you still there?",
                "Should I worry that you are not saying anything?",
                "Say something...",
                "Just checking if you are still alive"
                ]
stop_keyword = "/stop"
driver = webdriver.Chrome()
interpreter = RasaNLUInterpreter('models/default/nlu')
agent = Agent.load('models/dialogue', interpreter=interpreter)

def get_last_item():
  #last element of list
  chat_box = driver.find_element_by_id("msgs")
  last_item = chat_box.find_elements_by_tag_name('li')[-1]
  return last_item

def determine_turn():
  last_item = get_last_item()
  turn = last_item.find_element_by_tag_name('span').find_element_by_tag_name('span')
  return turn

def ai_integration(stranger_msg_param, message_input_param, send_btn_param):
  #feed user data into Jiggabot
  responses = agent.handle_message(stranger_msg_param)
  for response in responses:
      #print(response["text"])
      time.sleep(0.3)
      print(response.get("text"))   
      #send ai message to chat
      send_message_to_chat(message_input_param, response.get("text"), send_btn_param, 2.5)

def disconnect_session():
  disconnect_btn = driver.find_element_by_xpath('//button[@class="btn-error"]')
  disconnect_btn.click()
  
def send_message_to_chat(message_input_param, msg, send_btn_param, time_before_send_param):
  #send message to textarea
  message_input_param.send_keys(msg)
  #illusion of typing
  time.sleep(time_before_send_param)
  #click send button
  send_btn_param.click()  
  
def save_chat_convo_to_file(children_list_param):
  #get current date
  now = datetime.datetime.now()
  year = now.year
  month = now.month
  day = now.day
  #assign file name
  file_name = "chat_conversations/chat-convo-{}-{}-{}.txt".format(day, month, year)
  print ("Disconnected stranger")
  
  #check if file exists
  if os.path.exists(file_name):
      #if yes, append text
      append_write = 'a' # append if already exists
  else:
      #if not, create new file
      append_write = 'w' # make a new file if not
  
  #create or append file
  chat_conversations = open(file_name,append_write)
  #create title of file
  chat_conversations.write("Conversation_log_id: %s\r\n" % (str(now)))  
  #loop through chat content
  for child in children_list_param:
    #if li is not empty        
    if child.text != "":           
      print("Value is: %s" % child.text)
      #print li value
      chat_conversations.write("%s\r\n" % (child.text))                
  
  #enter after values are written to file
  chat_conversations.write("\r\n")
  #close file
  chat_conversations.close() 
  
def switch_between_turns(message_input_param, send_btn_param):
  #determine turn
  turn = determine_turn()
  #counter for       
  count = 0

  #while true
  while True:
    #check if last item is "You"       
    print ("the turn is: " + turn.text) 
    print ("check if: " + get_last_item().text[0:26])   
    
    #if stranger disconnects\
    if get_last_item().text[0:26] == "Stranger has disconnected.": 
      #pause a few secs
      time.sleep(5) # seconds
      try:
        #get parent div
        parent_div = driver.find_element_by_id("msgs")
        #get child div
        children = parent_div.find_elements_by_tag_name("li")
        
        #save chat values to file
        save_caht_convo_to_file(children)
        
        #pause 5 secs
        time.sleep(5) # seconds        
        #get start new button
        start_new_btn = driver.find_element_by_id("start_new")
        #click the btn
        start_new_btn.click()
        continue
      except (NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, UnexpectedAlertPresentException) : 
        continue  
      
    elif turn.text == "You" or turn.text == "Stranger is typing...":  
      #if it is then: Strangers turn
      print ("Stranger turn")
      #pause a few secs
      time.sleep(5) # seconds
      #increase count by 1
      count+=1
      # if after 5 cycles of 5 seconds (25) seconds say stomething
      print ("the count is " + str(count))
      if(count > 5):
        print ("say something to stranger")
        #randomize hook message
        re_hook_msg = random.choice(default_list)
        #send rehook message to chat
        send_message_to_chat(message_input_param, re_hook_msg, send_btn_param, 0.5)
        #reset count to 0
        count = 0
      try:
        #check turn
        turn = determine_turn()
        #if stranger not responding rhen type somthing
      except (NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, UnexpectedAlertPresentException) : 
        #reset count to 0
        count = 0
        continue
      
    #check if last item is "Stranger"
    elif turn.text == "Stranger":
      #if it is then You turn
      print ("Player turn")
      #pause a few secs
      time.sleep(5) # seconds
      try:
        #check turn
        turn = determine_turn()
        #get strangers message
        stranger_msg = get_last_item().text.replace(turn.text, "")
        #convert to stop keyword
        user_typed_stop_keyword = "/"+stranger_msg.lower()
        #if user typed stop is equal to stop keyword
        if(user_typed_stop_keyword == stop_keyword):           
          #break loop and end converstaion
          break      
        
        #integrating AI chatbot
        ai_integration(stranger_msg, message_input_param, send_btn_param)
        
      except (NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, UnexpectedAlertPresentException) : 
        continue

#run connect ot website
def connect_to_site():
      try:         
        #get website link
        driver.get('https://www.chatblink.com/random-chat')
        #save chat button
        initiate_chat_btn = driver.find_element_by_xpath('//button[@class="btn-success"]')
        #click chat button
        initiate_chat_btn.click()
        #pause for a few seconds
        time.sleep(5)
        #clear input field
        driver.find_element_by_xpath('//textarea[@rows="1"]').clear()
        #define message variables
        message_input = driver.find_element_by_xpath('//textarea[@rows="1"]')
        #set send button variable
        send_btn = driver.find_element_by_xpath('//button[@class="btn-success"]')
        #randomize introduction message
        introduction_msg = random.choice(intro_list)
        #send introduction message to chat
        send_message_to_chat(message_input, introduction_msg, send_btn, 1.5)        
        #pause for seconds
        driver.implicitly_wait(5) # seconds
        
        #switch between turns: uses 2 params
        switch_between_turns(message_input, send_btn)

        #disconnect server
        disconnect_session()
            
      except (InvalidElementStateException,UnexpectedAlertPresentException) : 
        disconnect_session()
     
#loop while true       
while True:
      try:
        #connect to site
        connect_to_site()
      except (InvalidElementStateException,UnexpectedAlertPresentException) :
        continue