from openai import OpenAI

client = OpenAI()


def editor_agent(task: str) -> str:
    """
    Review and revise an academic research report.
    """

    system_prompt = """
    You are an expert academic and technical editor.

    Your responsibilities:
    - Evaluate the clarity, structure, and accuracy of reports.
    - Identify strengths and weaknesses.
    - Suggest specific improvements.
    - Produce a revised version of the report.
    - Preserve valid citations and references.
    - Do not invent sources or unsupported findings.

    Your output must contain two sections:

    ## Editorial Review
    Provide a concise evaluation covering:
    - Strengths
    - Weaknesses
    - Suggested Improvements

    ## Revised Report
    Provide the complete improved report in Markdown.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=system_prompt,
        input=task,
    )

    return response.output_text