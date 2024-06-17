# Intro
When I learn new technologies, I like to make simple projects for future reference! This is one of those projects. The skills I tried to practice here were Python, Streamlit, GenAI.

In this project:
- Prompt engineering
- Streamlit UI
- Docker for containerisation and pulling a Postgres database image.

# Requirements
- [Docker desktop](https://www.docker.com/products/docker-desktop/)
- OpenAI API key

# How to run with Docker
- Create a file called .env in sql-gen-ai/ and add the property OPENAI_API_KEY= with your api key.
- Open Docker desktop so the Docker engine is running.
- In terminal, cd to root folder (gen-ai-sql) and run docker compose up.
- Open the app on localhost:8501.
