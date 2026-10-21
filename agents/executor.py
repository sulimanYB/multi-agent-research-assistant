from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.writer import writer_agent
from agents.editor import editor_agent


def executor_agent(topic: str) -> dict:
    """
    Coordinate the multi-agent research workflow.
    """

    print("\n=== PLANNING ===")
    plan = planner_agent(topic)

    for i, step in enumerate(plan, 1):
        print(f"{i}. {step}")

    print("\n=== RESEARCH: STEP 1 ===")
    research_1 = research_agent(plan[0])

    print("\n=== RESEARCH: STEP 2 ===")
    research_2 = research_agent(plan[1])

    research_context = (
        f"Research topic: {topic}\n\n"
        f"First research findings:\n{research_1}\n\n"
        f"Additional research findings:\n{research_2}"
    )

    print("\n=== WRITING ===")
    draft = writer_agent(
        f"{plan[2]}\n\n"
        f"Use the following research findings:\n{research_context}"
    )

    print("\n=== EDITING ===")
    final_report = editor_agent(
        f"{plan[3]}\n\n"
        f"Review and revise this report:\n{draft}\n\n"
        f"Original research sources:\n{research_context}"
    )

    return {
        "topic": topic,
        "plan": plan,
        "research": [research_1, research_2],
        "draft": draft,
        "final_report": final_report,
    }