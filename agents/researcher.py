import json
from openai import OpenAI

from tools.research_tools import (
    arxiv_search_tool,
    wikipedia_search_tool,
)

client = OpenAI()


def research_agent(task: str) -> str:
    """
    Research a topic using OpenAI function calling
    with arXiv and Wikipedia.
    """

    tools = [
        {
            "type": "function",
            "name": "arxiv_search_tool",
            "description": "Search arXiv for academic research papers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "max_results": {
                        "type": "integer",
                        "default": 5,
                    },
                },
                "required": ["query"],
            },
        },
        {
            "type": "function",
            "name": "wikipedia_search_tool",
            "description": "Search Wikipedia for background information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "sentences": {
                        "type": "integer",
                        "default": 5,
                    },
                },
                "required": ["query"],
            },
        },
    ]

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=(
            "You are an academic research assistant. "
            "Use the available research tools to gather factual "
            "information. Summarise findings and include source URLs. "
            "Do not invent references."
        ),
        input=task,
        tools=tools,
        tool_choice="required",
    )

    tool_outputs = []

    for item in response.output:
        if item.type != "function_call":
            continue

        arguments = json.loads(item.arguments)

        if item.name == "arxiv_search_tool":
            result = arxiv_search_tool(**arguments)

        elif item.name == "wikipedia_search_tool":
            result = wikipedia_search_tool(**arguments)

        else:
            continue

        print(f"Tool executed: {item.name}")

        tool_outputs.append({
            "tool": item.name,
            "results": result,
        })

    return json.dumps(tool_outputs, indent=2)