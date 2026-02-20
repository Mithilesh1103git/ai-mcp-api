import json
import os
import sys
import time
from pathlib import Path

# Add the project root (2 levels up from this file) to sys.path
project_root = str(Path(__file__).resolve().parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from fastapi.responses import StreamingResponse

from applications.api.src.langchain_module import chain

API_SERVER_HOST = os.getenv("API_SERVER_HOST", "localhost")
API_SERVER_PORT = int(os.getenv("API_SERVER_PORT", "8081"))
MCP_ENDPOINT_TYPE = os.getenv("MCP_ENDPOINT_TYPE", "http")
MCP_SERVER_HOST = os.getenv("MCP_SERVER_HOST", "localhost")
MCP_SERVER_PORT = int(os.getenv("MCP_SERVER_PORT", "8080"))

print(MCP_ENDPOINT_TYPE)


def get_llm_response():
    """
    Main function to get LLM model inference responses.
    """

    async def generate_response_content():
        try:
            response = await chain.ainvoke(
                {"message": f"Hello from LangChain to FastMCP!"}
            )
        except Exception as e:
            raise e
        response_json = json.loads(response)

        yield f"event: status\ndata: [begin]\n\n"

        query = response_json.get("query", "")
        if query:
            yield f"event: message\ndata: {json.dumps(query)}\n\n"

        data_events = response_json.get("data_events", [])
        for event in data_events:
            yield f"event: message\ndata: {json.dumps(event)}\n\n"
            time.sleep(0.1)

        yield f"event: status\ndata: [done]\n\n"

    return StreamingResponse(
        generate_response_content(), media_type="text/event-stream"
    )


if __name__ == "__main__":
    get_llm_response()
