'''
Data Extraction Utils contains function used specifically for data extraction
'''
# Import Libraries for function
import  requests
import sys
import json
import pandas as pd

# Append utils folder file path to call function
sys.path.append("../utils")

# Import in function(s) from utils
from general_util import print_main_info_divider, print_sub_info_divider



# Function returns the specifie authorisation string, authorisation string is only valid for 3 days
def return_authorisation_string():
    authorisation_string = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI5MzUwM2I0MmViMzViOTg2Y2ZhMTUyZGQzZTdmMjA1YiIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNjkyMjQ3Mzc0LCJleHAiOjE2OTI1MDY1NzQsIm5iZiI6MTY5MjI0NzM3NCwianRpIjoiR2hkV2N2ejFjOUpLSDh6eCIsInVzZXJfaWQiOjQ3NiwiZm9yZXZlciI6ZmFsc2V9.9UgLXb31F_MRbwKdPgNwrD7ZE90pDYt2GVkHADN2B3k"
    print_main_info_divider()
    print("# FUNCTION return_authorisation_string: Authorisation string has been returned")    
    return authorisation_string


# Function returns the specifie authorisation string, authorisation string is only valid for 3 days
def return_authorisation_string_2():
    authorisation_string = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3OTg2NzQ4YzVmMDlmMjNlNGM2ZjZmZTAxNjY2YmVjOCIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNjkxNjkxMDg2LCJleHAiOjE2OTE5NTAyODYsIm5iZiI6MTY5MTY5MTA4NiwianRpIjoiWjZiUFZzWGw3dnVrcWMwSCIsInVzZXJfaWQiOjM4MiwiZm9yZXZlciI6ZmFsc2V9.057rdaqMDGn348QNwiaRR4ped7dk3XDrjv9V-aSGdP0"
    print_main_info_divider()
    print("# FUNCTION return_authorisation_string: Authorisation string has been returned")    
    return authorisation_string

# convert Json string to type such as dictionary or list
def convert_json_str_to_type(response_str):
    converted_response = json.loads(response_str)
    return converted_response


# Function returns response as a derived string based on URL and authorisation string
def retrieve_response_string(url,authorisation_string):
   
    try:
        print_main_info_divider()
        print(f'# FUNCTION retrieve_response_string\n')
        print("Auhorisation String used",authorisation_string,"\n")        
        headers = {"Authorization": authorisation_string}   
        response = requests.request("GET", url, headers=headers)
        response_str = response.text
        
        print_sub_info_divider()
        print("function retrieve_response_string: \n")
        print(response_str,"\n")
        print_sub_info_divider()
        
        print("Response string has been returned")

        print_main_info_divider()
        
#         url = "https://www.onemap.gov.sg/api/public/popapi/getAllPlanningarea"
      
#         headers = {"Authorization": authorisation_string}
      
#         response = requests.request("GET", url, headers=headers)
        print(response_str)
    except:
        print("Unable to retrieve response string")
        response_str = "NA"
    print_sub_info_divider()
    return response_str

# Function exorts dataframe to pickle and csv file. Function reimports file to check export has been successful and prints out info
def export_file_pickle_csv_check(dataframe,export_filepath):
    print_main_info_divider()
    print(f'FUNCTION export_file_pickle_csv_check')
    
    #instanticate path for csv and pickle
    csv_filepath = export_filepath+".csv"
    pickle_filepath = export_filepath+".pkl"
    
    # export coordinateList to csv
    dataframe.to_csv(csv_filepath, encoding='utf-8', index=False)
    print("file exported to csv")

    # export as pickle file
    dataframe.to_pickle(pickle_filepath)
    print("file export to pickle")
          
    # file reimport check
    print_sub_info_divider()
    print(f'Print file Reimport Check') 
    print(f'CSV file reimport info:')          
    csv_df = pd.read_csv(csv_filepath)
    print(csv_df.info())
          
    print_sub_info_divider()
    print(f'pickle file reimport info:')             
    pickle_df = pd.read_pickle(pickle_filepath)
    print(pickle_df.info())


# Function write text to file
def write_text_file(filename,text):
    file_object = open(filename,'a')
    file_object.write(text+"\n")
    
# Function to update cell of specified column and index
def update_csv_cell(filepath,index,col_name,cell_value):
    # reading the csv file
    df = pd.read_csv(filepath)
    df.loc[index, col_name] = cell_value
    
    # writing into the file
    df.to_csv(filepath, index=False)    
    
    
def retrieve_unique_df_columns(filepath,col_name):
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    df = pd.read_csv("../assets/onemap/planning_area_id.csv")
    unique_col_values = df["planning_area"].unique()
    return unique_col_values