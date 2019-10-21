## hi bye
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## bye
* goodbye
    - utter_goodbye


## interactive_story_1
* greet{"user_name": "Raghvendra"}
    - slot{"user_name": "Raghvendra"}
    - utter_greet
* ask_what_can_bot_do
    - utter_what_can_bot_do
* ask_who_is_it
    - utter_who_is_it
* ask_how_bot_doing
    - utter_how_bot_doing
* user_mood_unhappy
    - utter_user_unhappy_response
    - utter_cheer_up
    - utter_did_that_help
* user_affirm
    - utter_helped

## interactive_story_2
* greet
    - utter_greet
* user_name{"user_name": "shruthi"}
    - slot{"user_name": "shruthi"}
    - utter_user_name_change
* user_thanks
    - utter_user_thanks_response
* ask_what_can_bot_do
    - utter_what_can_bot_do
* ask_time
    - action_tell_time
* user_got_to_go
    - utter_user_got_to_go_response
* goodbye
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* user_name{"user_name": "don"}
    - slot{"user_name": "don"}
    - utter_user_name_change
* tell_a_joke
    - utter_a_joke
* funny_bot
    - utter_funny_bot_response
* user_affirm
    - utter_user_affirm_response
* user_mood_happy
    - utter_user_happy_response
* marry_me
    - utter_marry_me_response
* ask_who_built_bot
    - utter_who_built_bot
* ask_bot_how_old
    - utter_bot_how_old
* bot_too_young
    - utter_too_young_response
* user_got_to_go
    - utter_user_got_to_go_response

## interactive_story_1
* greet{"user_name": "Bro"}
    - slot{"user_name": "Bro"}
    - utter_greet
* ask_what_can_bot_do
    - utter_what_can_bot_do
* tell_a_joke
    - utter_a_joke
* not_funny_bot
    - utter_not_funny_bot_response
* ask_who_built_bot
    - utter_who_built_bot
* ask_who_is_it
    - utter_who_is_it
* greet
    - utter_greet
* ask_bot_where_from
    - utter_ask_bot_where_from
* insult_bot
    - utter_insult_bot_response
* user_mood_unhappy
    - utter_user_unhappy_response
    - utter_cheer_up
    - utter_did_that_help
* user_deny
    - utter_didnt_help
* user_affirm
    - utter_user_affirm_response
* user_got_to_go
    - utter_user_got_to_go_response
* goodbye
    - utter_goodbye
