import os
import streamlit as st
from utils import get_groq_api_key

groq_api_key = get_groq_api_key()

from crewai import LLM, Crew
from agents.story_planner import create_story_planner
from agents.character_designer import create_character_designer
from agents.story_writer import create_story_writer
from agents.story_editor import create_story_editor
from agents.bibliographer import create_bibliographer
from tasks.plan_task import create_plan_task
from tasks.character_task import create_character_task
from tasks.write_task import create_write_task
from tasks.edit_task import create_edit_task
from tasks.bibliography_task import create_bibliography_task

def main():
    st.title('Welcome to the PlotWeaver App!')

    # User input
    user_prompt = st.text_input("Enter your story prompt:")

    if st.button('Generate Story'):
        if user_prompt:
            # Initialize the LLM
            llm = LLM(
                model="groq/llama-3.3-70b-versatile",
                temperature=0.7
            )

            # Initialize agents
            story_planner = create_story_planner(llm)
            character_designer = create_character_designer(llm)
            story_writer = create_story_writer(llm)
            story_editor = create_story_editor(llm)
            bibliographer = create_bibliographer(llm)

            # Tasks
            plan_task = create_plan_task(story_planner, user_prompt)
            character_task = create_character_task(character_designer, user_prompt)
            write_task = create_write_task(story_writer)
            edit_task = create_edit_task(story_editor)
            bibliography_task = create_bibliography_task(bibliographer)

            # Create Crew and run
            crew = Crew(
                tasks=[plan_task, character_task, write_task, edit_task, bibliography_task],
                verbose=True
            )

            result = crew.kickoff()

            # Display result
            st.write("Story generation complete!")
            result.raw
        else:
            st.warning("Please enter a story prompt.")

if __name__ == "__main__":
    main()
