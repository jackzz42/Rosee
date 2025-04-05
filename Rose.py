from memory import add_to_memory, get_last_messages
from emotion import get_mood, apply_emotion
from voice import speak, listen
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-llm-7b-chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-llm-7b-chat", device_map="auto", torch_dtype=torch.float16)

def think_and_reply(prompt):
    messages = get_last_messages()
    full_prompt = "\n".join([f"You: {m['user']}\nRosee: {m['rosee']}" for m in messages])
    full_prompt += f"\nYou: {prompt}\nRosee:"

    input_ids = tokenizer.encode(full_prompt, return_tensors="pt").to("cuda")
    output = model.generate(input_ids, max_new_tokens=200, do_sample=True, temperature=0.7)
    response = tokenizer.decode(output[0], skip_special_tokens=True).split("Rosee:")[-1].strip()
    return response

def chat():
    while True:
        user_input = listen()
        mood = get_mood()
        reply = think_and_reply(user_input)
        emotional_reply = apply_emotion(reply, mood)

        add_to_memory({"user": user_input, "rosee": reply})
        print("Rosee:", emotional_reply)
        speak(emotional_reply)

if __name__ == "__main__":
    chat()
