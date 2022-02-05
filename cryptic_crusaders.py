#import required libraries and dependencies

import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# add title

st.set_page_config(
    page_title="Cryptic Crusaders")

st.title("Cryptic Crusaders")
st.markdown("An NFT company specializing in provding unique and exclusive player icons and avatars, allowing you to stick out from the crowd whether you're gaming with frineds, live streaming, or even gaming professionally. Look out for #whydoboring on social media to keep up to date with our offering and promotions.")
st.image("https://media.giphy.com/media/gM5rskUNwmHJ1DCiAX/giphy.gif")

#add player gallery section
st.subheader("Gallery")
