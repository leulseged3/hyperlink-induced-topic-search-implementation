create_topics_table_query = '''
  CREATE TABLE IF NOT EXISTS topics (
      id SERIAL PRIMARY KEY,
      name VARCHAR(100) NOT NULL
  );
  '''

create_news_table_query = '''
  CREATE TABLE IF NOT EXISTS news (
      id SERIAL PRIMARY KEY,
      author VARCHAR(255),
      title TEXT,
      description TEXT,
      url VARCHAR(512),
      urlToImage VARCHAR(512),
      publishedAt TIMESTAMP,
      content TEXT,
      topic_id INTEGER,
      FOREIGN KEY (topic_id) REFERENCES topics(id)
  );
  '''

insert_news = ''' 
    INSERT INTO news (author, title, description, url, urlToImage, publishedAt, content, topic_id)
      VALUES %s
    '''
insert_first_topics_query = '''
    INSERT INTO topics (name)
    VALUES ('technology'), ('science'), ('politics'), ('entertainment');
    '''

insert_second_topics_query = '''
    INSERT INTO topics (name)
    VALUES ('health'), ('business'), ('sports');
    '''

fetch_topics = '''
SELECT id, name
FROM topics;
'''
def fetchTopic(topic):
  return  f'''SELECT id, name FROM topics WHERE name = '{topic}' '''

def fetchNews(topicId):
  return  f'''SELECT * FROM news WHERE topic_id = {topicId}'''
