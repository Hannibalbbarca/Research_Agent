from ddgs import DDGS

def search_documents(query):
    "Find upto 5 web results for a document requested"

    search_results = DDGS().text(query, max_results=5)
    documents = []

    for result in search_results:
        document = {
            "title": result.get("title"),
            "url": result.get("href"),
            "description": result.get("body",""),
        }
        documents.append(document)

    return documents

if __name__ == "__main__":
    query = input("Enter your search query: ")
    documents = search_documents(query)



    if not documents:
        print("No results found.")

    for number, document in enumerate(documents, start=1):
        print(f"\nResult {number}")
        print("Title:", document["title"])
        print("URL:", document["url"])
        print("Description:", document["description"])