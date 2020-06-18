import basilica
import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)

if __name__ == "__main__":
    sentences = ['Hello World", "How are you?"']
    embeddings = connection.embed_sentences(sentences)
    print(embeddings)

