'''
ONE MAP POPULATION DWELLING TYPE HOUSEHOLD

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API retrieves data related to dwelling type household for given the planning area name and year.

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
        hdb_1_and_2_room_flats = response_dictionary["hdb_1_and_2_room_flats"]
        hdb_3_room_flats = response_dictionary["hdb_3_room_flats"]        
        hdb_4_room_flats = response_dictionary["hdb_4_room_flats"]
        hdb_5_room_and_executive_flats = response_dictionary["hdb_5_room_and_executive_flats"]     
        condominiums_and_other_apartments = response_dictionary["condominiums_and_other_apartments"]
        landed_properties = response_dictionary["landed_properties"]
        others = response_dictionary["others"]
        year = response_dictionary["year"]
        total_hdb = response_dictionary["total_hdb"]
        

       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'hdb_1_and_2_room_flats': hdb_1_and_2_room_flats
               , 'hdb_3_room_flats': hdb_3_room_flats                    
               , 'hdb_4_room_flats': hdb_4_room_flats
               , 'hdb_5_room_and_executive_flats': hdb_5_room_and_executive_flats
               , 'condominiums_and_other_apartments': condominiums_and_other_apartments
               , 'landed_properties': landed_properties
               , 'others': others
               , 'year': year
               , 'total_hdb': total_hdb                                    
               }       
    
    
        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves data related to dwelling type household for given planning area name and year.")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getTypeOfDwellingHousehold" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=[
                                            'planning_area', 'hdb_1_and_2_room_flats','hdb_3_room_flats'
                                            ,"hdb_4_room_flats",'hdb_5_room_and_executive_flats'  
                                            ,'condominiums_and_other_apartments','landed_properties'
                                            ,'others','year','total_hdb'
                                           ])          
    

    
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_info(custom_url, authorisation_string)
                retrieve_df = retrieve_info(custom_url, authorisation_string)

                combined_df = pd.concat([combined_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_dwelling_type_household"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()