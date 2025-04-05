import json
import os

MEMORY_FILE = "memory.json"
CONFIG_FILE = "config.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"conversations": []}
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)

def save_memory(conversations):
    with open(MEMORY_FILE, "w") as file:
        json.dump({"conversations": conversations[-50:]}, file, indent=2)

def add_to_memory(message):
    data = load_memory()
    data["conversations"].append(message)
    save_memory(data["conversations"])

def get_last_messages(n=5):
    data = load_memory()
    return data["conversations"][-n:]

def save_name(name):
    config = load_config()
    config["name"] = name
    save_config(config)

def load_name():
    return load_config().get("name", "Hexgon")

def save_mode(mode):
    config = load_config()
    config["mode"] = mode
    save_config(config)

def load_mode():
    return load_config().get("mode", "normal")

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=2)
