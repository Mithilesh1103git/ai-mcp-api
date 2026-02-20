
## Description: 

#### This is an AI model deployment using FastMCP, Langchain, and FastAPI, with MCP, chaining, and API implementation. It can be used as a universal agent for all tasks that can be optimized using an LLM-based agent. In the repository, the current response is static for demo purposes; however, in a practical scenario, any open-source or commercial proprietary LLM API can be used to generate responses. Kindly note that this is a simpler implementation of the MCP and API services for demo purposes. In a production environment, advanced features like network security, higher memory allocation, context management, and prompt engineering will be necessary.

## Setup:

#### Main apps directory: `/applications`.

#### Recommended Python version: `3.12.x`

## Usage SOP:

### Step 1: 
#### Go to the directory where you have cloned the repository and run the following command: 
    pip install -r requirements.txt
#### This command installs all the necessary external library packages needed for our application. 
#### Note: You might want to activate your Python venv before running the command, if you are using one.

### Step 2:
#### After the library packages are successfully installed, you can start the MCP server with the command:     
    uvicorn --host=0.0.0.0 --port=8080 applications.mcp:app
#### Alternatively, you can also use the command: 
    python3 src/mcp_server.py
#### Note: By default, the port must be 8080 for the API server to discover it. You can use a different port by changing the environment variable in the .env file, if wanted.

### Step 3:
#### Once the MCP server is up and running, you can start the API server with the following command: 
    uvicorn --host 0.0.0.0 --port 8081 applications.api:app

### Step 4:
#### You can call api with the following command: 
    curl -X GET http://<your-host>:<your-port>/api/v1/get-llm-response
#### For localhost, you can use the following command: 
    curl -X GET http://localhost:8081/api/v1/get-llm-response
#### For MS Windows localhost, you can use the following PowerShell command: 
    Invoke-RestMethod -Method GET http://localhost:8081/api/v1/get-llm-response
#### Note: You can use the port that you have set during the API server startup command in the earlier step. By default, it is set to 8081.

### Alternate method using Docker Compose:
#### You can directly use Docker Compose to start both the servers. CURL command to call the api remains the same. You can use the following Docker Compose command:
    docker compose up --build --force-recreate

## Additional Notes:
#### 1. In real world scenario, the LLM MCP server would be calling hosted models or paid models like OpenAI GPT. In this version, I am using a simple static response to all queries because hosting a model is not possible on a local system due to the size and resources required.
#### 2. In real world scenario, API calls would be POST calls and not GET calls. The client would be sending a prompt message in a POST call as data, which will be forwarded by the API server to the MCP server for model outputs. I have simplified this with GET calls since I am using static responses and not real model responses.
#### 3. Responses are in the format of SSE events, which can be used both in the API client and Web service client.
#### 4. OpenAI ChatGPT responses are currently disabled. This can be used to get a response from OpenAI and return it as a string. This function can be used in real-world scenarios where you want to get a response from OpenAI. Location of this function is `applications/mcp/src/mcp_server.py` `get_openai_response()`
