import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, redirect, url_for, request
from forms import SearchForm
from model import get_recommendations, df

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

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


