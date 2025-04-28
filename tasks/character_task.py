from crewai import Task

def create_character_task(agent, user_prompt):
    return Task(
        description = f"""Based on the user prompt: "{user_prompt}", and the planned story structure,
create the main characters. If the user provided characters, expand on them.
Otherwise, invent interesting protagonists, sidekicks, and antagonists with good character development. """,
        expected_output="A list of main characters with descriptions, personalities, and motivations.",
        agent=agent,
    )