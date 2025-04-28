from crewai import Task

def create_plan_task(agent, user_prompt):
    return Task(
        description=f"""Based on this user prompt: "{user_prompt}"
        Make sure that there is character growth for postiive characters and a clear path for antagonist to go into their descent into evil. Also make sure that the number of chapters dont exceed four
        Include:
-       Setting
-       Main conflict
-       Beginning, middle, and end outline
-       Optional: Genre and tone""",
        expected_output="A structured story plan with clear sections.",
        agent=agent,
    )