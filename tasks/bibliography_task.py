from crewai import Task

def create_bibliography_task(agent):
    return Task(
        description="""Display the entire generated story first, then follow it with a well-organized bibliography listing the named entities 
        such as characters, places, events, and any other significant elements. The bibliography should be categorized by entity type (e.g., 
        Characters, Places, Events), and should appear after the complete story text.""",
        expected_output="""The entire final story with good formatting in markdown format highlighting the chapter names and the story title,
          followed by a well-organized bibliography listing the named entities categorized 
        by type (characters, places, events, etc.) at the end of the story.""",
        agent=agent,
    )

