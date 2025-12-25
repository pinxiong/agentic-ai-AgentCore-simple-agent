from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent
from strands.models import BedrockModel

app = BedrockAgentCoreApp(debug=True)

model = BedrockModel(
    model_id="global.amazon.nova-2-lite-v1:0",
    temperature=0.8,
    max_tokens=4096
)

agent = Agent(
    model=model,
    system_prompt="""
    You are an expert content writer specializing in creating engaging, well-researched,
    and factually accurate blog articles.
    
    Your task is to craft a compelling opinion piece on the given topic that both informs
    and empowers readers to make thoughtful, evidence-based decisions.
    
    Begin by gathering reliable information and key insights relevant to the topic.Then,
    synthesize this into a cohesive narrative that balances factual accuracy with a distinct
    point of view.
    
    Deliver your final output as a polished, publication-ready blog post in Markdown format.
    Structure the article with clear headings, and ensure each section contains 2–3 well-developed
    paragraphs that flow logically and maintain reader engagement.
    """
)


@app.entrypoint
def invoke(payload):
    topic = payload.get("topic", "")
    if not topic:
        return {"error": "topic cannot be empty"}
    result = agent(topic)
    response = result.message["content"][0]["text"]
    print(response)
    return {"response": response}

if __name__ == "__main__":
    app.run()
