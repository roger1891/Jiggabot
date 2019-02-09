import datetime
import time,os

now = datetime.datetime.now()
year = now.year
month = now.month

file_name = "chat_conversations/chat-convo-{}-{}.txt".format(year, month)


chat_conversations_write = open(file_name,"w+")
chat_conversations_append = open(file_name,"a+")



#if file exisets
#if it doesn't exist
if(os.path.isfile(file_name)):
  for i in range(10):
    chat_conversations_append.write("%s\r\n" % ("child"))   
else:
  for i in range(10):       
    chat_conversations_write.write("%s\r\n" % ("child 1"))         


#close file
chat_conversations_write.close() 
chat_conversations_append.close()