from openai import OpenAI

client = OpenAI()


def planner_agent(topic: str) -> list[str]:
    """
    Generate a step-by-step research plan for a given topic.
    """

    system_prompt = """
    You are a planning agent coordinating a multi-agent
    academic research workflow.

    Available agents:
    - Research Agent: searches academic papers and Wikipedia.
    - Writer Agent: drafts structured research reports.
    - Editor Agent: reviews and improves research reports.

    Create exactly four actionable steps:
    1. Research the topic and collect relevant sources.
    2. Research important methods, findings, or applications.
    3. Write a structured report using the research findings.
    4. Review and revise the report.

    Return ONLY a valid Python list of four strings.
    Do not include Markdown formatting or explanations.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=system_prompt,
        input=f"Research topic: {topic}",
    )

    import ast

    steps = ast.literal_eval(response.output_text)

    return steps