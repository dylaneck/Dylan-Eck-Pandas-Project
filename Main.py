###########################
#Dylan Eck
#CPSC 222, Fall 2021
#Data Assignment #3
#I did not attempt the bonus
#This program reads in 2 different csv files, then prompts a user for a section of the data and a column, then calculates summary stats for this column and section
#This then merges the 2 files and sorts them by day of week, then takes the mean of the user selected column and prints both of these to csv files
#############################

import math
import numpy as np
import pandas as pd

youtube_df = pd.read_csv("youtube_analytics.csv", index_col="Date")
#Reads csv to a pandas dataframe and assigns index column
days_df = pd.read_csv("days_of_week.csv", index_col="Date")
#Reads csv to a pandas dataframe and assigns index column

print("Enter a start date:")
start = input()
#Prompts user for start date and assigns to variable

print("Enter an end date:")
end = input()
#Prompts user for end date and assigns to variable

new_yt_df = youtube_df[start:end]
#Creates new data frame including the start and end dates inputed by user
print(new_yt_df)

print("Enter one of the column names: Date, Views, Average percentage viewed (%), Unique viewers, Subscribers, Watch time (hours), Average view duration, Shares, Likes, Dislikes, Comments added, Impressions, Impressions click-through rate (%)")
col = input()
#Prompts user for column

new_df = new_yt_df[col]
#Creates new data frame with user input
print(new_df)

print()
print("Sum:", new_df.sum())
print("Mean:", new_df.mean())
print("Standard Deviation:", new_df.std())
print("Median:", new_df.median())
print("Maximum:", new_df.max())
print("Minimum:", new_df.min())
#Calculates and prints summary stats

merged_df = days_df.merge(youtube_df, on="Date")
#Merges the 2 data frames
merged_df.to_csv("merged.csv")
#Printes merged data frames to a CSV file

grouped_by_day = merged_df.groupby("Day of Week")
#Creates seperate groups by day of week
mean_info = grouped_by_day[col].mean()
#Finds mean for each day based off of user entered column
mean_info.to_csv("means.csv")
#Prints results to csv
#The youtube account seems to be the most active from Monday to Wednesday, and least on Friday and Saturday
