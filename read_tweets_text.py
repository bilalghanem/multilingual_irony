import sys, tweepy
import pandas as pd
from tqdm import tqdm


CONSUMER_KEY = "<consumer key>"
CONSUMER_SECRET = "<consumer secret>"
OAUTH_TOKEN = "<application key>"
OAUTH_TOKEN_SECRET = "<application secret"

def read_tweets(list_of_id):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tweepy.API(auth)

    texts = []
    for id in tqdm(list_of_id, desc='Reading tweets'):
        id = int(id.replace("'", ''))
        try:
            tweet = api.get_status(id)
            texts.append(tweet._json['text'])
        except:
            print('Tweet id {} doesn\'t exits. Filled with \'empty_tweet\' token.'.format(id))
            texts.append('empty_tweet')
    return texts

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        print('Error: Please enter the csv file name.')
        exit(1)

    data = pd.read_csv(file_name, header=0, encoding='utf-8')
    data['text'] = read_tweets(data['tweet_id'])
    data.to_csv('with_text_'+file_name, header=True, index=False, encoding='utf-8')
    print('Saved!')