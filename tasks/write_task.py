from crewai import Task

def create_write_task(agent):
    return Task(
        description="Write the complete story using the given story structure and characters.",
        expected_output="A detailed story of about 1000-2000 words.",
        agent=agent,
    )
