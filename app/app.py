import pandas as pd
import numpy as np

from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import json
from io import BytesIO
import base64

from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from bs4 import BeautifulSoup

from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from sklearn.metrics.pairwise import linear_kernel


from flask import Flask, render_template, redirect, url_for, request
from forms import SearchForm
from model import get_recommendations, df, cosine_sim, plt_3dscatter



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

@app.route('/visual')
def visual():
    
    
    return render_template('visual.html', plt_3dscatter=plt_3dscatter)

if __name__ == '__main__':
    app.run(debug=True)


