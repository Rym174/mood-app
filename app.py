import streamlit as st
import random

# Mood-to-compliments dictionary
compliments = {
    "happy": [
        "You glow different today ✨",
        "Your smile is contagious! 😄",
        "You're like sunshine on a rainy day ☀️"
    ],
    "sad": [
        "You’re doing your best, and that’s enough 💖",
        "This too shall pass 🌈",
        "You’ve survived 100% of your worst days so far 🌷"
    ],
    "angry": [
        "Take a deep breath 🌬️ You’ve got this",
        "Your calm is stronger than the chaos 🧘",
        "You deserve peace, not pressure 💆"
    ],
    "tired": [
        "Even the stars need rest 🌟",
        "You’re allowed to pause and recharge 🔋",
        "Nap now, conquer later 😴"
    ],
    "anxious": [
        "You are safe right now 💗",
        "Inhale courage, exhale doubt 🌸",
        "One step at a time. You’re doing great 💫"
    ],
    "bored": [
        "Maybe it's time to try something silly, like dancing alone 💃",
        "Boredom is the gateway to imagination — go be weird 🎨",
        "Even geniuses got bored before they invented cool stuff 🧠💡"
    ],
    "good": [
        "Keep riding that good vibe 🌈",
        "You make ordinary days feel magical ✨",
        "The universe notices your light — keep shining 🌟"
    ],
    "bad": [
        "It’s okay to have off days. You’re still incredible 💖",
        "You don’t have to be strong all the time. Just be real 🌧️",
        "Even storms eventually run out of rain 🌦️"
    ]
}

# Streamlit UI
st.title("💖 Mood-Based Compliment Generator")

mood = st.selectbox("How are you feeling today?", list(compliments.keys()))

if st.button("Give me a compliment!"):
    st.success(random.choice(compliments[mood]))

