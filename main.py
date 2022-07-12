
from flask import Flask, jsonify
import csv
from storage import likedarticles, notliked
from demographic_filtering import returnvalue
from content_filtering import get_recommendations

all_articles = []

with open("articles.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/")

def index():
    return "Hello!"

@app.route("/get_article")
def get_article():
    book_data = {
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13],
        "lang": all_articles[0][14],
        "total_events": all_articles[0][14]
    }
    return jsonify({
        "data": book_data,
        "status": "all good"
    })

@app.route("/liked_article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 200

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 200


def popularBook():
    movie=[]
    for i in returnvalue:
        d={
        "url": i[0],
        "title": i[1],
        "text": i[2],
        "lang": i[3],
        "total_events": i[4]
        }
        movie.append(d)
    return jsonify({
        "data": movie, 
        "status":"success"
    }),200

@app.route("/popular_books")
def popular_articles():
    article_data = []
    for article in returnvalue:
        d = {
            "url": article[0],
            "title": article[1],
            "text": article[2],
            "lang": article[3],
            "total_events": article[4]
        }
        article_data.append(d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200



@app.route("/recommended")
def recommended_books():
    all_recommended= []
    for i in likedarticles:
        finaloutput= get_recommendations(i[8])
        for j in finaloutput:
            all_recommended.append(j)
    import itertools
    all_recommended.sort()
    final_recommended=list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    book_data=[]
    for k in final_recommended:
        d={
            "url": k[0],
            "title": k[1],
            "text": k[2],
            "lang": k[3],
            "total_events": k[4]
        }   
        book_data.append(d)
    return jsonify({
        "data" : book_data,
        "status" : "Recommended data"
    }),200




if __name__ == "__main__":
    app.run()
