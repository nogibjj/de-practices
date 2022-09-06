#!/usr/bin/env python3

"""An open AI api key is required to run this code. The engine leverages the GPT-3 model, and the code was 
written by Github copilot.
"""

import openai
import os
import click

# write a function that takes a text string and returns a summary of the text
def summarize(text):
    """Summarize a text string and return a summary of the text"""
    openai.api_key = os.getenv("OPEN_AI_SECRET_KEY")

    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"],
    )
    return response.choices[0].text
