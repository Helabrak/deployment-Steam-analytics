import pandas as pd
import json # The module we need to decode JSON
import re

#df = pd.read_csv("tmdb_5000_movies.csv")
#open json
with open ('C:/Users/acer.LAPTOP-OODPR6CI/Documents/GitHub/Deployment/deployment-Steam-analytics/steam scrape/database.json') as f:
    data=json.load(f)

df_1=pd.DataFrame(data)
pd.set_option('display.max_columns',111)
df_2=df_1.T


df_2_sub = df_2.filter(['name', 'steam_appid', 'required_age', 'is_free','short_description',
             'num_reviews','review_score', 'total_positive', 'total_negative','total_reviews'])

#df_2_sub.set_index('steam_appid',inplace = True)
#df_2_sub.reset_index(drop=True)

#print(df_2_sub.shape)
#print(df_2_sub.info())
#print(df_2_sub.head())

#df_3=df_2_sub['price_overview']
#df_2_sub.drop(['price_overview'],axis=1,inplace = True)

df_3 = df_2['price_overview'].apply(pd.Series)
#print(df_3.info())

df_3['final_formatted'] = df_3['final_formatted'].replace(",", ".", regex=True)
df_3['final_formatted'] = df_3['final_formatted'].replace(" ", "", regex=True)
df_price = pd.DataFrame(df_3['final'])
#df_3= pd.json_normalize(df_3)

df_4=pd.concat([df_2_sub,df_price],axis=1)
df_4=df_4.dropna(axis=0)
#df_4.reset_index(drop=True)
print(df_4.head())
print(df_4.info())

#convert object to int and float
df_4["required_age"]=df_4["required_age"].astype(int, errors = 'raise')
df_4["num_reviews"]=df_4["num_reviews"].astype(int, errors = 'raise')
df_4["review_score"]=df_4["review_score"].astype(int, errors = 'raise')
df_4["total_positive"]=df_4["total_positive"].astype(int, errors = 'raise')
df_4["total_negative"]=df_4["total_negative"].astype(int, errors = 'raise')
df_4["total_reviews"]=df_4["total_reviews"].astype(int, errors = 'raise')
df_4['final'] = df_4['final']/100
"""df_4['final_formatted'] = df_4['final_formatted'].replace("€", "", regex=True)
#df_4['final_formatted'] = df_4['final_formatted'].replace(regex=[0-9,\.], value='')
df_4['final_formatted'] = df_4['final_formatted'].replace("[^[0-9]]|[^\.]", "", regex=True)
df_4["final_formatted"]=df_4["final_formatted"].astype(str, errors = 'raise')
df_4["final_formatted"]=df_4["final_formatted"].astype(float, errors = 'raise')
"""
print(df_4['final']      )

print(df_4.info())
print(df_4.head())


'''
df_4["steam_appid"].astype(str).astype(int)

df_4["required_age"] = pd.to_numeric(df_4["required_age"])
df_4["num_reviews"] = pd.to_numeric(df_4["num_reviews"])
df_4["review_score"] = pd.to_numeric(df_4["review_score"])
df_4["total_positive"] = pd.to_numeric(df_4["total_positive"])
df_4["total_negative"] = pd.to_numeric(df_4["total_negative"])
df_4["total_reviews"] = pd.to_numeric(df_4["total_reviews"])
df_4["final_formatted"] = pd.to_numeric(df_4["final_formatted"])
'''



'''
# sample_type = type(df["genres"][0])
sample_type = type(df["type"][0])
print(f"The data type before using apply function: {sample_type}\n")

# Column names that contain JSON
json_cols=df.columns.tolist()

#json_cols = ['type', 'name', 'steam_appid', 'required_age', 'is_free', 'detailed_description',
#             'about_the_game', 'short_description', 'supported_languages', 'header_image',
#             'website', 'pc_requirements', 'mac_requirements', 'linux_requirements',
#             'legal_notice', 'developers', 'publishers', 'price_overview', 'packages',
#             'package_groups', 'platforms', 'categories', 'genres', 'screenshots', 'movies',
#             'release_date', 'support_info', 'background', 'content_descriptors', 'num_reviews',
#             'review_score', 'review_score_desc', 'total_positive', 'total_negative',
#             'total_reviews', 'controller_support', 'dlc', 'demos', 'recommendations',
#             'achievements', 'reviews', 'ext_user_account_notice', 'metacritic', 'drm_notice']


def clean_json(x):
    "Create apply function for decoding JSON"
    return json.loads(x)

# Apply the function column wise to each column of interest
for x in json_cols:
    df[x] = df[x].apply(clean_json)

sample_type2 = type(df["type"][0])
print(f"The data type after using apply function: {sample_type2}")


##############################
# One-Hot-Encode all JSON Data
##############################
def clean_json2(x):
    # store values
    ls = []

    # loop through the list f dictionaries
    for y in range(len(x[0])):

        # Access each key and value in each dictionary
        for k, v in x[0][y].items():
            # append column names to ls
            ls.append(str(k) + "_" + str(v))

    # create a new column or change 0 to 1 if keyword exists
    for z in range(len(ls)):

        # If column not in the df columns then make a new column and assign zero values while changing the current row to 1
        if ls[z] not in df.columns:
            df[ls[z]] = 0
            df[ls[z]].iloc[x.name] = 1
        else:
            df[ls[z]].iloc[x.name] = 1
    return


print("Original Shape", df.shape)

# Loop over all columns and clean json and create new columns
for x in json_cols:
    df[[x]].apply(clean_json2, axis=1)

print("New Shape", df.shape)
'''
