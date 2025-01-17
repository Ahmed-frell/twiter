import streamlit as st
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
st.set_page_config(page_title="souravs_sentiment_analysis_app")
def cal(searchTerm,noOfSearchTerms):
    def percentage(part,whole):
        return 100*float(part)/float(whole)
    consumerKey = "VdoHWrzpfrT8aEfDd4GcPjy3I"
    noOfSearchTerms = int(noOfSearchTerms)
    consumerSecret = "yMF15IIKQiT3y0u4tO0kxIMJfpKcINOhXg1WsxjRumJs4Dnt6h"
    accessToken = "1297879475900702720-aMY7lZHhFqWbJ6lpDNtjHxRPJ5peKx"
    accessTokenSecret = "GtwlHb6QuHrxxsB6P6ViqzKE9KWaNL7U0uGzWpxGJaTvs"
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    #noOfSearchTerms=10
    #searchTerm = input("Enter keyword/Hashtag to search About : ")
   # noOfSearchTerms = int(input("Enter how many tweets to analyse : "))
    tweets = tweepy.Cursor(api.search).items(noOfSearchTerms)
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    for tweet in tweets:
        # print(tweet.text)
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity
        if(analysis.sentiment.polarity == 0):
            neutral += 1
        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
        elif (analysis.sentiment.polarity > 0.00):
            positive += 1
    positive = percentage(positive,noOfSearchTerms)
    negative = percentage(negative,noOfSearchTerms)
    neutral = percentage(neutral,noOfSearchTerms)
    polarity = percentage(polarity,noOfSearchTerms)
    positive = format(positive,'.2f')
    negative = format(negative,'.2f')
    neutral = format(neutral,'.2f')
    print("how pepole are reacting on " + searchTerm +" after analysing " + str(noOfSearchTerms) + " tweets.")
    if(polarity == 0):
        print("Neutral")
    elif(polarity < 0.00):
        print("Negative")
    elif(polarity > 0.00):
        print("positive")

    labels = ['Positive ['+str(positive)+'%]','Negative ['+str(negative)+'%]','Neutral ['+str(neutral)+'%]']
    size = [positive, negative , neutral]
    label = ['positive','negative','neutral']
    colors = ['green', 'red', 'orange']
    wp = {'linewidth': 1, 'edgecolor': "black"}
    patches, texts = plt.subplots()
    texts.pie(size, colors=colors, startangle=90,shadow=True,labels=labels,wedgeprops=wp)
    #plt.legend(patches, labels)
    plt.title('how pepole are reacting on ' + searchTerm + ' after analysing ' + str(noOfSearchTerms) + ' tweets.')
    plt.axis('equal')
    plt.gcf().canvas.set_window_title('sentiment analysis by souravsing')
    plt.tight_layout()
    plt.show()
    st.pyplot(patches)
    return polarity  
def main():
    #st.write("Author:Souravsing S. Pardeshi") 
    st.title("Twitter Sentiment Analysis APP")
    st.markdown("@souravsing ")
    st.image("img/demo.gif")
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    local_css("style.css")
    dataset_name = st.sidebar.selectbox("Select which results you want to see :",("All","Positive","Negative"))
    #st.write(dataset_name)
    searchTerm = st.sidebar.text_input("Enter hashtag or string to be searched : ","")
    noOfSearchTerms = st.sidebar.text_input("Choose Number of Tweets to Analyse:")
    result=""
    if st.sidebar.button("Predict"):
        result=cal(searchTerm,noOfSearchTerms)
        st.balloons()
        st.success("Result is : {}".format(result))
        st.write("Press About Button to know more")
    if st.sidebar.button("About me"):
        st.balloons()
        st.header("This app is created by Souravsing S. Pardeshi")
        st.write("follow me on github: https://github.com/souravsingpardeshi",":sunglasses:")
    st.text("This project is created by souravsing with 🖤")
    #st.pyplot()
if __name__=='__main__':main()
