In this repository, you can find an Arabic Irony corpus which is mentioned in [Irony Detection in a Multilingual Context](https://www.google.com) **ECIR-2020** paper.
The corpus consists of ~5.5k tweets annotated by two native Arabic speakers with appended with another randomly 5.5k sampled tweets from the original un-annotated corpus (`ECIR_training.csv` & `ECIR_test.csv`).

This corpus has been used also in **IDAT** shared task at FIRE-2019: [IDAT@FIRE2019: Overview of the Track on Irony Detection in Arabic Tweets](http://ceur-ws.org/Vol-2517/T4-1.pdf), but without adding the random 5.5k sample to ensure the quality of the data (`IDAT_training.csv` & `IDAT_test.csv`).


We distribute only the Ids of the annotated tweets due to [Twitter policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy). Thus, we share a python script to read the text of these tweets `read_tweets_text.py`.

REQUIREMENTS:
- tweepy
- pandas 
- tqdm

USAGE:
> python read_tweets_text.py file_name

example:
> python read_tweets_text.py ECIR_test.csv

Citations:

      @inproceedings{ghanem2019irony,
        title={Irony Detection in a Multilingual Context},
        author={Ghanem, Bilal and Karoui, Jihen and Benamara, Farah and Rosso, Paolo and Moriceau, V{\'e}ronique},
        booktitle={European Conference on Information Retrieval},
        year={2020},
        organization={Springer}
      }


    @inproceedings{ghanem2019idat,
      title={IDAT@FIRE2019: Overview of the Track on Irony Detection in Arabic Tweets},
      author={Ghanem, Bilal and Karoui, Jihen and Benamara, Farah and Moriceau, V{\'e}ronique and Rosso, Paolo},
      booktitle={Working Notes of the Forum for Information Retrieval Evaluation (FIRE 2019). CEUR Workshop Proceedings. In: CEUR-WS.org, Kolkata, India},
      volume = {2517},
      pages={380--390},
      year={2019}
    }


If you face any problem while downloading the tweets, and you need a copy of the full data, please fill the following form: 
[IDAT data](https://forms.gle/FsgZrbv5YfR5Jibx6)


For further information, feel free to contact the authors.
