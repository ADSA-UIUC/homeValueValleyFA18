'''Import statements: DO NOT TOUCH'''
import scipy
import matplotlib
import pyglet
import pandas as pd
import plotly

'''This is the master function that will be called at the end of the project.'''
def parse_file(file_path, desired_columns):
    data = pd.read_csv(filepath_or_buffer=file_path, usecols=desired_columns, low_memory=True)
    print(data)

'''Think of this as your main() method when running the file'''
def main():
    file_path = "..\OriginalCSV\Assessor_Historical_Secured_Property_Tax_Rolls.csv"
    desired_columns = ["Parcel Number", "Analysis Neighborhood"]
    parse_file(file_path, desired_columns)

'''The code that's actually run'''
main()