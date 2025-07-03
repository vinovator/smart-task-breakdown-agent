from openai import OpenAI
from utils import load_config, save_task, load_memory

cfg = load_config()
client = OpenAI(api_key=cfg["openai"]["api_key"])


agent_prompt = """
You are a professional task planning agent. 

Your job is to breakdown the user's goal into a set of 5-10 clear, actionable steps. 
Make the steps concise, specific, and logical. Each steup should build on the previous one. 
For each step, include: Step description, Estimated time, Suggested tools or resources (if any)
The goal is: {goal}

Give your output as a numbered list.
"""

def breakdown_goal_with_memory(goal):
    """
    # role = system: Tells GPT what kind of agent it is. This shapes its personality and rules.
    # role = user: The actual prompt (instructions + user's goal)
    # temperature: Controls randomness
        0.0 = deterministic, good for strict tasks.
        0.7 = balanced creativity and structure
    """
    response = client.chat.completions.create(
        model = cfg["openai"]["model"],
        messages = [
            {"role": "system", "content": "You are a helpful assistant that breaks goals into tasks."},
            {"role": "user", "content": agent_prompt.format(goal=goal)}
        ],
        temperature = cfg["openai"]["temperature"]
    )

    task_list = response.choices[0].message.content.strip()
    save_task(goal, task_list)
    
    return task_list