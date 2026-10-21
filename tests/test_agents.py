from dotenv import load_dotenv
load_dotenv()

from agents.planner import planner_agent

def test_planner_agent_returns_four_steps():
    plan = planner_agent("Ensemble Kalman Filter for time series forecasting")
    assert isinstance(plan, list)
    assert len(plan) == 4
    assert all(isinstance(step, str) for step in plan)