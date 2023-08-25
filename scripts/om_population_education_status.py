'''
ONE MAP POPULATION EDUCATION STATUS

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API retrieves data related to education status for given planning area name and year.

The data is available for the years 2000, 2010, 2015, and 2020.
'''

# Import Libraries
import sys
import pandas as pd

# Append utils folder file path to call function
sys.path.append("../utils")

# Import in function(s) from util
from data_extraction_util import return_authorisation_string, retrieve_response_string, convert_json_str_to_type, retrieve_unique_df_columns,export_file_pickle_csv_check
from general_util import print_main_info_divider, print_sub_info_divider

# Function to retrieve education status

def retrieve_education_status(custom_url, authorisation_string):
    # Retrieve response string
    response_string = retrieve_response_string(custom_url,authorisation_string)
    
    # Convert response string to type
    response_retrieve = convert_json_str_to_type(response_string)
    
    print("response_retrieve",response_retrieve)
    
    if isinstance(response_retrieve, list):
        # Retrieve Dictionary:
        response_dictionary = response_retrieve[0]
        
        print("response_dictionary",response_dictionary)
        
        # Retrieve Variables from Dictionary:
        planning_area = response_dictionary["planning_area"]
        pre_primary = response_dictionary["pre_primary"]
        primary = response_dictionary["primary"]
        secondary = response_dictionary["secondary"]
        post_secondary = response_dictionary["post_secondary"]
        polytechnic = response_dictionary["polytechnic"]
        prof_qualification_diploma = response_dictionary["prof_qualification_diploma"]
        university = response_dictionary["university"]
        year = response_dictionary["year"]
        
        
       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'pre_primary': pre_primary
               , 'primary': primary
               , 'secondary': secondary
               , 'post_secondary': post_secondary
               , 'polytechnic': polytechnic
               , 'prof_qualification_diploma': prof_qualification_diploma
               , 'university':university
               , 'year': year}
        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves education status by planning area and year")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getEducationAttending" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        education_status_df = pd.DataFrame(columns=['planning_area', 'pre_primary','primary',"secondary",'post_secondary',"polytechnic"
                                                   ,"prof_qualification_diploma","university","year"])
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_df = retrieve_education_status(custom_url, authorisation_string)

                education_status_df = pd.concat([education_status_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_education_status"
        export_file_pickle_csv_check(education_status_df,export_filepath)
        
        print("COMPLETE:", education_status_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()