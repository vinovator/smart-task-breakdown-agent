import toml
import json
import os
from datetime import datetime

def load_config(path='config.toml'):
    """
    Load configuration from a TOML file.
    """
    return toml.load(path)


def save_task(goal, task_list):
    """
    Save the task breakdown to a memory file in JSON format.
    """
    memory_file = load_config()["agent"]["memory_file"]

    # Open the memory file if it exists, else create one
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            memory = json.load(f)
    else:
        memory = []

    # Add to memory
    memory.append(
        {
            "timestamp": datetime.now().isoformat(),
            "goal": goal,
            "tasks": task_list
        }
    )

    # Update the memory in json file
    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)


def load_memory():
    """
    Load the memory from the JSON file.
    """
    memory_file = load_config()["agent"]["memory_file"]

    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            return json.load(f)
    else:
        return []
    
    

        
