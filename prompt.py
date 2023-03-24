from dotenv import load_dotenv
import openai
import os

def user(): return """

Code for a node server with a /healthcheck endpoint that returns a 200 status code and a JSON response of {“status”: “ok”}.

""".strip()

def system(): return """

You are a programming assistant. When asked for code, respond only with executable code, do not include any other comments or formatting (do not include ``` to create a block), and do not include multiple examples or alternatives.

""".strip()

def examples():
    return [
        # {"role": "user", "content": "Example user query"},
        # {"role": "assistant", "content": "Example answer"},
    ]

def prompt():
    try:
        messages = [
                {"role": "system", "content": system()},
                *examples(),
                {"role": "user", "content": user()},
            ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        print(completion.choices[0].message.content)
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.error.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass
    except Exception as e:
        print(f"Unknown error: {e}")
        pass

def setup():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("Put your OpenAI API key in the OPENAI_API_KEY environment variable.")
    openai.api_key = openai_api_key

setup()
prompt()