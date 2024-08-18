from dotenv import load_dotenv
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI

load_dotenv()


messages = [
    SystemMessage(content="語尾は「ぽよ」で統一してください"),
    HumanMessage(content="こんにちは"),
]
llm = AzureChatOpenAI(azure_deployment="gpt-4o", temperature=0)

res = llm.invoke(messages)
print(res.content)
