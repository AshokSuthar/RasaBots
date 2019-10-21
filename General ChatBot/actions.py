# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []


from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from urllib.request import urlopen
from urllib.parse import urlencode
import json
import datetime
import spacy

class TellTime:
   def time(self):
      return datetime.datetime.now()


class ActionTellTime(Action):
   def name(self):
      return "action_tell_time"

   def run(self, dispatcher, tracker, domain):
      print("TELLING TIME")
      tell_time = TellTime()
      result = tell_time.time()
      if result:
         dispatcher.utter_message(result.strftime("Today is %d %b, %Y and The time is %H:%M:%S"))
      return []

# class ExtractName:
#    def tellName(self, text):
#       arr = text.split()
#       arr[len(arr)-1] = arr[len(arr)-1].capitalize()
#       text = " ".join(arr)
#       nlp = spacy.load('en_core_web_md', disable=['parser', 'tagger', 'textcat'])
#       sents = nlp(text)
#       print(text)
#       people = [name.text for name in sents.ents if name.label_ in ['PERSON', 'ORG', 'GPE' ]]
#       name = None
#       if len(people) > 0:
#          name = people[0]
#       return name


# class ActionExtractUserName(Action):
#    def name(self):
#       return "action_get_user_name"
#
#    def run(self, dispatcher, tracker, domain):
#       print("Extracting User Name")
#       if tracker.get_slot("user_name") != 'human':
#          print("User name already set, returning")
#          return []
#       else:
#          print("User name not set, using spacy to extract...")
#          extract_name = ExtractName()
#          message = (tracker.latest_message)['text']
#          user_name = extract_name.tellName(message)
#          if user_name:
#             dispatcher.utter_message("Ok I will call you "+str(user_name)+" from now on.")
#             return [SlotSet("user_name", user_name)]
#          else:
#             dispatcher.utter_message("Sorry I couldn't get your name")
#             return []
