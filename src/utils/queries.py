create_topics_table_query = '''
  CREATE TABLE IF NOT EXISTS topics (
      id SERIAL PRIMARY KEY,
      name VARCHAR(100) NOT NULL
  );
  '''

create_news_table_query = '''
  CREATE TABLE IF NOT EXISTS news (
      id SERIAL PRIMARY KEY,
      author VARCHAR(255) NOT NULL,
      title VARCHAR(255) NOT NULL,
      description VARCHAR(255) NOT NULL,
      url VARCHAR(255) NOT NULL,
      urlToImage VARCHAR(255) NOT NULL,
      publishedAt TIMESTAMP,
      content TEXT,
      topic_id INTEGER,
      FOREIGN KEY (topic_id) REFERENCES topics(id)
  );
  '''

insert_topics_query = '''
    INSERT INTO topics (name)
    VALUES ('technology'), ('science'), ('politics'), ('entertainment'), ('health'), ('business'), ('sports');
    '''