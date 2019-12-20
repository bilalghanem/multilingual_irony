In this repository, you can find an Arabic Irony corpus which is mentioned in [Irony Detection in a Multilingual Context](https://www.google.com) **ECIR-2020** paper.
The corpus consists of ~5.5k tweets annotated by two native Arabic speakers with appended with another randomly 5.5k sampled tweets from the original un-annotated corpus (`ECIR_training.csv` & `ECIR_test.csv`).

This corpus has been used also in **IDAT** shared task at FIRE-2019: [IDAT@FIRE2019: Overview of the Track onIrony Detection in Arabic Tweets](http://irlab.daiict.ac.in/~Parth/T4-1.pdf), but without adding the random 5.5k sample to ensure the quality of the data (`IDAT_training.csv` & `IDAT_test.csv`).


We distribute only the Ids of the annotated tweets due to [Twitter policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy). Thus, we share a python script to read the text of these tweets `read_tweets_text.py`.

REQUIREMENTS:
- tweepy
- pandas 
- tqdm

USAGE:
> python read_tweets_text.py file_name
example:
> python read_tweets_text.py ECIR_test.csv


For further information, feel free to contact us.
