#import required libraries and dependencies

#import os
#import json
#from web3 import Web3
#from pathlib import Path
#from dotenv import load_dotenv
import streamlit as st

# add title, description, and gif 

st.set_page_config(
    page_title="Cryptic Crusaders")

st.title("Cryptic Crusaders")
st.markdown("An NFT company specializing in providing unique and exclusive player icons and avatars, allowing you to stick out from the crowd whether you're gaming with friends, live streaming, or even gaming professionally. Look out for #whydoboring on social media to keep up to date with our latest offerings and promotions.")
st.image("https://media.giphy.com/media/gM5rskUNwmHJ1DCiAX/giphy.gif")

#ICO 

st.subheader("Join the Crusade - Intial Coin Offering Coming Soon")
colCoinText, colCoinImage = st.columns(2)

with colCoinText:
    st.markdown("Follow #jointhecrusade on social media to keep up to date on all the latest news on our ICO (initial coin offering). Avatars will be available for purchase with ETH (Ethereum) to start and will eventually be able to be purchased with or sold for ETH or CRC (Crusader Coin). Please see our gallery below for our initial launch of 3 exclusive avatars. Purchase now and join the future of gaming today!") 

with colCoinImage:
    st.image("Images/coin.jpg") 

#create and display avatar_database


avatar_database ={
    "Elna": ["Elna the Elven Warrior", .6, "Images/Icon_2.jpg"],
    "Talman": ["Talman the Tactical Turtle", .5, "Images/Icon_3.jpg"],
    "Ozhar": ["Ozhar the Observant Orc", .4, "Images/Icon_1.jpg"],
    
}

avatars=["Elna","Talman", "Ozhar"]

def get_avatars():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(avatar_database.values())

    for number in range(len(avatars)):
        st.image(db_list[number][2], width=200)
        st.subheader(db_list[number][0])
        st.write("Price (ETH): ", db_list[number][1])
        st.text(" \n")

st.header("Avatar Gallery")

get_avatars()


