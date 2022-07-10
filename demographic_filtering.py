from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df3=pd.read_csv("articles.csv")


df=df3.sort_values(['total_events'], ascending=False)

returnvalue= df[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()

