'''
ONE MAP PLANNING AREA ID

- This API retrieves the names of all planning areas and id in Singapore for given year in JSON format.
- Users could enter specified year to get planning area polygons as accordingly. If not specified, api retrieves polygon results for latest master plan year.
- Optional. If not specified, the latest data will be provided. Else, values available are 1998, 2008, 2014, and 2019.
'''
# Import Libraries
import sys
import pandas as pd

# Append utils folder file path to call function
sys.path.append("../utils")

# Import in function(s) from util
from data_extraction_util import return_authorisation_string, retrieve_response_string, convert_json_str_to_type, export_file_pickle_csv_check
from general_util import print_main_info_divider, print_sub_info_divider

# retrieve planning area with id
def retrieve_planning_area_id(current_url,authorisation_string,year,planning_area_id_df):
    # Retrieve response string
    response_string = retrieve_response_string(current_url,authorisation_string)

    # Convert response string to type
    response_dictionary = convert_json_str_to_type(response_string)   
    
   
    # loop through dictionary to extract information
    for value in response_dictionary:

        temp_id = value['id']
        temp_planning_area = value['pln_area_n'] 
        print("exit for loop",temp_id,temp_planning_area)
        if(temp_planning_area != 'TOTAL'):
            temp_row = {'planning_area_id':temp_id
                        ,'planning_area':temp_planning_area
                        , 'year': year}           
            temp_df = pd.DataFrame([temp_row])
            planning_area_id_df = pd.concat([planning_area_id_df, temp_df], axis=0, ignore_index=True)
    
    # Print Retrieve Dataframe 
    print_main_info_divider()
    print("DATAFRAME BEFORE EXPORT: ",year)
    print("Dataframe Info: \n",planning_area_id_df.info())        
    print_sub_info_divider()
    print("Dataframe First 5 rows \n", planning_area_id_df.head())            
    return planning_area_id_df


# create main() function
def main():
    print_main_info_divider()
    print("API Retrieves all planning area and id in JSON Format")
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

        
    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getPlanningareaNames"   
    
    # Set Year_String in list for 1998, 2008, 2014 and 2019
    year_list = ["1998", "2008", "2014", "2019"]  #  

    # Returns response string based on URL
    try:
        # Create an empty DataFrame
        planning_area_id_df = pd.DataFrame(columns=['planning_area_id', 'planning_area','year'])
        
        # Loop through the year to get the information
        for year in year_list:
            print_main_info_divider()
            print(f'Retrieving Data for year {year}')
            current_url = base_url + "?" + year
            print(current_url)
            
            planning_area_id_df = retrieve_planning_area_id(current_url,authorisation_string,year,planning_area_id_df)
            
#             retrieved_df = retrieve_planning_area_id(current_url,authorisation_string,year,planning_area_id_df)
#             planning_area_id_df = pd.concat([planning_area_id_df, retrieved_df], axis=0, ignore_index=True)
            
            

        # Print out information on Joined Dataset    
        print_main_info_divider()
        print("JOINED DATAFRAME BEFORE EXPORT: ")
        print("Dataframe Info: \n",planning_area_id_df.info())        
        print_sub_info_divider()
        print("Dataframe First 5 rows \n", planning_area_id_df.head())
        
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/planning_area_id"
        export_file_pickle_csv_check(planning_area_id_df,export_filepath)
             
    except:
        print("main: error has occurred")

# call main function
if __name__ == "__main__":
    main()