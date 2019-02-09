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
introduction_msg = random.choice(intro_list)
re_hook_msg = random.choice(default_list)
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
  
def switch_between_turns(message_input_param, send_btn_param):
  #determine turn
  turn = determine_turn()
  #counter for       
  count = 0

  #while true
  while True:
    #check if last item is "You"                  
    if turn.text == "You":  
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
      
    #if stranger disconnects
    elif turn.text == "Stranger has disconnected.":           
      try:
        chat_box = driver.find_element_by_id("msgs")
        #pause 5 secs
        time.sleep(5) # seconds
        #get  start new button
        start_new_btn = driver.find_element_by_id("start_new")
        #click the btn
        start_new_btn.click()
        print("Sranger is typing") 
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