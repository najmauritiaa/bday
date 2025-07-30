import streamlit as st
from datetime import datetime
import time
import random
from PIL import Image
from streamlit_autorefresh import st_autorefresh
import base64

# Load local image and convert to base64
def get_base64_from_file(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get base64 string
img_base64 = get_base64_from_file("e.jpeg")

# Inject custom CSS with dark overlay
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(
            rgba(0, 0, 0, 0.5), 
            rgba(0, 0, 0, 0.5)
        ), url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if "card_picked" not in st.session_state:
    st.session_state.card_picked = False

# 🔁 Auto-refresh only if card not picked
if not st.session_state.card_picked:
    st_autorefresh(interval=1000, key="countdownrefresh")

# 🎯 Aya's Birthday
birthday = datetime(2025, 8, 17, 0, 0, 0)
now = datetime.now()
countdown = birthday - now

# 🎉 Title
st.title("🎂Dylon's Birthday Countdown🎂")
st.markdown(
    "<p style='text-align: center; font-size: 16px; color: white;'>"
    "🎈 17 August"
    "</p>",
    unsafe_allow_html=True
)

# Countdown
if not st.session_state.card_picked:
    if countdown.total_seconds() <= 0:
        st.success("🎈 Happy Birthday, Aya!")
        st.balloons()
    else:
        days = countdown.days
        hours, rem = divmod(countdown.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        st.markdown(f"""
            <div style='text-align: center; font-size: 60px; color: yellow;'>
                <div style="display: inline-block; margin: 0 15px;">
                    <div>{days:02d}</div>
                    <div style="font-size: 20px;">Days</div>
                </div>
                <div style="display: inline-block; margin: 0 15px;">
                    <div>{hours:02d}</div>
                    <div style="font-size: 20px;">Hours</div>
                </div>
                <div style="display: inline-block; margin: 0 15px;">
                    <div>{minutes:02d}</div>
                    <div style="font-size: 20px;">Minutes</div>
                </div>
                <div style="display: inline-block; margin: 0 15px;">
                    <div>{seconds:02d}</div>
                    <div style="font-size: 20px;">Seconds</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Load image from local folder
image = Image.open("dp.png")  # adjust path as needed

# Display the image
st.image(image, use_container_width=True)

# 🎴 Card Game
st.markdown("## Pick a Card to Reveal Your Themed Gift!")

cards = ["🎴 Card 1", "🎴 Card 2", "🎴 Card 3", "🎴 Card 4"]
presents = [
    "⚽Sports Essentials",
    "👕Apparel/Accessories",
    "🪀Toys/Figurine",
    "👀Secret",
]


cols = st.columns(4)
for i in range(4):
    if cols[i].button(cards[i]):
        st.session_state.card_picked = True
        st.session_state.card_result = presents[i]

# 🎁 Show Result
if st.session_state.get("card_picked", False):
    st.success(f"You got: {st.session_state.card_result}")
    st.balloons()

# 💖 Favorite Moments Section
st.markdown("---")
st.markdown("## About You ")

moments = [
    ("Pros", "punya pacar cantik"),
    ("Cons", "kebooo"),
    ("Note", "semoga sukses, rajin ibadah, makin banyak duit, sama jangan cuek ke aku hiks. semangat yaww kuliahnya. love u🤍"),
]

for title, description in moments:
    with st.expander(title):
        st.write(description)

# Birthday Wish Input
st.markdown("---")
st.markdown("## Birthday Wish")

wish = st.text_area("",placeholder="Type here...")

if st.button("Send Wish"):
    if wish.strip() != "":
        st.success("Aamiin")
    else:
        st.warning("Please write something before submitting!")
