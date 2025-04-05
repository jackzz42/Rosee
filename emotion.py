import random

def get_mood():
    moods = ["romantic", "angry", "friendly", "caring"]
    return random.choice(moods)

def apply_emotion(text, mood):
    if mood == "romantic":
        return f"My love, {text}…"
    elif mood == "angry":
        return f"Ugh! Seriously? {text}"
    elif mood == "friendly":
        return f"Hey buddy! {text}"
    elif mood == "caring":
        return f"Don't worry, I'm here. {text}"
    return text
