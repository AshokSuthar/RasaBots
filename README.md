# RasaBots
Contains Random test bots built while learning and working with Rasa

## Steps to Run
### rasa train: 
Trains a model using your NLU data and stories, saves trained model in ./models.
### rasa run
Starts a server with your trained model.
### rasa run actions
Starts an action server using the Rasa SDK.
### rasa x
Launches Rasa X in local mode.


# cmi-content-processor
### required donwloadables
$ python -m spacy download en_core_web_sm
$ python
>>> import nltk
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('stopwords')
### Changes to make
change path 'CMIContentProcessor/search/Data/SO_vectors_200.bin' accordingly in the program 'doc_search.py'.

### Running the Program in command Prompt
"Expects <python> <doc_search.py> <file_to_index.csv> [<file_to_index.csv>...]"

### cleanXMLBlog.py
Extracts the data from 'blog.WordPress.2019-08-07' XML Dump file, cleans it and creates a csv format file.

### General ChatBot ###
Is the current bot I am working on. I am trying to learn how to handle small talks/chitchats by building this bot.

