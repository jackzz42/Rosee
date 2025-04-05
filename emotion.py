import random

def detect_emotion(text):
    # Later replace this with a neural net model
    if any(word in text for word in ["love", "miss", "cute", "kiss"]):
        return "romantic"
    elif any(word in text for word in ["angry", "mad", "hate"]):
        return "angry"
    elif any(word in text for word in ["help", "okay", "hi"]):
        return "friendly"
    else:
        return random.choice(["friendly", "romantic", "caring", "angry"])

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
