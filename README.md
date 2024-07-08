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
**final_datatset_clean.csv**: pulled from ComicVine API (https://comicvine.gamespot.com/api/)
 - 0   character_credits
 - 1   character_died_in
 - 2   concept_credits     
 - 3   cover_date           
 - 4   description          
 - 5   has_staff_review     
 - 6   id                   
 - 7   issue_number        
 - 8   location_credits  
 - 9   name
 - 10  object_credits
 - 11  person_credits
 - 12  story_arc_credits
 - 13  team_credits
 - 14  team_disbanded_in
 - 15  volume
 - 16  combined_description


## References





