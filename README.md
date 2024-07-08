# Comic Book Recommendation System

## Project Overview


## Walkthrough Demo


## Project Flowchart


## Project Organization
* `app`
  - contains the html/python/flask Web App for the capstone project
* `data`
  - contains all the datasets pulled using ComicVine's API
  - `final`
    - contains the final combined and cleanned dataset (of all pulled data) used in the model
  - `marvel`
    - contains the marvel dataset found on kaggle and used during earlier sprints in capstone project
* `old_sprints`
  - contains powerpoints of old sprints and zip files with earlier phases of the capstone project
* `01_comicvine_API.ipynb`
  - notebook that contains the api functions used to pull my datasets
* `02_concat_final_csv.ipynb`
  - notebook where all pulled datasets were combined into one (large) final dataset to use
* `03_cleaning_final_dataset.ipynb`
  - notebook where the final dataset was cleaned and went through preprocessing/feature engineering in preparation for usage in model
* `04_final_dataset_EDA1.ipynb`
  - notebook containing basic EDA on the final dataset
* `05_final_dataset_EDA2.ipynb`
  - notebook containing more advance EDA on the final dataset after vectorizing and using average tfidf scores
* `06_final_rec_model_ipynb`
  - notebook containing the final recommendation model for the project
* `README.md`
  - project landing page (this page)


## Dataset
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6767 entries, 0 to 6766
Data columns (total 17 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   character_credits     6767 non-null   object
 1   character_died_in     6767 non-null   object
 2   concept_credits       6767 non-null   object
 3   cover_date            6767 non-null   object
 4   description           6669 non-null   object
 5   has_staff_review      6767 non-null   object
 6   id                    6767 non-null   int64 
 7   issue_number          6767 non-null   object
 8   location_credits      6767 non-null   object
 9   name                  6767 non-null   object
 10  object_credits        6767 non-null   object
 11  person_credits        6767 non-null   object
 12  story_arc_credits     6767 non-null   object
 13  team_credits          6767 non-null   object
 14  team_disbanded_in     6767 non-null   object
 15  volume                6767 non-null   object
 16  combined_description  6767 non-null   object
dtypes: int64(1), object(16)
memory usage: 898.9+ KB



## References





