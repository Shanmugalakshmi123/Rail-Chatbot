import streamlit as st
import pandas as pd
import Levenshtein
def clean_data():
    df=pd.read_csv('Train_details_22122017.csv')
    df=df[df['Source Station Name'].notnull()]
    df2=df
    #df2['duration']=df[df['Arrival time']-df['Departure Time']]
    # for i in range(len(df)):
    #     df2['Distance'][i]=pd.(df2['Arrival time'][i])-pd.to_timedelta(df2['Departure Time'][i])
    # df2
    df2['Arrival time']=pd.to_datetime(df2['Arrival time'])
    df2['Departure Time']=pd.to_datetime(df2['Departure Time'])
    df2['duration']=df2['Departure Time']-df2['Arrival time']
    return df2
def string_similarity(s1, s2):
            distance = Levenshtein.distance(s1, s2)
            similarity = 1 - (distance / max(len(s1), len(s2)))
            return similarity * 100


st.title("Rail Chatbot")
c1, c2 = st.columns(2)
start=c1.text_input("Start", key="start")
end=c2.text_input("Destination", key="end")
st.button("Retrieve Train Details", key="retrieve")
df2=clean_data()
start=start.upper()
end=end.upper()
st.write("Train No","Train Name","Arrival","Departure","Duration")
for i,j in df2.iterrows():
    #print(1)
    x=string_similarity(j.iloc[9],start)
    y=string_similarity(j.iloc[11],end)
    #print(x,y)
    
    if x>50 and y>50:
        #print(x,y)
        st.write(j.iloc[0],j.iloc[1],j.iloc[5],j.iloc[6],j.iloc[12])