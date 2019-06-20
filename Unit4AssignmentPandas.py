#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


purchase_data = pd.read_csv("Resources/purchase_data.csv")
purchase_data.head()


# In[3]:


uniqueplayers = len(purchase_data["SN"].unique())
totalplayers = {"Total Players":[uniqueplayers]}
totaldf = pd.DataFrame(totalplayers)
totaldf


# In[4]:


uniqueitems = len(purchase_data["Item ID"].unique())
avgprice = round(purchase_data["Price"].mean(), 2)
totalpurchases = purchase_data["Purchase ID"].count()
totalrevenue = purchase_data["Price"].sum()
purchasinganalysis = {"Number of Unique Items": [uniqueitems], 
                      "Average Price":[avgprice],
                      "Number of Purchases": [totalpurchases],
                      "Total Revenue": [totalrevenue]}
purchasedf = pd.DataFrame(purchasinganalysis)
purchasedf


# In[5]:


maledata = purchase_data.loc[purchase_data["Gender"]=='Male']
malecount= len(maledata["SN"].unique())
maleper = (malecount*100)/uniqueplayers
malepercent = round(maleper, 2)

femaledata = purchase_data.loc[purchase_data["Gender"]=='Female']
femalecount= len(femaledata["SN"].unique())
femaleper = (femalecount*100)/uniqueplayers
femalepercent = round(femaleper, 2)

otherdata = purchase_data.loc[purchase_data["Gender"]=='Other / Non-Disclosed']
othercount = len(otherdata["SN"].unique())
otherper = (othercount*100)/uniqueplayers
otherpercent = round(otherper, 2)
otherpercent

genderdemog = {"Gender":["Male", "Female", "Other/Non-Disclosed"],
              "Total Count":[malecount, femalecount, othercount],
              "Percentage of Players":[malepercent, femalepercent, otherpercent]}

genderdf = pd.DataFrame(genderdemog)
genderdf


# In[6]:


female_ds = purchase_data.loc[purchase_data["Gender"]=='Female']
male_ds = purchase_data.loc[purchase_data["Gender"]=='Male']
other_ds = purchase_data.loc[purchase_data["Gender"]=='Other / Non-Disclosed']
total_count = len(purchase_data["Purchase ID"])

femalepurcount = len(female_ds)
femaleavgpur = round(female_ds["Price"].mean(), 2)
femaletotpur = round(female_ds["Price"].sum(), 2)
femaleavgtotpp = round(femaletotpur/uniqueplayers, 2)

malepurcount = len(male_ds)
maleavgpur = round(male_ds["Price"].mean(), 2)
maletotpur = round(male_ds["Price"].sum(), 2)
maleavgtotpp = round(maletotpur/uniqueplayers, 2)

otherpurcount = len(other_ds)
otheravgpur = round(other_ds["Price"].mean(), 2)
othertotpur = round(other_ds["Price"].sum(), 2)
otheravgtotpp = round(othertotpur/uniqueplayers, 2)

genderpuranalysis = {"Gender":["Male", "Female", "Other/Non-Disclosed"],
                    "Purchase Count":[femalepurcount,malepurcount,otherpurcount],
                    "Avg Purchase Price":[femaleavgpur, maleavgpur, otheravgpur],
                    "Total Purchase Value":[femaletotpur, maletotpur, othertotpur],
                    "Avg Total Purchase per Person":[femaleavgtotpp, maleavgtotpp, otheravgtotpp]}

gpa_df = pd.DataFrame(genderpuranalysis)
gpa_df


# In[7]:


print("Minimum Age: "+ str(min(purchase_data["Age"])))
print("Maximum Age: "+str(max(purchase_data["Age"])))
agebins = [0, 9, 14, 19, 24, 29, 34, 39, 45]
labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
arange = pd.cut(purchase_data["Age"], bins=agebins, labels=labels)
purchase_data['Age Range'] = arange
arangedf = purchase_data
totalplayers = len(arangedf["SN"].unique())

#datasets for each Age Range
age10ds = arangedf.loc[arangedf["Age Range"]=="<10"]
age15ds = arangedf.loc[arangedf["Age Range"]=="10-14"]
age20ds = arangedf.loc[arangedf["Age Range"]=="15-19"]
age25ds = arangedf.loc[arangedf["Age Range"]=="20-24"]
age30ds = arangedf.loc[arangedf["Age Range"]=="25-29"]
age35ds = arangedf.loc[arangedf["Age Range"]=="30-34"]
age40ds = arangedf.loc[arangedf["Age Range"]=="35-39"]
age45ds = arangedf.loc[arangedf["Age Range"]=="40+"]

#count of unique players by each age group
age10players = len(age10ds["SN"].unique())
age15players = len(age15ds["SN"].unique())
age20players = len(age20ds["SN"].unique())
age25players = len(age25ds["SN"].unique())
age30players = len(age30ds["SN"].unique())
age35players = len(age35ds["SN"].unique())
age40players = len(age40ds["SN"].unique())
age45players = len(age45ds["SN"].unique())               
total_cnt = [age10players, age15players, age20players, age25players, age30players, age35players, age40players, age45players]

#Percentage of each player group by age
age10per = round(age10players*100/totalplayers, 2)
age15per = round(age15players*100/totalplayers, 2)
age20per = round(age20players*100/totalplayers, 2)
age25per = round(age25players*100/totalplayers, 2)
age30per = round(age30players*100/totalplayers, 2)
age35per = round(age35players*100/totalplayers, 2)
age40per = round(age40players*100/totalplayers, 2)
age45per = round(age45players*100/totalplayers, 2)
per_play = [age10per, age15per, age20per, age25per, age30per, age35per, age40per, age45per]
per_play

agedf = {"Age Range":["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"],
        "Total Count":total_cnt,
        "Percentage of Players":per_play
        }
ageanalysis = pd.DataFrame(agedf)
ageanalysis


# In[8]:


spender_stats = purchase_data.groupby("SN")

purchase_count_spender = spender_stats["Purchase ID"].count()
avg_purchase_price_spender = spender_stats["Price"].mean()
purchase_total_spender = spender_stats["Price"].sum()

top_spenders = pd.DataFrame({"Purchase Count": purchase_count_spender,
                             "Average Purchase Price": avg_purchase_price_spender,
                             "Total Purchase Value":purchase_total_spender})

format_spenders = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()

format_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                                 "Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})


# In[9]:


items = purchase_data[["Item ID", "Item Name", "Price"]]

item_stats = items.groupby(["Item ID","Item Name"])
purchase_count_item = item_stats["Price"].count()
purchase_value = (item_stats["Price"].sum()) 

item_price = purchase_value/purchase_count_item

most_popular_items = pd.DataFrame({"Purchase Count": purchase_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":purchase_value})

popular_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()

popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})


# In[10]:


popular_formatted = most_popular_items.sort_values(["Total Purchase Value"],
                                                   ascending=False).head()
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})


# In[ ]:




