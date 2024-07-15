from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
def fetchstats(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    num_messages= df.shape[0]

    words = []
    for message in df['Message']:
        words.extend(message.split())
    num_media=df[df['Message']=='<Media omitted>'].shape[0]

    extractor=URLExtract()
    links=[]
    for message in df['Message']:
        links.extend(extractor.find_urls(message))

    return num_messages,len(words),num_media,len(links)


def most_busy_users(df):
    x = df['User'].value_counts().head()
    df = round((df['User'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Name', 'User': 'percent'})
    return x,df


def create_wordcloud(selected_user,df):

    f = open('Manglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]
    
    temp = df[~df['Message'].str.contains('<Media omitted>|null|deleted')]

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['Message'] = temp['Message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['Message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):

    f = open('Manglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    temp = df[~df['Message'].str.contains('<Media omitted>|null|deleted')]

    words = []

    for message in temp['Message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df




    
    
    
