import os
import json
from sqlalchemy import true
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import numpy as np

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./mintArt_abi.json')) as f:
        mintArt_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=mintArt_abi
    )

    return contract


# Load the contract
contract = load_contract()

st.title("Welcome Crusader! Happy Minting!")
st.header("Please Login")


################################################################################
# Login
################################################################################


with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    if password != "****":
        print("Incorrect Password")
    if st.form_submit_button('Login'):
        st.success('Logged in Successfully')



################################################################################
# Register New Artwork
################################################################################

st.subheader("Mint New Avatars Here!")
accounts = w3.eth.accounts
address = st.selectbox("Select the wallet address", options=accounts)
tokenURI = st.text_input("The URI to the artwork")
if st.button("Mint Artwork"):
    tx_hash = contract.functions.mintArtwork(tokenURI).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")

#st.markdown(contract.function.name.call())
#st.markdown(contract.functions.symbol.call())


################################################################################
# Display a Token
################################################################################

st.markdown("## Display an Art Token")
selected_address = st.selectbox("Select Account", options=accounts)
tokens = contract.functions.balanceOf(selected_address).call()
st.write(f"This address owns {tokens} tokens")
token_id = st.selectbox("Artwork Tokens", list(range(tokens)))
if st.button("Display"):
    # Get the art token owner
    owner = contract.functions.ownerOf(token_id).call()
    st.write(f"The token is registered to {owner}")

    # Get the art token's URI
    token_uri = contract.functions.tokenURI(token_id).call()
    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)
