from tools import search_tool
from llm import generate_answer

question = input("Ask a question: ")

context = search_tool(question)

print("\nContext:")
print(context)

answer = generate_answer(question, context)

print("\nAnswer:")
print(answer)