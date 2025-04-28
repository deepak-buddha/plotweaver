from crewai import Task

def create_edit_task(agent):
    return Task(
        description="Edit the story for clarity, grammar, pacing, and add artistic flourishes if needed.",
        expected_output="A polished story along with chapter headings and a fitting title ",
        agent=agent,
    )