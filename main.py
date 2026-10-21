from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

from agents.executor import executor_agent


def main():
    # Load OpenAI API credentials
    load_dotenv()

    # Define the research topic
    topic = "Ensemble Kalman Filter for time series forecasting"

    # Execute the multi-agent workflow
    result = executor_agent(topic)

    # Create the reports directory if necessary
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"research_report_{timestamp}.md"

    # Save the final research report
    report_path.write_text(
        result["final_report"],
        encoding="utf-8"
    )

    print("\n==================================")
    print("Research workflow completed!")
    print(f"Report saved to: {report_path}")
    print("==================================")


if __name