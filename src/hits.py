
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import networkx as nx
import matplotlib.pyplot as plt

def createNetwork(articles):
   texts = [' '.join([str(article.get('title', '')), str(article.get('description', '')), str(article.get('content', ''))]) for article in articles]

   # Tokenize and preprocess the text
   stop_words = set(stopwords.words('english'))
   punctuation = set(string.punctuation)

   texts = [' '.join([word.lower() for word in word_tokenize(text) if word.isalnum() and word.lower() not in stop_words and word not in punctuation]) for text in texts]

   # Calculate TF-IDF vectors
   vectorizer = TfidfVectorizer()
   tfidf_matrix = vectorizer.fit_transform(texts)

   # Calculate cosine similarity
   cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

   # Establish edges based on similarity threshold
   edges = []
   threshold = 0.02

   for i in range(len(cosine_similarities)):
      related_articles = [(j, cosine_similarities[i, j]) for j in range(len(cosine_similarities[i])) if cosine_similarities[i, j] > threshold and j != i]
      edges.extend([(i, related_article) for related_article, _ in related_articles])


   G = nx.DiGraph()

   # Add nodes for each article
   for i, article in enumerate(articles):
      G.add_node(i, title=article['title'])  # Node represents an article, 'i' as node ID

   # Add edges between related articles
   for edge in edges:
      G.add_edge(edge[0], edge[1])  # Assuming 'edges' contains pairs of related article IDs
   return G


def getAuthorities(articles):
   graph = createNetwork(articles)
   hubs, authorities = nx.hits(graph)

   return sorted(authorities, key=authorities.get)
