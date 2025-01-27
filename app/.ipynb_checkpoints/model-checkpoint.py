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

# Load and preprocess the dataset
df = pd.read_csv("final_dataset_clean.csv")
def final_fillna(df):
    df['description'] = df['description'].fillna('')
    df['combined_description'] = df['combined_description'].fillna('')
    lst = ['character_credits', 'character_died_in', 'concept_credits',
           'location_credits', 'object_credits', 'person_credits', 'story_arc_credits', 
           'team_credits', 'team_disbanded_in', 'volume']
final_fillna(df)

# Create the TF-IDF matrix
tfidf_des = TfidfVectorizer(stop_words='english')
tfidf_des_matrix = tfidf_des.fit_transform(df['description'])
tfidf_char = TfidfVectorizer(stop_words='english')
tfidf_char_matrix = tfidf_char.fit_transform(df['character_credits'])
tfidf_concept = TfidfVectorizer(stop_words='english')
tfidf_concept_matrix = tfidf_concept.fit_transform(df['concept_credits'])
tfidf_location = TfidfVectorizer(stop_words='english')
tfidf_location_matrix = tfidf_location.fit_transform(df['location_credits'])
tfidf_object = TfidfVectorizer(stop_words='english')
tfidf_object_matrix = tfidf_object.fit_transform(df['object_credits'])
tfidf_person = TfidfVectorizer(stop_words='english')
tfidf_person_matrix = tfidf_person.fit_transform(df['person_credits'])
tfidf_arc = TfidfVectorizer(stop_words='english')
tfidf_arc_matrix = tfidf_arc.fit_transform(df['story_arc_credits'])
tfidf_team = TfidfVectorizer(stop_words='english')
tfidf_team_matrix = tfidf_team.fit_transform(df['team_credits'])
tfidf_vol = TfidfVectorizer(stop_words='english')
tfidf_vol_matrix = tfidf_vol.fit_transform(df['volume'])

tfidf_vectorizers = [tfidf_des, tfidf_char, tfidf_concept, 
                    tfidf_location, tfidf_object, tfidf_person,
                    tfidf_arc, tfidf_team, tfidf_vol]
all_matrices = [tfidf_des_matrix, tfidf_char_matrix, tfidf_concept_matrix, 
               tfidf_location_matrix, tfidf_object_matrix, tfidf_person_matrix,
               tfidf_arc_matrix, tfidf_team_matrix, tfidf_vol_matrix]
weights = [3, 2, 1,
           1, 0, 1,
           0, 1, 0]
# Scale each TF-IDF matrix by its corresponding weight
weighted_tfidf_matrices = [matrix * weight for matrix, weight in zip(all_matrices, weights)]

combined_matrix = hstack(weighted_tfidf_matrices)

# Compute cosine similarity
cosine_sim = linear_kernel(combined_matrix, combined_matrix)

def get_recommendations(df, title, cosine_sim=cosine_sim):
    try:
        idx = df[df['name'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[0:21]  # Skip the first one as it is the title itself
        issue_indices = [i[0] for i in sim_scores]
        return df.iloc[issue_indices]
    except IndexError:
        return pd.DataFrame(columns=['name', 'issue_number', 'description'])

pca = PCA(n_components=3)
cosine_sim_pca = pca.fit_transform(cosine_sim)
cos_df = pd.DataFrame(cosine_sim_pca, columns=['PCA Component 1', 'PCA Component 2', 'PCA Component 3'])
cos_df['comic_name'] = df['name']
cos_df['volume'] = df['volume']
cos_df['character_credits'] = df['character_credits']
cos_df['description'] = df['description']
cos_df['issue_number'] = df['issue_number']
fig = plt.figure(figsize=(80, 64))
fig = px.scatter_3d(cos_df, x='PCA Component 1', y='PCA Component 2', z='PCA Component 3',
                color='volume',  # Color points based on 'volume'
                hover_data={'comic_name': True, 'volume': True, 'character_credits': False, 'description':False, 'issue_number':True},
                title='3D Scatter Plot of Cosine Similarity after PCA Transformation')
fig.update_layout(
    hovermode='closest',  # Show hover info for closest point
    hoverlabel=dict(bgcolor="white", font_size=16),
    width=int(1400), height=int(1000))
plt_3dscatter = fig.to_html(full_html=False)







