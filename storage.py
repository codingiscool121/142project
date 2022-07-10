import csv

with open("articles.csv", encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_moves=data[1:]

likedarticles=[]
notliked=[]