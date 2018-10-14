'''Import statements: DO NOT TOUCH'''
import scipy
import matplotlib
import pyglet
import pandas as pd
import plotly
import re

'''This is the master function that will be called at the end of the project.'''


def parse_file(file_path, desired_columns):
    sf_data = pd.read_csv(filepath_or_buffer=file_path, usecols=desired_columns, low_memory=True)
    sunset_regex = re.compile(".*Sunset.*")
    neighborhood = sf_data["Analysis Neighborhood"]

    sf_data = sf_data[neighborhood.str.match(sunset_regex)]
    print(sf_data)


'''Think of this as your main() method when running the file'''


def parsing_main():

    # Make sure CSV file is in the correct file_path
    file_path = "..\OriginalCSV\Assessor_Historical_Secured_Property_Tax_Rolls.csv"

    desired_columns = ["Parcel Number", "Analysis Neighborhood"]
    parse_file(file_path, desired_columns)


'''The code that's actually run'''
parsing_main()
