# deployment-Steam-analytics
data link : https://github.com/becodeorg/GNT-Arai-2.31/blob/master/content/additional_resources/datasets/steam%20scrape/database.json



## Parse json files

Json files are basicly nested dictionaries. a good way to store data but really difficult to acces. For this reason we have extracted the sub-dictionaries and have flattend them. In the end we took items from the json file which weren't dictionaries and created a pandas datafram. after that we concatenated this pd with the flattend dictionaries. Creating a larg pd

Before exporting the datafram to an sql database we first clean it. We found one big thing that we needed to rrslove and that is that there are different currrencies. Converting them into the sam currency gives us the option to plot them later and use this data correctley.

## Save json data into an SQL database
we  haven't flattend al the items from the json file. we also exported specific dictionaries directley to sql, these where in different tables, an example of this is genres.

Exporting the pandas datafram to sql wasn't that hard, just three lines. The problem arrises when the features aren't formatted correctley and gives error's. we formatted each column in it's respective datatype, str, float, int.

## Visualize data from a SQL database
Fo the visulisation of the work we have done we have chosen to display it on the interent. We deploy our database on a site we have created with streamlit. We chose streamlit because it is easier to create interactive websites with. This is a big plus for us because we can easily connect our database to streamlit. model how the site is going to look like and give the conusmer the opportunity to directley interect with the data as they see fit.


    


## Our code explained
    
    Use of Pandas to clean the data
    Tranposition of the rows to columns and the opposite
    Flattening
    Creation of a SQL database

![image](https://user-images.githubusercontent.com/84380899/131641487-1d280a6d-7e3a-4e28-acdc-e31dd9c9dd40.png)
![image](https://user-images.githubusercontent.com/84380899/131641663-85cee3fe-6978-4ce6-855a-a123e6087702.png)


