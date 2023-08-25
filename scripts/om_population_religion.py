'''
ONE MAP POPULATION RELIGION

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API retrieves data related to religion for given planning area name and year.

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

# Function to retrieve info
def retrieve_info(custom_url, authorisation_string):
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
        no_religion = response_dictionary["no_religion"]
        buddhism = response_dictionary["buddhism"]
        
        taoism = response_dictionary["taoism"]
        islam = response_dictionary["islam"]
        hinduism = response_dictionary["hinduism"]
        
        sikhism = response_dictionary["sikhism"]
        catholic_christian = response_dictionary["catholic_christian"]
        other_christians = response_dictionary["other_christians"] 
        
        other_religions = response_dictionary["other_religions"]
        year = response_dictionary["year"]      
       
                

       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'no_religion': no_religion
               , 'buddhism': buddhism
                    
               , 'taoism': taoism
               , 'islam': islam
               , 'hinduism': hinduism
                    
               , 'sikhism': sikhism
               , 'catholic_christian':catholic_christian
               , 'other_christians': other_christians      
 
               , 'other_religions': other_religions
               , 'year':year                  
                
               }               



        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves data related to religion for given planning area name and year.")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getReligion" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=['planning_area', 'no_religion','buddhism'
                                                    ,"taoism",'islam',"hinduism"
                                                    ,"sikhism","catholic_christian","other_christians"
                                                    , "other_religions", "year"
                                           ])          
   
       
 
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_df = retrieve_info(custom_url, authorisation_string)

                combined_df = pd.concat([combined_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_religion"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()