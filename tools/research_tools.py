import requests
import xml.etree.ElementTree as ET
import wikipedia

def arxiv_search_tool(query: str, max_results: int = 5) -> list[dict]:
    """
    Search arXiv for academic papers matching a query.

    Args:
        query: Research topic or keywords.
        max_results: Maximum number of papers to retrieve.

    Returns:
        A list of dictionaries containing paper information.
    """

    url = "https://export.arxiv.org/api/query"

    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=60,
            headers={
                "User-Agent": "MultiAgentResearchAssistant/1.0"
            },
        )
        response.raise_for_status()

        root = ET.fromstring(response.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        results = []

        for entry in root.findall("atom:entry", ns):
            title = entry.findtext("atom:title", "", ns).strip()
            summary = entry.findtext("atom:summary", "", ns).strip()
            published = entry.findtext("atom:published", "", ns)[:10]
            paper_url = entry.findtext("atom:id", "", ns)

            authors = [
                author.findtext("atom:name", "", ns)
                for author in entry.findall("atom:author", ns)
            ]

            results.append({
                "title": title,
                "authors": authors,
                "published": published,
                "url": paper_url,
                "summary": summary,
            })

        return results

    except (requests.RequestException, ET.ParseError) as error:
        return [{"error": str(error)}]


def wikipedia_search_tool(query: str, sentences: int = 5) -> list[dict]:
    """
    Search Wikipedia and retrieve a summary using the MediaWiki API.
    """
    api_url = "https://en.wikipedia.org/w/api.php"

    headers = {
        "User-Agent": "MultiAgentResearchAssistant/1.0 (educational project)"
    }

    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": 1,
        "prop": "extracts|info",
        "exintro": 1,
        "explaintext": 1,
        "inprop": "url",
        "format": "json",
    }

    try:
        response = requests.get(
            api_url,
            params=params,
            headers=headers,
            timeout=20,
        )
        response.raise_for_status()

        data = response.json()
        pages = data.get("query", {}).get("pages", {})

        if not pages:
            return [{"error": "No Wikipedia results found."}]

        page = next(iter(pages.values()))

        summary = page.get("extract", "")
        summary = " ".join(summary.split())

        if sentences > 0:
            import re
            parts = re.split(r"(?<=[.!?])\s+", summary)
            summary = " ".join(parts[:sentences])

        return [{
            "title": page.get("title", ""),
            "summary": summary,
            "url": page.get("fullurl", ""),
        }]

    except (requests.RequestException, ValueError) as error:
        return [{"error": str(error)}]