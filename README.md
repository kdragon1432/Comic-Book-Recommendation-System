# The Comic Book Recommendation System #

## Project Overview ##
The comic book industry has been alive and well since the 1940s. With this comes an enormous amount of volumes and issues. That's not even taking account the various reboots, contradicting storylines and similar title names. Altogether, the Marvel and DC fandoms are bethometh messes. 

It is a challenge for vertern fans to navigate. Many new fans are put off by this hurdle. The question of, What shall I read next?, has never been harder to answer!

**Solution**

Using data science and machine learning, the goal is to create a model that will take in user preferences and output comic recommendations. 

The user’s preferences could be based on a favorite character/team, plotline (action/slice of life), favorite writer or artist, etcetc. Recommendations are also based on similarities to between comics that you have read before. These models will be created using various classification machine learning methods and natural language processing. 

The final product should be a simple website created with either HTML/CSS or Ruby to present our findings in an easily digestible method. 

**Impact**

The main service that our solution provides is convenience. The typical reader has to plow through tons of different sites to hunt for descriptions and summaries to decide what to read. This process is even harder for new fans who are not familiar with the comic series. 

Our model does the legwork, saving the user both time and effort. This allows them to effortlessly enjoy reading. 


## Project Organization ##



**Datasets**

Kaggle Marvel Dataset: marvel_comics.csv
- https://www.kaggle.com/discussions/general/284056
- Features:     
 0   comic_name         34853 non-null  object    <br />    
 1   active_years       34853 non-null  object     <br />   
 2   issue_title        34332 non-null  object       <br /> 
 3   publish_date       34332 non-null  datetime64[ns]<br />
 4   issue_description  30301 non-null  object        <br />
 5   penciler           25398 non-null  object        <br />
 6   writer             27508 non-null  object        <br />
 7   cover_artist       12224 non-null  object        <br />
 8   Imprint            11650 non-null  object        <br />
 9   Format             32766 non-null  object        <br />
 10  Rating             12583 non-null  object        <br />
 11  Price              34853 non-null  float64       <br />
 12  year               34332 non-null  float64       <br />

ComicVine API Dataset: batman0.csv
- This dataset is still incomplete. Must use API to gather for information. 
- However, this dataset has more features than the Marvel Dataset. 
- Features:
 0   aliases                      0 non-null      float64 <br />
 1   api_detail_url               200 non-null    object <br />
 2   associated_images            200 non-null    object <br />
 3   character_credits            200 non-null    object <br />
 4   character_died_in            200 non-null    object <br />
 5   concept_credits              200 non-null    object <br />
 6   cover_date                   200 non-null    object <br />
 7   date_added                   200 non-null    object <br />
 8   date_last_updated            200 non-null    object <br />
 9   deck                         3 non-null      object <br />
 10  description                  181 non-null    object <br />
 11  first_appearance_characters  0 non-null      float64 <br />
 12  first_appearance_concepts    0 non-null      float64 <br />
 13  first_appearance_locations   0 non-null      float64<br/>
 14  first_appearance_objects     0 non-null      float64<br />
 15  first_appearance_storyarcs   0 non-null      float64<br />
 16  first_appearance_teams       0 non-null      float64<br />
 17  has_staff_review             200 non-null    object <br />
 18  id                           200 non-null    float64<br />
 19  image                        200 non-null    object <br />
 20  issue_number                 200 non-null    object <br />
 21  location_credits             200 non-null    object <br />
 22  name                         200 non-null    object <br />
 23  object_credits               200 non-null    object <br />
 24  person_credits               200 non-null    object <br />
 25  site_detail_url              200 non-null    object <br />
 26  store_date                   17 non-null     object <br />
 27  story_arc_credits            200 non-null    object <br />
 28  team_credits                 200 non-null    object <br />
 29  team_disbanded_in            200 non-null    object <br />
 30  volume                       200 non-null    object <br />