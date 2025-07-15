# Paper-to-Podcast 🎤

**Paper-to-Podcast** is a tool that transforms academic research papers into an engaging and conversational podcast format. With this project, listeners can absorb the content of a research paper in a lively discussion involving three distinct personas—perfect for those who prefer listening over reading, especially during commutes or travel.

## Project Overview

### Objective
This app simulates a three-person discussion around the content of a research paper, making complex information more accessible and enjoyable to absorb. Instead of merely reading aloud, it converts papers into conversations that are engaging and intuitive, providing valuable insights and critical thinking.

### Personas
- **Host**: Guides the conversation, introducing each section and explaining the main points in an engaging and warm tone.
- **Learner**: Asks intuitive questions and brings curiosity to the discussion, helping listeners grasp core concepts.
- **Expert**: Provides in-depth knowledge and additional details, enhancing the discussion with profound insights.

This structure fosters an interactive listening experience, helping users better understand the paper in a way that feels natural and human.

### Code Structure and Key Components
- **Planning Chain**: Starts by creating a detailed plan for each section of the paper. Planning helps the model stay on track, reducing the chances of hallucinations or redundancy.
- **Discussion Chain**: Uses a retrieval-augmented generation model to expand on each section. This ensures the script stays true to the source content while generating meaningful dialogue.
- **Enhancement Chain**: Finalizes the script by removing redundancies, refining transitions, and ensuring a smooth flow.
- **Text-to-Speech**: The generated script is then converted into audio using the OpenAI API, producing realistic voices for each persona.

### Cost Efficiency
The app is cost-effective, utilizing OpenAI's API. For example, generating a 9-minute podcast from a 19-page research paper costs approximately $0.16.

### Prerequisites
1. Ensure you have a valid OpenAI API key stored in your `.env` file.

### Running the App
argument:
   ```bash
   streamlit run app.py
   ```

