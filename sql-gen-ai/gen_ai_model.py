from openai import OpenAI
client = OpenAI()

def call_model(query):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": "Given the following SQL table, your job is to write queries given a user’s request. Return only the query, no other text.\n    \n    CREATE TABLE Movies (\n      ID INT,\n      NAME TEXT,\n      DIRECTOR TEXT,\n      RATING INT,\n     PROFITS INT,\n    PRIMARY KEY (ID)\n    );"
        },
        {
          "role": "user",
          "content": query
        }
      ]
    )
    return(response.choices[0].message.content)