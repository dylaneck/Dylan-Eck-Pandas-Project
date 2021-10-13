import math
import numpy as np
import pandas as pd
def open_csv():
    youtube_df = pd.read_csv("youtube_analytics.csv", index_col="Date")
    #Reads csv to a pandas dataframe and assigns index column
    days_df = pd.read_csv("days_of_week.csv", index_col="Date")
    #Reads csv to a pandas dataframe and assigns index column

    return youtube_df, days_df


def slice_data(youtube_df):
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

    return new_df, col


def calculate_sum_stats(new_df):
    print()
    print("Sum:", new_df.sum())
    print("Mean:", new_df.mean())
    print("Standard Deviation:", new_df.std())
    print("Median:", new_df.median())
    print("Maximum:", new_df.max())
    print("Minimum:", new_df.min())
    #Calculates and prints summary stats


def merge_tables(youtube_df, days_df):
    merged_df = days_df.merge(youtube_df, on="Date")
    #Merges the 2 data frames
    merged_df.to_csv("merged.csv")
    #Printes merged data frames to a CSV file
    return merged_df


def means_by_day(merged_df, col):
    grouped_by_day = merged_df.groupby("Day of Week")
    #Creates seperate groups by day of week
    mean_info = grouped_by_day[col].mean()
    #Finds mean for each day based off of user entered column
    mean_info.to_csv("means.csv")
    #Prints results to csv
    #The youtube account seems to be the most active from Monday to Wednesday, and least on Friday and Saturday
