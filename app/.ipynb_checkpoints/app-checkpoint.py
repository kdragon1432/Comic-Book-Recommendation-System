import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, redirect, url_for, request
from forms import SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

df = pd.read_csv("clean_data.csv")
df['description'] = df['description'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(df, title, cosine_sim=cosine_sim):
    try:
        idx = df[df['name'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[0:21]  # Skip the first one as it is the title itself
        issue_indices = [i[0] for i in sim_scores]
        return df.iloc[issue_indices]
    #return df[['name', 'issue_number', 'description']].iloc[issue_indices]
    except IndexError:
        return pd.DataFrame(columns=['name', 'issue_number', 'description'])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    issue_name = None
    results = pd.DataFrame()
    recommendations = pd.DataFrame()
    if form.validate_on_submit():
        issue_name = form.issue_name.data
        results = df[df['name'] == issue_name]
        if not results.empty:
            recommendations = get_recommendations(df, issue_name)
    return render_template('index.html', form=form, issue_name=issue_name, results=results, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)


