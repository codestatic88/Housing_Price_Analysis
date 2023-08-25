'''
ONE MAP POPULATION LANGUAGE LITERACY

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API retrieves data related to language literacy for given planning area name and year.

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
        no_literate = response_dictionary["no_literate"]
        l1_chi = response_dictionary["l1_chi"]
        
        l1_eng = response_dictionary["l1_eng"]
        l1_mal = response_dictionary["l1_mal"]
        l1_tam = response_dictionary["l1_tam"]
        
        l1_non_off = response_dictionary["l1_non_off"]
        l2_eng_chi = response_dictionary["l2_eng_chi"]
        l2_eng_mal = response_dictionary["l2_eng_mal"] 
        
        l2_eng_tam = response_dictionary["l2_eng_tam"]
        l2_other_two = response_dictionary["l2_other_two"]
        l3_eng_chi_mal = response_dictionary["l3_eng_chi_mal"] 
        
        l3_eng_mal_tam = response_dictionary["l3_eng_mal_tam"]
        l3_other_three = response_dictionary["l3_other_three"]
        year = response_dictionary["year"] 
        
        l2_eng_non_off = response_dictionary["l2_eng_non_off"]        
       
                

       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'no_literate': no_literate
               , 'l1_chi': l1_chi
                    
               , 'l1_eng': l1_eng
               , 'l1_mal': l1_mal
               , 'l1_tam': l1_tam
                    
               , 'l1_non_off': l1_non_off
               , 'l2_eng_chi':l2_eng_chi
               , 'l2_eng_mal': l2_eng_mal      
 
               , 'l2_eng_tam': l2_eng_tam
               , 'l2_other_two':l2_other_two
               , 'l3_eng_chi_mal': l3_eng_chi_mal
 
               , 'l3_eng_mal_tam': l3_eng_mal_tam
               , 'l3_other_three':l3_other_three
               , 'year': year     
                    
               , 'l2_eng_non_off': l2_eng_non_off 
                   
                
               }             
   


        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves data related to language literacy for given planning area name and year.")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getLanguageLiterate" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=['planning_area', 'no_literate','l1_chi'
                                                    ,"l1_eng",'l1_mal',"l1_tam"
                                                    ,"l1_non_off","l2_eng_chi","l2_eng_mal"
                                                    , "l2_eng_tam", "l2_other_two", "l3_eng_chi_mal"
                                                    , "l3_eng_mal_tam", "l3_other_three"
                                                    ,"year", "l2_eng_non_off"])          


       
 
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_df = retrieve_info(custom_url, authorisation_string)

                combined_df = pd.concat([combined_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_language_literacy"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()