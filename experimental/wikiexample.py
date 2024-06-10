from langchain_community.document_loaders import WikipediaLoader

query = "openai"
content = WikipediaLoader(query=query).load()
print(content)

