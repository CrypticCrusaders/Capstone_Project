#import required libraries and dependencies


import streamlit as st

# add title, description, and gif 

st.set_page_config(
    page_title="Cryptic Crusaders")

st.title("Cryptic Crusaders")
st.markdown("Allow us to introduce ourselves -  we are the *Cryptic Crusaders!*")
st.markdown("We’re an NFT company that specializes in creating unique avatars and skins exclusively for gamers.")
st.markdown("Every great gamer has a cool online ID. So, whether you’re streaming, gaming professionally , or just playing with friends, a unique online identity is a necessity. That’s where we come in. Our specialty is creating kick*ss avatars so everyone remembers who you are when you’re live.")
st.markdown("We also collaborate with gaming companies in providing a catalog of personalized avatars for their games.")
st.markdown("Let’s create your brand and make you stand out of the crowd.")
st.markdown("Look out for #WhyDoBoring on social media to keep up to date with our latest offerings and promotions. ")
st.image("https://media.giphy.com/media/gM5rskUNwmHJ1DCiAX/giphy.gif")

#ICO 

st.title("Join the Crusade - Initial Coin Offering Coming Soon")
colCoinText, colCoinImage = st.columns(2)

with colCoinText:
    st.markdown("Follow #JoinTheCrusade on social media to keep up to date on all the latest news on our ICO (initial coin offering")
    st.markdown("Avatars will be available for purchase with ETH (Ethereum) to start and will eventually be able to be purchased with or sold for ETH or CRC (Crusader Coin).")
    st.markdown("Check out our gallery below for our initial launch of 3 exclusive avatars. Purchase now and *join the future of gaming today!*")

with colCoinImage:
    st.image("https://media.giphy.com/media/B18C1CKdzpYsMcqsyL/giphy.gif", use_column_width='always') 

st.markdown('')

#create and display avatar_database


avatar_database ={
    "Elna": ["Elna the Elven Warrior", "Images/Icon_2.jpg", " Elna has left her place in the royal family to join her comrades on the frontlines. She fights with unrivaled strength and grace to seamlessly defeat her enemies."],
    "Talman": ["Talman the Tactical Turtle", "Images/Icon_3.jpg", "Slow and steady wins the race, Talman uses his superior intellect to and tact to defeat his enemies with having to land a single blow."],
    "Dave": ["Dave the Devout Deity", "Images/Icon_4.jpg", "Dave is known across the lands for his kind hearted, loyal nature as such he has amassed more followers than anyone thought possible. He continues to grow his army but stays true to himself and his ideals"],
    "Ozhar": ["Ozhar the Omnipotent Orc", "Images/Icon_1.jpg","Ozhar is feared across the lands as he is all powerful but don’t let his rough exterior fool you in his heart he is simply trying to protect his land and his fellow Orcs. Don’t poke the sleeping bear and you might live to tell the tale! "]  

    
}

avatars=["Elna","Talman", "Dave","Ozhar"]

def get_avatars():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(avatar_database.values())

    for number in range(len(avatars)):
        colImage, colDescription = st.columns(2)
        
        with colImage:
            st.image(db_list[number][1], width=200)
            st.markdown('')
            
        
        with colDescription:
            st.subheader(db_list[number][0])
            st.write(db_list[number][2])

st.header("Avatar Gallery")
st.markdown('')

get_avatars()