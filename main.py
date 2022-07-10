
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
        "total_events": all_articles[0][15]
    }
    return jsonify({
        "data": book_data,
        "status": "all good"
    })

@app.route("/liked_article")
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

if __name__ == "__main__":
    app.run()