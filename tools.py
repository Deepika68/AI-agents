from ddgs import DDGS

def search_tool(query):

    context = ""

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        for i, result in enumerate(results,1):

            context += (
                f"Source {i}\n"
                f"Title: {result['title']}\n"
                f"Summary: {result['body']}\n\n"
            )

    except Exception as e:
        context = f"Search error: {e}"

    return context