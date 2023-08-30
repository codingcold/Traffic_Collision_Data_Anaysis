# Traffic_Collision_Data_Anaysis
Description: For Homework 5, I get 3 datasets from the internet, including dataset1 which is scraped from the internet, dataset2 which is through reverse geocoding using Python and dataset3 which is downloaded from the website. I import sys to apply the command line, import beautifulsoup and pandas to read the website and csv files, import urllib to download csv files through links, import opencage to geocode and import re to search the zip code in the address.I installed packages including Beautiful Soup, geopandas, pandas and requests

Data sources:
Dataset1 about la traffic collision
It is scraped from the website(https://www.splitgraph.com/lacity/traffic-collision-data-from-2010-to-present-d5tf-ez2w). I read the source code through the requests and beautifulsoup and get the csv file download link so that I can use urllib  library to open the link and get the file. The data I need to use from the dataset is the victim age, the latitudes and longitudes which I can get the address and zip codes from. After that I can form a csv file called “raw_data.csv” to collect the data. I use 2000 rows of the csv because the api has rate limits every day.

Dataset 2 about zipcodes use opencage to reverse geocode(https://towardsdatascience.com/reverse-geocoding-in-python-a915acf29eb6) so that I can get the address. I use re to search the zipcodes in the address. The address and corresponding zip codes are used to form a new csv called “zip_data.csv”.

Dataset 3 
It is about the population in Los Angeles by zip codes downloaded from the website(https://data.lacity.org/Community-Economic-Development/2010-Census-Populations-by-Zip-Code/nxs9-385f). And according to the csv formed in the dataset2 processing, I get a new column corresponding to the zipcodes where the traffic collision happened. I also counted the frequency of the zipcodes shown in the traffic collision data and zip codes’ responding population number.  The new csv is called “frequency.csv''. 

Library to install:

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from opencage.geocoder import OpenCageGeocode
import bs4
from bs4 import BeautifulSoup
import requests
import csv
import seaborn as sns
import urllib

Running the code:
I have two .py files, but we just need to run the data_analysis.py
In command line, type in $python data_analysis.py and the there will be output images and counting results shown in the shell.
The results include images and texts showing Number of collisions through time, location of collisions, collisions by age group, collisions by time of day, pearson correlation and OLS regression results.

