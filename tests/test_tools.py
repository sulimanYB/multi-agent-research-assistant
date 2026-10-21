from tools.research_tools import arxiv_search_tool, wikipedia_search_tool

def test_arxiv_search_tool_returns_list():
    results = arxiv_search_tool("ensemble Kalman filter", max_results=2)
    assert isinstance(results, list)
    assert len(results) > 0

def test_wikipedia_search_tool_returns_list():
    results = wikipedia_search_tool("Ensemble Kalman filter", sentences=2)
    assert isinstance(results, list)
    assert len(results) > 0