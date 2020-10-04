# Neutral Portuguese
Translates to gender neutral language and changes people's pronouns to the elu/delu system.

Trained a custom spacy model with Prodigy tool to identify gendered words directed at people based on a [Kaggle dataset](https://www.kaggle.com/rafaelperes/ner-in-brazilian-portuguese-tweets) of tweets in Brazilian Portuguese and a [webhose.io dataset](https://webhose.io/free-datasets/portuguese-news-articles/) of articles from the top news sites in Portuguese. After picking the words, the translation was made based on a set of rules and an exception database.

Hosted in my [PythonAnywhere](fernandesafp.pythonanywhere.com) page with FlaskAPI.
