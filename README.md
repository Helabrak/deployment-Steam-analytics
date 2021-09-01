# deployment-Steam-analytics
data link : https://github.com/becodeorg/GNT-Arai-2.31/blob/master/content/additional_resources/datasets/steam%20scrape/database.json



## Parse json files

Json files are basicly nested dictionaries. a good way to store data but really difficult to acces. For this reason we have extracted the sub-dictionaries and have flattend them. In the end we took items from the json file which weren't dictionaries and created a pandas datafram. after that we concatenated this pd with the flattend dictionaries. Creating a larg pd with these features.


| Name              | Steam_appid    | Required_age | Is_free         | 
| Short_description |num_reviews     |   Review_score |total_positive |
| Total_negative    | Total_revieuws | final_price    |       null       |

Before exporting the datafram to an sql database we first clean it. We found one big thing that we needed to rrslove and that is that there are different currrencies. Converting them into the sam currency gives us the option to plot them later and use this data correctley.

## Save json data into an SQL database
we  haven't flattend al the items from the json file. we also exported specific dictionaries directley to sql, these where in different tables, an example of this is genres.
![https://github.com/Helabrak/deployment-Steam-analytics/blob/f5abe9f1964da7b50dd90c928b25037b02fa015b/2tables.png] 

Exporting the pandas datafram to sql wasn't that hard, just three lines. The problem arrises when the features aren't formatted correctley and gives error's. we formatted each column in it's respective datatype, str, float, int.

## Visualize data from a SQL database
As part of the project we started with a minimum viable product. This just means we went through the whole process of parsing the data and constructing a database. We also created som visuals which show the relation between certain datapoints. The MVP was created to have something to show for each step of the way. We knew the interactive site would take a lot of work and in case it wasn't complete in time we still have this to show for our work.

![image](https://user-images.githubusercontent.com/84380899/131641487-1d280a6d-7e3a-4e28-acdc-e31dd9c9dd40.png) ![image](https://user-images.githubusercontent.com/84380899/131641663-85cee3fe-6978-4ce6-855a-a123e6087702.png)




Fo the visulisation of the work we have done we have chosen to display it on the interent. We deploy our database on a site we have created with streamlit. We chose streamlit because it is easier to create interactive websites with. This is a big plus for us because we can easily connect our database to streamlit. model how the site is going to look like and give the conusmer the opportunity to directley interect with the data as they see fit.


    







