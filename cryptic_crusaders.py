#import required libraries and dependencies

#import os
#import json
#from web3 import Web3
#from pathlib import Path
#from dotenv import load_dotenv
import streamlit as st

# add title

st.set_page_config(
    page_title="Cryptic Crusaders")

st.title("Cryptic Crusaders")
st.markdown("An NFT company specializing in providing unique and exclusive player icons and avatars, allowing you to stick out from the crowd whether you're gaming with friends, live streaming, or even gaming professionally. Look out for #whydoboring on social media to keep up to date with our latest offerings and promotions.")
st.image("https://media.giphy.com/media/gM5rskUNwmHJ1DCiAX/giphy.gif")

#ICO 

st.subheader("Intial Coin Offering")
colCoinText, colCoinImage = st.columns(2)

with colCoinText:
    st.markdown("Check out our ICO and get your CrusaderCoin (CRC) today! CRC will initially be offered at a price of $100 USD per coin and will be used for all your customization needs buy now and join gaming of the future today! For a listing of player icons currently available please see gallery below.") 

with colCoinImage:
    st.image("Images/coin.jpg") 
#add player gallery section
st.subheader("Gallery")

st.image("Images/Icon_1.jpg", width=200)
st.image("Images/Icon_2.jpg", width=200)
st.image("Images/Icon_3.jpg", width=200)

