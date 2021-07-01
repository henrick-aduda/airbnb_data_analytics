#!/usr/bin/env python
# coding: utf-8

# # Identifying most common amenities that give Airbnb hosts a competitive advantage over others in Guateng & Cape Town, South Africa

# This notebook looks into using various Python-based data science libraries in an attempt to 
# identify the most common amenities that give Airbnb hosts a competitive advantage as per host listings in Guateng & Cape Town, South Africa.
# I am going to take the following appproach:
# 1. Problem definition
# 2. Data source description
# 3. Data dictionary 
# 4. Fetching data
# 5. Exploratory analysis
# 5. Data analysis
#     * look at common amenities vs review rating
#     * look at common amenities vs review comments (need to categorize what is positive & negative comment)
#     * If possible gather revenue data from other sources and look at common amenities vs income made by airbnb hosts
# 5. Data visualization and communication 
# 6. Findings 
# 6. Conclusion
# 
# ## 1. Problem definition 
# In a statement,
# >Given airbnb review data can we identify common amenities that give airbnb hosts a competitive advantage over other hosts based on review ratings and review comments.
# 
# ## 2. Data source description 
# The original dataset came from Inside Airbnb web database:
# 
# 1. Cape town dataset link: http://data.insideairbnb.com/south-africa/wc/cape-town/2021-03-25/data/listings.csv.gz
# 2. Gauteng dataset link: http://data.insideairbnb.com/south-africa/gt/gauteng/2021-03-29/data/listings.csv.gz
# 
# ## 3. Data dictionary 
# 
# You can find further information about each of the columns in our dataframe by following this link: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=982310896

# ## 4. Fetching data 
# The airbnb dataset for cape town was downloaded from previously shown link. I then moved the csv file from downloads to my data project directory.

# In[36]:


# Importing airbnb data from Gauteng,SA into notebook
import pandas as pd
listings_Guateng = pd.read_csv("data/listings_Guateng.csv", low_memory=False)
listings_Guateng.head()


# In[37]:


# Importing airbnb data for Capetown, SA into notebook 
listings_cape_town = pd.read_csv("data/listings_cape_town.csv", low_memory=False)
listings_cape_town.head()


# ## 5. Exploratory analysis
# ### 1. Gauteng 
# Performed exploratory analysis for airbnb data from Gauteng

# In[4]:


# Checking data types
listings_Guateng.dtypes


# In[5]:


# check shape of data
listings_Guateng.shape


# In[45]:


# Check general summary of statistics
listings_Guateng.describe()


# In[6]:


type(listings_Guateng.amenities)


# In[7]:


# trying to estimate the most common amenities from the pandas series data 
listings_Guateng.amenities.value_counts()


# **Arbitrary common amenities for exploratory analysis**
# 
# I had to come up with top 10 arbitrary common amenities to explore. Based on a rough visual look at the value count `listings_Guateng.amenities.value_counts()`. For now these may be worth looking at as possible common amenities :
# * Long terms stays allowed
# * Air conditioning 
# * TV
# * Cable TV
# * Essentials 
# * Breakfast
# * Wifi
# * Free parking on premises 
# * Hot tub 
# * Luggage dropoff allowed
# 
# **Note:** This is just exploratory analysis for now. In future I would want to really pick up on the amenities that appear the most instead of estimating

# In[8]:


# Counting the number of times long terms stays and other amenities appear from review data
long_term_guateng = listings_Guateng.amenities.str.contains(r'Long term stays allowed').sum()
long_term_guateng = int(long_term_guateng) # converting to integer for easy downstream analysis
type(long_term_guateng)
long_term_guateng


# In[9]:


# Counting number of times air conditioning appears
air_con_guateng = listings_Guateng.amenities.str.contains(r'Air conditioning').sum()
air_con_guateng = int(air_con_guateng)
air_con_guateng


# In[10]:


# counting number of times tv appears
tv_guateng = listings_Guateng.amenities.str.contains(r'TV').sum()
tv_guateng = int(tv_guateng)
tv_guateng


# In[12]:


# Counting number of times cable tv appears
cable_tv_guateng = listings_Guateng.amenities.str.contains(r'Cable TV').sum()
cable_tv_guateng = int(cable_tv_guateng)


# In[15]:


# Counting number of times essentials appears
essentials_guateng = listings_Guateng.amenities.str.contains(r'Essentials').sum()
essentials_guateng = int(essentials_guateng)


# In[16]:


# Counting number of times breakfast appears
breakfast_guateng = listings_Guateng.amenities.str.contains(r'Breakfast').sum()
breakfast_guateng = int(breakfast_guateng)


# In[17]:


# Counting number of times Free parking appears
free_parking_guateng = listings_Guateng.amenities.str.contains(r'Free parking on premises').sum()
free_parking_guateng = int(free_parking_guateng)


# In[18]:


# Counting number of times hot tub appears
hot_tub_guateng = listings_Guateng.amenities.str.contains(r'Hot tub').sum()
hot_tub_guateng = int(hot_tub_guateng)


# In[19]:


# Counting number of times luggage dropoff appears
luggage_drop_guateng = listings_Guateng.amenities.str.contains(r'Luggage dropoff allowed').sum()
luggage_drop_guateng = int(luggage_drop_guateng)


# In[46]:


# Visualizing data for common amenities in airbnbs in Guateng, SA
import matplotlib.pyplot as plt # Import relevant libraries
#we want our plot to appear inside the notebook
get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.pyplot.bar(x = ["Long term allowed", "air conditioning", "TV",
                           "Cable TV","Essentials", "Breakfast",
                           "Free parking", "Hot tub",
                          "Luggage drop"],
                      height = [long_term_guateng,air_con_guateng, tv_guateng, cable_tv_guateng, essentials_guateng,
                          breakfast_guateng, free_parking_guateng,hot_tub_guateng,luggage_drop_guateng]);
plt.xticks(rotation=90)
plt.xlabel("Amenities")
plt.ylabel("Frequency of amenities in listings")
plt.title("Airbnb Common amenities in Gauteng, South Africa", fontweight="bold", fontsize=13);


# The above plot shows that most common amenities listed by airbnb hosts in Guateng are: Long term stays allowed, TV, Essentials and Free parking.
# 
# As per an airbnb blog post (https://news.airbnb.com/amenities-do-matter-airbnb-reveals-which-amenities-guests-search-for-most/), most people prefer comfort over connectivity. Survey data indicated that a large number of people in the US (59%), Australia (46%) and Italy (39%) prefer air conditioning as an important indoor amenities over internet/wifi and full kitchens.
# 
# Our brief exploratory analysis shows that air conditioning, cable tv, breakfast and hot tub are the least common amenities placed by airbnb hosts. It therfore seems that there is a gap. Most clients would prefer to have amenities that provide comfort but the airbnb host amenities listings from Guateng indicate a different story. Amenities that would most likely provide comfort like air conditioning and hot tub are the least common amenities

# ### 2. Cape Town
# Next I went ahead to look at most common amenities in airbnb listings in Capetown, South Africa. I also want to generate a third plot that compares frequency of amenities in capetown vs amenities in guateng. Is the trend the same for both cities in terms of frequency of common amenities? 

# #### Amenities to choose?
# I chose similar  amenities used for exploring Guateng data. As follows:
# * Long terms stays allowed
# * Air conditioning 
# * TV
# * Cable TV
# * Essentials 
# * Breakfast
# * Wifi
# * Free parking on premises 
# * Hot tub 
# * Luggage dropoff allowed

# In[39]:


# Check data types
listings_cape_town.dtypes


# In[43]:


# Check summary of statistics
listings_cape_town.describe()


# In[42]:


# check shape of data
listings_cape_town.shape


# In[23]:


# Counting the number of times long terms stays and other amenities appear from review data
long_term_cape = listings_cape_town.amenities.str.contains(r'Long term stays allowed').sum()
long_term_cape = int(long_term_cape) # converting to integer for easy downstream analysis
type(long_term_cape)
long_term_cape


# In[24]:


# Counting the number of times air conditioning appears from review data
air_con_cape = listings_cape_town.amenities.str.contains(r'Air conditioning').sum()
air_con_cape = int(air_con_cape) # converting to integer for easy downstream analysis
air_con_cape


# In[26]:


# Counting the number of times TV appears on review data (amenities column)
tv_cape = listings_cape_town.amenities.str.contains(r'TV').sum()
tv_cape = int(tv_cape)
tv_cape


# In[27]:


# Counting the number of times Cable TV appears on review data (amenities column)
cable_tv_cape = listings_cape_town.amenities.str.contains(r'Cable TV').sum()
cable_tv_cape = int(cable_tv_cape)
cable_tv_cape


# In[28]:


# Counting the number of times Essential appears on the review data
essentials_cape = listings_cape_town.amenities.str.contains(r'Essentials').sum()
essentials_cape = int(essentials_cape)
essentials_cape


# In[29]:


# Counting the number of times Breakfast appears on the review data
breakfast_cape = listings_cape_town.amenities.str.contains(r'Breakfast').sum()
breakfast_cape = int(breakfast_cape)
breakfast_cape


# In[30]:


# Counting number of times Free parking appears
free_parking_cape = listings_cape_town.amenities.str.contains(r'Free parking on premises').sum()
free_parking_cape= int(free_parking_cape)
free_parking_cape


# In[31]:


# Counting number of times hot tub appears
hot_tub_cape = listings_cape_town.amenities.str.contains(r'Hot tub').sum()
hot_tub_cape = int(hot_tub_cape)
hot_tub_cape


# In[32]:


# Counting number of times luggage dropoff appears
luggage_drop_cape = listings_cape_town.amenities.str.contains(r'Luggage dropoff allowed').sum()
luggage_drop_cape = int(luggage_drop_cape)
luggage_drop_cape


# In[47]:


# Visualizing data for common amenities in airbnbs in Cape town, SA
import matplotlib.pyplot  # Import relevant libraries
matplotlib.pyplot.bar(x = ["Long term stays allowed", "air conditioning", "TV",
                           "Cable TV","Essentials", "Breakfast",
                           "Free parking", "Hot tub",
                          "Luggage drop"],
                      height = [long_term_cape,air_con_cape, tv_cape, cable_tv_cape, essentials_cape,
                          breakfast_cape, free_parking_cape,hot_tub_cape,luggage_drop_cape]);
# Adding labels, ticks and titles for more information
plt.xticks(rotation=90)
plt.xlabel("Amenities", fontweight="bold")
plt.ylabel("Frequency of amenities in listings", fontweight="bold")
plt.title("Airbnb Common amenities in Cape Town, South Africa", fontweight="bold", fontsize=13);


# The above plot shows that most common amenities listed by airbnb hosts in Cape town are: Long term stays allowed, TV, Essentials and Free parking. 
# 
# As per an airbnb blog post (https://news.airbnb.com/amenities-do-matter-airbnb-reveals-which-amenities-guests-search-for-most/), most people prefer comfort over connectivity. Survey data indicated that a large number of people in the US (59%), Australia (46%) and Italy (39%) prefer air conditioning as an important indoor amenities over internet/wifi and full kitchens.
# 
# Our brief exploratory analysis shows that air conditioning, cable tv, breakfast and hot tub are the least common amenities placed by airbnb hosts. It therfore seems that there is a gap. Most clients would prefer to have amenities that provide comfort but the airbnb host amenities listings from Guateng indicate a different story. Amenities that would most likely provide comfort like air conditioning are the least common amenities. 

# ### Comparing common amenities in Gauteng vs Capetown South Africa

# In[48]:


# Import relevant libraries
import matplotlib.pyplot as plt
import numpy as np
# setting x axis
labels =["Long term stays allowed", "air conditioning", "TV", "Cable TV","Essentials", "Breakfast",
        "Free parking", "Hot tub", "Luggage drop off"]
# y axis (contains frequency of amenities in airbnb listings)
cape_town =[long_term_cape,air_con_cape, tv_cape, cable_tv_cape, essentials_cape,breakfast_cape,
             free_parking_cape,hot_tub_cape,luggage_drop_cape]
guateng =[long_term_guateng,air_con_guateng, tv_guateng, cable_tv_guateng, essentials_guateng,
               breakfast_guateng,free_parking_guateng,hot_tub_guateng,luggage_drop_guateng]

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, cape_town, width, label='Cape_town', color="lightblue")
rects2 = ax.bar(x + width/2, guateng , width, label='Guateng', color ="salmon")

# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Frequency of amenities in listings')
ax.set_xlabel('Common amenities')
ax.set_title('Airbnb Common amenities in Cape Town & Guateng, South Africa',fontweight="bold", fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.xticks(rotation=90)
figsize=(10,6)

plt.show();


# The above plot shows a comparison of common amenities in Cape town and Gauteng, South Africa. There seems to be a similar trend in frequency of common amenities in listings in both cities. The most common amenities in both cities are : Long term stays allowed, TV, Essentials and Free parking. I also noted that generally Cape Town seems to have more occurences of amenities than Gauteng i.e **Cape town has more amenities popping up accross the listings data than Guateng.** I thought perhaps this could be attributed to the population of the cities. My hypothesis was: **cities that have a larger population most likely have more airbnb hosts listings than cities with small populations.** However that was not the case. As per statistics from https://worldpopulationreview.com/world-cities , Guateng has a population of 5,926,668 while Cape town has a population of 4,709,990 as of 2021. The most likely reason may be the average income of individuals (purchasing power). This requires further research. However due to time constraints I did not analyse this further.
# 
# **Conclusion**
# 
# Generally it seems that amenities that would most likely provide comfort (breakfast, hot tub, air conditioning) are the least common among airbnb host listings data in both cities.

# ## 6. Data analysis
# Yet to be conducted:
#  * look at common amenities vs review rating
#  * look at common amenities vs review comments (need to categorize what is positive &   negative comment)
#  * If possible gather revenue data from other sources and look at common amenities vs income made by airbnb hosts

# ## 7. Data visualization and communication
# Yet to be conducted 
# ## 8. Findings 
# Yet to be conducted 
# ## 9. Conclusion
# Yet to be conducted
