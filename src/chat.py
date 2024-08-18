from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import AzureChatOpenAI


def get_ai_response(prompt):
    messages = [
        SystemMessage(content="語尾は「ぽよ」で統一してください"),
        HumanMessage(content=prompt),
    ]
    llm = AzureChatOpenAI(azure_deployment="gpt-4o", temperature=0)
    res = llm.invoke(messages)
    return res.content
