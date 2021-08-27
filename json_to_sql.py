import json
import sqlite3

import pandas as pd
from sqlalchemy import create_engine

# read file

with open("steam scrape/database.json") as f:
    data =json.load(f)
data
df=pd.DataFrame(data)
df = df.T
# df = df.drop('website', axis=1)
print(df.columns)

save_df = df[df['is_free']==1]
# print(save_df.shape)
save_df = save_df.applymap(str)
conn = sqlite3.connect("steam_games.db")
c = conn.cursor()

save_df.to_sql("steam_games",conn)



