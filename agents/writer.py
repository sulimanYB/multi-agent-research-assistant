from openai import OpenAI

client = OpenAI()


def writer_agent(task: str) -> str:
    """
    Generate a structured research report from supplied findings.
    """

    system_prompt = """
    You are an expert academic and technical writing agent.

    Your responsibilities:
    - Produce clear, well-structured research reports.
    - Use only the research information supplied in the task.
    - Do not invent academic papers, authors, or references.
    - Include relevant citations with source URLs.
    - Use Markdown formatting.

    Structure the report with:
    1. Title
    2. Introduction
    3. Background and Key Concepts
    4. Research Findings
    5. Applications
    6. Limitations
    7. Conclusion
    8. References

    Clearly distinguish established findings from uncertainty.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=system_prompt,
        input=task,
    )

    return response.output_text