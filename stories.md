## Generated Story -2753607020895660283
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* user_name_prompt_reply{"name": "John"}
    - slot{"name": "John"}
    - utter_positive_user_name_response
    - utter_want_to_know_my_name
* user_asks_bot_name_positive
    - utter_positive_my_name_response
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* user_is_clueless
    - utter_joke1_answ
    - utter_joke2_quest
* user_is_clueless
    - utter_joke2_answ
    - utter_joke3_quest
* user_is_clueless
    - utter_joke3_answ
    - utter_joke4_quest
* user_is_clueless
    - utter_joke4_answ
    - utter_joke5_quest
* user_is_clueless
    - utter_joke5_answ
    - utter_joke6_quest
* user_is_clueless
    - utter_joke6_answ
    - utter_joke7_quest
* user_is_clueless
    - utter_joke7_answ
    - utter_joke8_quest
* user_is_clueless
    - utter_joke8_answ
    - utter_joke9_quest
* user_is_clueless
    - utter_joke9_answ
    - utter_joke10_quest
* user_is_clueless
    - utter_joke10_answ
    - utter_joke11_quest
* user_is_clueless
    - utter_joke11_answ
    - utter_user_joke
* user_joke
    - utter_end_conversation
    - utter_goodbye

# compliment
* compliment
    - utter_compliment

# greet plus determine gender
* greet
    - utter_greet
* asks_gender
    - utter_i_am_female
  
# determine gender
* asks_gender
    - utter_i_am_female
  
# question whether real
* are_you_real
    - utter_i_am_real  
    
# not focused
* not_focused
    - utter_redirect_conversation   
    - utter_joke_prompt
    
# profession
* what_do_you_do
     - utter_what_i_do     
  
# greet plus location
* greet
    - utter_greet  
* where_u_from
    - utter_location
    
# determine location 
* where_u_from
    - utter_location    
    
# determine age
* whats_your_age
    - utter_age
    
# greet plus age
* greet
    - utter_greet  
* whats_your_age
    - utter_age   
     
  
## joke path compliant user wrong answers
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* user_name_prompt_reply
    - utter_positive_user_name_response
    - utter_want_to_know_my_name
* user_asks_bot_name_positive
    - utter_positive_my_name_response
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* user_is_clueless
    - utter_joke1_answ
    - utter_joke2_quest
* user_is_clueless
    - utter_joke2_answ
    - utter_joke3_quest
* user_is_clueless
    - utter_joke3_answ
    - utter_joke4_quest
* user_is_clueless
    - utter_joke4_answ
    - utter_joke5_quest
* user_is_clueless
    - utter_joke5_answ
  - utter_joke6_quest
* user_is_clueless
    - utter_joke6_answ
    - utter_joke7_quest
* user_is_clueless
    - utter_joke7_answ
    - utter_joke8_quest
* user_is_clueless
    - utter_joke8_answ
    - utter_joke9_quest
* user_is_clueless
    - utter_joke9_answ
    - utter_joke10_quest
* user_is_clueless
    - utter_joke10_answ
    - utter_joke11_quest
* user_is_clueless
    - utter_joke11_answ
    - utter_user_joke
* user_joke
    - utter_end_conversation
    - utter_goodbye
  
## joke path compliant user right answers
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* user_name_prompt_reply
    - utter_positive_user_name_response
    - utter_want_to_know_my_name
* user_asks_bot_name_positive
    - utter_positive_my_name_response
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* joke1_answ
    - utter_you_are_correct
    - utter_joke2_quest
* joke2_answ
    - utter_you_are_correct
    - utter_joke3_quest
* joke3_answ
    - utter_you_are_correct
    - utter_joke4_quest
* joke4_answ
    - utter_you_are_correct
    - utter_joke5_quest
* joke5_answ
    - utter_you_are_correct
    - utter_joke6_quest
* joke6_answ
    - utter_you_are_correct
    - utter_joke7_quest
* joke7_answ
    - utter_you_are_correct
    - utter_joke8_quest
* joke8_answ
    - utter_you_are_correct
    - utter_joke9_quest
* joke9_answ
    - utter_you_are_correct
    - utter_joke10_quest
* joke10_answ
    - utter_you_are_correct
    - utter_joke11_quest
* joke11_answ
    - utter_you_are_correct
    - utter_user_joke
* user_joke
    - utter_end_conversation
    - utter_goodbye  
  
## joke path compliant user wrong answers and doesn't understand
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* user_name_prompt_reply
    - utter_positive_user_name_response
    - utter_want_to_know_my_name
* user_asks_bot_name_positive
    - utter_positive_my_name_response
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* user_is_clueless
    - utter_joke1_answ
* user_dont_understand
    - utter_user_dont_understand
    - utter_joke2_quest
* user_is_clueless
    - utter_joke2_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke3_quest
* user_is_clueless
    - utter_joke3_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke4_quest
* user_is_clueless
    - utter_joke4_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke5_quest
* user_is_clueless
    - utter_joke5_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke6_quest
* user_is_clueless
    - utter_joke6_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke7_quest
* user_is_clueless
    - utter_joke7_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke8_quest
* user_is_clueless
    - utter_joke8_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke9_quest
* user_is_clueless
    - utter_joke9_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke10_quest
* user_is_clueless
    - utter_joke10_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_joke11_quest
* user_is_clueless
    - utter_joke11_answ
* user_dont_understand
    - utter_user_dont_understand  
    - utter_user_joke
* user_joke
    - utter_end_conversation
    - utter_goodbye  
 
## joke path non compliant intro user wrong answers 1
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* mood_deny
    - utter_negative_user_name_response
    - utter_want_to_know_my_name
* mood_deny
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* user_is_clueless
    - utter_joke1_answ
    - utter_joke2_quest
* user_is_clueless
    - utter_joke2_answ
    - utter_joke3_quest
* user_is_clueless
    - utter_joke3_answ
    - utter_joke4_quest
* user_is_clueless
    - utter_joke4_answ
    - utter_joke5_quest
* user_is_clueless
    - utter_joke5_answ
    - utter_joke6_quest
* user_is_clueless
    - utter_joke6_answ
    - utter_joke7_quest
* user_is_clueless
    - utter_joke7_answ
    - utter_joke8_quest
* user_is_clueless
    - utter_joke8_answ
    - utter_joke9_quest
* user_is_clueless
    - utter_joke9_answ
    - utter_joke10_quest
* user_is_clueless
    - utter_joke10_answ
    - utter_joke11_quest
* user_is_clueless
    - utter_joke11_answ
    - utter_user_joke
* user_joke
    - utter_end_conversation
    - utter_goodbye 
 
## joke path non compliant intro user wrong answers 2
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* mood_deny
    - utter_negative_user_name_response
    - utter_want_to_know_my_name
* mood_deny
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* mood_deny
    - utter_goodbye
 
## bad words path
* user_says_bad_word
    - utter_bad_word
* user_says_bad_word
    - utter_bad_word
    - utter_leave_prompt
* user_says_bad_word
    - utter_goodbye

## say goodbye
* goodbye
    - utter_goodbye
  
## doesn't want jokes
* negative_joke_reply
    - utter_goodbye

## Generated Story 260849555570653091
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* user_name_prompt_reply{"name": "James"}
    - slot{"name": "James"}
    - utter_positive_user_name_response
    - utter_want_to_know_my_name
* user_asks_bot_name_positive
    - utter_positive_my_name_response
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* user_is_clueless
    - utter_joke1_answ
    - utter_joke2_quest
* user_is_clueless
    - utter_joke2_answ
    - utter_joke3_quest
* joke3_answ
    - utter_you_are_correct
    - utter_joke4_quest
* user_is_clueless
    - utter_joke4_answ
    - utter_joke5_quest
* user_is_clueless
    - utter_joke5_answ
    - utter_joke6_quest
* user_is_clueless
    - utter_joke6_answ
    - utter_joke7_quest
* user_is_clueless
    - utter_joke7_answ
    - utter_joke8_quest
* user_is_clueless
    - utter_joke8_answ
    - utter_joke9_quest
* user_is_clueless
    - utter_joke9_answ
    - utter_joke10_quest
* user_is_clueless
    - utter_joke10_answ
    - utter_joke11_quest
* user_is_clueless
    - utter_joke11_answ
    - utter_user_joke
* user_joke
    - utter_end_conversation
    - utter_goodbye

## Generated Story 5700898822704264022
* greet
    - utter_greet
* mood_great
    - utter_user_name_prompt
* user_name_prompt_reply{"name": "Roger"}
    - slot{"name": "Roger"}
    - utter_positive_user_name_response
    - utter_want_to_know_my_name
* mood_deny
    - utter_joke_prompt
* positive_joke_reply
    - utter_positive_joke_prompt
    - utter_joke1_quest
* joke1_answ
    - utter_you_are_correct
    - utter_joke2_quest
* user_is_clueless
    - utter_joke2_answ
    - utter_joke3_quest
* joke3_answ
    - utter_you_are_correct
    - utter_joke4_quest
* user_is_clueless
    - utter_joke4_answ

