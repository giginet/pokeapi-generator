from llama_index import SimpleWebPageReader, GPTVectorStoreIndex
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    loader = SimpleWebPageReader(html_to_text=True)
    documents = loader.load_data(urls=['https://bulbapedia.bulbagarden.net/wiki/Empoleon_(Pok%C3%A9mon)'])
    index = GPTVectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    response = query_engine.query("What moves does Empoleon learn?")
    print(response)