# Final Project for GEOG5995
## Project Goal

The goal of this project is to analyze crime data in Leeds and its relationship with the Priority Places for Food Index (PPFI).
This GitHub repository contains 

## Repository Contents
This GitHub repository contains the following files:

* Raw Crime Data: Downloaded from data.police.uk.
* merge_data.py: A Python script to merge multiple crime data files into a single dataset.
* Merged Crime Data File: The result of running merge_data.py.
* Lecture Materials Data Files:
  ** ppfi_index_v2_nov2023.csv
  ** Leeds.geojson
* Analysis Result Files: Two PNG files showing analysis results.
* Final Project Notebook: A .ipynb file for performing the data merge, cleaning, joining, and analysis.

## Instructions

The .ipynb file is designed to run in a Google Colab environment. If you are using a different environment, please modify the file reading sections and address any Python library installation issues as needed.

## Analysis Overview

The final project notebook performs the following tasks:
1. Data Merge/Cleaning and Join: Combines and prepares the data for analysis.
2. Spearman Correlation Analysis: Examines the correlation between crime data and the PPFI in Leeds.
3. K-Cluster Mapping Model: Utilizes clustering techniques to analyze the spatial relationship between crime data and the PPFI in Leeds.
