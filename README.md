# PlotWeaver

PlotWeaver is a multi-agent CrewAI creative writing assistant that generates short stories (up to 4 chapters, 1000-2000 words) based on your prompts.

In this project, groq model "llama-3.3-70b-versatile" is used for its advanced language understanding and creative narrative generation, with free usage up to a certain limit. Alternative LLMs include models from Mistral and OpenAI.

## Overview

PlotWeaver uses a crew of specialized AI agents to craft engaging stories from simple prompts. Each agent handles a specific aspect of the storytelling process:

- **Story Planner**: Creates the overall structure and plot.
- **Character Designer**: Develops interesting, well-rounded characters.
- **Story Writer**: Writes the actual narrative based on the plan and characters.
- **Story Editor**: Polishes the text and organizes it into chapters.
- **Bibliographer**: Catalogs all named entities (characters, places, events).

## Features

- Generate complete stories from simple text prompts.
- Automatic character development and world-building.
- Structured narrative with proper pacing and flow.
- Stories organized into clear chapters.
- Full bibliography of all named entities.

## Installation

1. Clone this repository.
2. Create a conda environment:
   ```
   conda env create -f environment.yml
   ```
   Alternatively, install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. Activate the conda environment:
   ```
   conda activate crewai_env
   ```

2. Run the application:
   ```
   streamlit run main.py
   ```

3. Enter your story prompt in the text field.
4. Click "Generate Story" and wait for the magic to happen!

## Example Prompts

- "What if Voldemort had won in the Harry Potter series"
- "A journey through space where the crew discovers an ancient alien artifact"
- "Game of Thrones ending but a better character ending for Daenerys"

## How It Works

1. The Story Planner creates the overall narrative structure.
2. The Character Designer develops the main characters.
3. The Story Writer crafts the complete narrative.
4. The Story Editor polishes and organizes the text.
5. The Bibliographer creates a catalog of all named entities.

## Potential Improvements

- **Interactive Editing**: Enable users to request specific revisions to generated stories.
- **Story Visualization**: Integrate image generation APIs like DALL-E to create chapter-specific illustrations and logos, enhancing the storytelling experience.
- **Fine-tuning Controls**: Let users adjust parameters like creativity, complexity, and tone.
- **Character Artwork**: Generate character portraits to accompany character descriptions.


## Acknowledgments

- Built with CrewAI
- Powered by Groq LLMs
