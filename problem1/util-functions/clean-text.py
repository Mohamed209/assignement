import pandas as pd
import re

# read tweets
dfraw = pd.read_csv('../dataset/raw/Tweets.csv')
# drop unwanted columns
dfraw.drop(columns=['tweet_id', 'name', 'tweet_coord',
                    'tweet_created', 'tweet_location',
                    'user_timezone'],
           axis=1, inplace=True)

for i in range(len(dfraw['text'])):
    #remove tweet account name
    dfraw['text'][i] = re.sub(r'@\w+', '', dfraw['text'][i])
    #remove website urls
    dfraw['text'][i]=re.sub(r'http\S+', '', dfraw['text'][i],flags=re.MULTILINE)
    #remove special characters
    dfraw['text'][i] = re.sub(r'[^A-Za-z0-9]+', ' ', dfraw['text'][i])
    #remove any white space
    dfraw['text'][i]=re.sub(r'\s+', ' ', dfraw['text'][i], flags=re.I)
    #convert into lower case
    dfraw['text'][i]=dfraw['text'][i].lower()
dfraw.to_csv(r'../dataset/processed/clean-text.csv')
print("File Saved")
