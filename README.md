# agentic-ai-AgentCore-simple-agent

## Preparation

### Install Python package tool

There are several tools to manage Python packages, but I strongly recommend `uv` because it's easy and simple to use. Here is how we can install it.

1. macOS and Linux OS


```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Windows OS

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Make sure it works well after installation.
 

### Configure AWS credentials

1. Install AWS credentials, you can run
```shell
aws configure
```

2. Check you have configured
```shell
aws sts get-caller-identity
```

### Install dependencies 

```shell

# Download the project
git clone git@github.com:pinxiong/agentic-ai-AgentCore-simple-agent.git

# Initialize python project
uv init agentic-ai-AgentCore-simple-agent --python 3.14

# enter the project
cd agentic-ai-AgentCore-simple-agent

# install bedrock-agentcore and strands-agents
uv add bedrock-agentcore strands-agents
```

**NOTE**
- `bedrock-agentcore`：The Python SDK of AgentCore for runtime and integration of service
- `strands-agents`：The framework for simplifing the construction of the agent.



## How to run

Open your terminal and then execute the command below:
```shell
uv run main.py
```

The output you will see

```shell
agentic-ai-AgentCore-simple-agent % uv run main.py
INFO:     Started server process [12790]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
```

And then, open another terminal to execute the following command:

```shell
% curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"topic": "What is Agentic AI?"}' | jq .
```

**NOTE** the given topic is `What is Agentic AI?` , you can change it if wanted.
