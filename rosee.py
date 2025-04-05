from memory import add_to_memory, get_last_messages, save_name, load_name, save_mode, load_mode
from emotion import get_mood, apply_emotion, detect_emotion
from voice import speak, listen, wait_for_wake_word
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

torch.set_default_dtype(torch.float32)

model_path = "C:/Users/Acer/Downloads/roseeai/deepseek-7b"
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True, torch_dtype=torch.float32)

def think_and_reply(prompt):
    messages = get_last_messages()
    name = load_name()
    emergency = load_mode() == "emergency"

    full_prompt = f"Your name is {name}.\n"
    full_prompt += "\n".join([f"You: {m['user']}\nRosee: {m['rosee']}" for m in messages])
    full_prompt += f"\nYou: {prompt}\nRosee:"

    input_ids = tokenizer.encode(full_prompt, return_tensors="pt")
    output = model.generate(input_ids, max_new_tokens=200, do_sample=True, temperature=0.7)
    response = tokenizer.decode(output[0], skip_special_tokens=True).split("Rosee:")[-1].strip()

    if emergency:
        response = response.replace("love", "").replace("babe", "").replace("romantic", "")

    return response

def chat():
    speak("System ready. Say 'Hey Rosee' to start.")
    while True:
        wait_for_wake_word()

        user_input = listen()
        if not user_input:
            continue

        user_input = user_input.lower()

        if "shutdown now" in user_input:
            speak("Shutting down, goodbye.")
            break

        if "emergency mode" in user_input:
            save_mode("emergency")
            speak("Emergency mode activated. I will only assist you now.")
            continue

        if "exit emergency mode" in user_input:
            save_mode("normal")
            speak("Back to normal mode.")
            continue

        if "my name is" in user_input:
            name = user_input.split("my name is")[-1].strip()
            save_name(name)
            speak(f"Nice to meet you, {name}")
            continue

        mood = detect_emotion(user_input)
        reply = think_and_reply(user_input)
        emotional_reply = apply_emotion(reply, mood)

        add_to_memory({"user": user_input, "rosee": emotional_reply})
        print("Rosee:", emotional_reply)
        speak(emotional_reply)

if __name__ == "__main__":
    chat()
