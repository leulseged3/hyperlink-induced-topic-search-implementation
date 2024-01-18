from flask import Flask, request
from flask_cors import CORS
from utils import db_connect, queries
import hits

app = Flask(__name__)
CORS(app)

@app.route('/get-topics', methods=['GET'])
def getTopics():
    conn1 = db_connect.create_connection('news-aggregate-dataset-1')
    conn2 = db_connect.create_connection('news-aggregate-dataset-2')

    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()

    cursor1.execute(queries.fetch_topics)
    topic_from_dataset_1 = cursor1.fetchall()


    cursor2.execute(queries.fetch_topics)
    topic_from_dataset2 = cursor2.fetchall()


    cursor1.close()
    cursor2.close()

    conn1.close()
    conn1.close()

    return { "topics": topic_from_dataset_1 + topic_from_dataset2 }

@app.route('/get-news', methods=['GET'])
def getNews():
    param = request.args.get('topic', 'Guest')
    news = []
    sortedNews = []
    # From dataset one
    conn1 = db_connect.create_connection('news-aggregate-dataset-1')

    if conn1:
        cursor = conn1.cursor()
        query1 = queries.fetchTopic(param)
        cursor.execute(query1)
        topic = cursor.fetchone()
        if topic:
            cursor.execute(queries.fetchNews(topic[0]))
            fetchedNews = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            result_list = [dict(zip(column_names, row)) for row in fetchedNews]

            news.extend(result_list)
        cursor.close()
        conn1.close()

    # From dataset two
    conn2 = db_connect.create_connection('news-aggregate-dataset-2')

    if conn2:
        cursor = conn2.cursor()
        query2 = queries.fetchTopic(param)
        cursor.execute(query2)
        topic = cursor.fetchone()
        if topic:
            cursor.execute(queries.fetchNews(topic[0]))
            fetchedNews = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            result_list = [dict(zip(column_names, row)) for row in fetchedNews]

            news.extend(result_list)
        cursor.close()
        conn2.close()
    sortedNewsIndexes = hits.getAuthorities(news)

    for i in sortedNewsIndexes:
        for theNews in news:

            if theNews['id'] == i:
                sortedNews.append(theNews)
                break
    return sortedNews
if __name__ == '__main__':
    app.run(debug=True)