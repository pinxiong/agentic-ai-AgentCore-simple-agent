# agentic-ai-AgentCore-simple-agent

# How to run this project

## install dependencies

```shell
uv add bedrock-agentcore strands-agents
```

```shell
uv run main.py
```

```shell
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"topic": "What is Agentic AI?"}' | jq .
```