# Neutral Portuguese
Changes people's pronouns to gender neutral elu/delu.

Trained a custom spacy model with Prodigy tool to identify gendered words directed at people based on [a Kaggle dataset of tweets in Brazilian Portuguese](https://www.kaggle.com/rafaelperes/ner-in-brazilian-portuguese-tweets) and [webhose.io dataset of articles from the top news sites in Portuguese](https://webhose.io/free-datasets/portuguese-news-articles/). After picking the words, the translation was made based on a set of rules and an exception database.

Hosted in my [PythonAnywhere](fernandesafp.pythonanywhere.com) page with FlaskAPI.
