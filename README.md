# LessWrong Bot

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

LessWrong Bot is a Python application that leverages natural language processing (NLP) to answer questions related to the work of Eliezer Yudkowsky on his [LessWrong](https://www.lesswrong.com/) website. The bot is capable of providing detailed and factual information from Eliezer Yudkowsky's publications.

You can chat with the bot [here](http://206.189.54.224:8501/).

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [How it Works](#how-it-works)
- [Feedback and Contribution](#feedback-and-contribution)
- [Contact the Project Maintainer](#contact-the-project-maintainer)

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.8 or higher
- Streamlit
- FAISS
- OpenAI Embeddings
- dotenv
- Other required dependencies (specified in `requirements.txt`)

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository
```bash
git clone https://github.com/yaroslavpoltoran/lesswrong-streamlit.git
cd lesswrong-streamlit
```
2. Create a `.env` file and add `OPENAI_API_KEY` variable there.
3. Run the Streamlit application:
```bash
streamlit run app.py
```
4. Access the bot via your web browser at http://localhost:8501.
5. Or just chat with the bot [here](http://206.189.54.224:8501/) :)

## Configuration
You can configure the bot's behavior by editing the config.py file. The following options are available:
1. `MODEL` - the model to use for question answering. Current model is `gpt-3.5-turbo`
2. `N_DOSC` - the number of documents to search for the answer. Note, each document contains up to 500 tokens, and `gpt-3.5-turbo` can process up to 4097 tokens at once. So, now `N_DOCS` is set to 8, the bot will process up to 4000 tokens + user's question.
3. `N_URLS` - the number of URLs to return to the user at the end of the answer. The bot will return the most relevant URLs from the top `N_DOCS` documents. If set to 0, the bot will not return any URLs.

## How it Works
The bot uses the following components:

- OpenAI Embeddings for language understanding.
- OpenAI ChatGPT for question answering.
- FAISS for similarity search. Please see `making_faiss_index.ipynb` to see how the index was created.
- Streamlit for the user interface.
- When a user inputs a question, the bot retrieves relevant publications from Eliezer Yudkowsky using FAISS. It then generates a detailed response using a language model and presents it to the user.

## Feedback and Contribution
If you encounter any issues, have feature suggestions, or would like to contribute to the development of this extension, please visit the [GitHub repository](https://github.com/yaroslavpoltoran/lesswrong-streamlit) and create an issue or pull request.

## Contact the Project Maintainer

If you have any questions or feedback, don't hesitate to reach out to the project maintainer:

**Yaroslav Poltoran**

- **Telegram**: [https://t.me/yaroslavpoltoran](https://t.me/yaroslavpoltoran)

Feel free to connect and get in touch with me. Your feedback is highly appreciated!