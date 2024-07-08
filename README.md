# Comic Book Recommendation System

## Project Overview
The comic book industry has been alive and well since the 1940s. With this comes an enormous amount of volumes and issues. That's not even taking account the various reboots, contradicting storylines and similar title names. Altogether, the DC fandom is a bethometh mess!!!<br>
The typical reader has to plow through tons of different sites to hunt for descriptions and summaries to decide what to read. This process is even harder for new fans who are not familiar with the comic series. 
<br>
**Solution**<br>
Using natural language processing and feature engineering, we will create a model that takes in an issue name that you have read before and output recommendations that are similar to your input <br>
The final product should be a simple website application created with either HTML/CSS/Flask to present our findings in an easily digestible method. <br>
**Impact**<br>
The resulting product will save the user time and energy as they browse for their next comic book. This allows them to efforlessly enjoy reading.




## Walkthrough Demo
1) download the `app` folder
2) run the `app.py` python file
3) enter `http://127.0.0.1:5000/` into url bar
4) enter an issue's name and click submit
5) look at results


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
`final_datatset_clean.csv`: pulled from ComicVine API (https://comicvine.gamespot.com/api/)
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





