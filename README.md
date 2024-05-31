# Comic Recommendation System #

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

**Datasets**

Kaggle Marvel Dataset: marvel_comics.csv
- https://www.kaggle.com/discussions/general/284056
- Features:
<class 'pandas.core.frame.DataFrame'>
Index: 34853 entries, 0 to 34991
Data columns (total 13 columns):
 #   Column             Non-Null Count  Dtype         
---  ------             --------------  -----         
 0   comic_name         34853 non-null  object        
 1   active_years       34853 non-null  object        
 2   issue_title        34332 non-null  object        
 3   publish_date       34332 non-null  datetime64[ns]
 4   issue_description  30301 non-null  object        
 5   penciler           25398 non-null  object        
 6   writer             27508 non-null  object        
 7   cover_artist       12224 non-null  object        
 8   Imprint            11650 non-null  object        
 9   Format             32766 non-null  object        
 10  Rating             12583 non-null  object        
 11  Price              34853 non-null  float64       
 12  year               34332 non-null  float64       
dtypes: datetime64[ns](1), float64(2), object(10)
memory usage: 3.7+ MB
</class>

ComicVine API Dataset: batman0.csv
- This dataset is still incomplete. Must use API to gather for information. 
- However, this dataset has more features than the Marvel Dataset. 