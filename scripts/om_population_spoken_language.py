'''
ONE MAP POPULATION SPOKEN LANGUAGE

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API retrieves data related to spoken language for given planning area name and year.

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
        english = response_dictionary["english"]
        mandarin = response_dictionary["mandarin"]
        
        chinese_dialects = response_dictionary["chinese_dialects"]
        malay = response_dictionary["malay"]        
        tamil = response_dictionary["tamil"]

        other_indian_languages = response_dictionary["other_indian_languages"]
        others = response_dictionary["others"] 
        eng_mand = response_dictionary["eng_mand"]

        eng_chn_dlt = response_dictionary["eng_chn_dlt"]      
        eng_mly = response_dictionary["eng_mly"]
        eng_oth_ind_lang = response_dictionary["eng_oth_ind_lang"]

        eng_oth_lang = response_dictionary["eng_oth_lang"]      
        mand_eng = response_dictionary["mand_eng"]        
        mand_chn_dlt = response_dictionary["mand_chn_dlt"]

        mand_oth_lang = response_dictionary["mand_oth_lang"]      
        chn_dlt_eng = response_dictionary["chn_dlt_eng"] 
        chn_dlt_mand = response_dictionary["chn_dlt_mand"]

        chn_dlt_oth_lang = response_dictionary["chn_dlt_oth_lang"]      
        mly_eng = response_dictionary["mly_eng"] 
        mly_oth_lang = response_dictionary["mly_oth_lang"]

        tml_eng = response_dictionary["tml_eng"]      
        tml_oth_lang = response_dictionary["tml_oth_lang"]
        oth_ind_lang_eng = response_dictionary["oth_ind_lang_eng"]

        oth_ind_lang_oth_lang = response_dictionary["oth_ind_lang_oth_lang"]  
        oth_lang_eng = response_dictionary["oth_lang_eng"]  
        oth_lang_oth_non_eng_lang = response_dictionary["oth_lang_oth_non_eng_lang"]        
        
        
        eng_tml = response_dictionary["eng_tml"]
        year = response_dictionary["year"]      
   

        

       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'english': english
               , 'mandarin': mandarin
                    
               , 'chinese_dialects': chinese_dialects
               , 'malay': malay                 
               , 'tamil': tamil

               , 'other_indian_languages':other_indian_languages
               , 'others': others
               , 'eng_mand': eng_mand

               , 'eng_chn_dlt':eng_chn_dlt                  
               , 'eng_mly':eng_mly                    
               , 'eng_oth_ind_lang': eng_oth_ind_lang

               , 'eng_oth_lang':eng_oth_lang                  
               , 'mand_eng':mand_eng                     
               , 'mand_chn_dlt': mand_chn_dlt

               , 'mand_oth_lang':mand_oth_lang                  
               , 'chn_dlt_eng':chn_dlt_eng 
               , 'chn_dlt_mand': chn_dlt_mand

               , 'chn_dlt_oth_lang':chn_dlt_oth_lang                  
               , 'mly_eng':mly_eng  
               , 'mly_oth_lang': mly_oth_lang

               , 'tml_eng':tml_eng                  
               , 'tml_oth_lang':tml_oth_lang
               , 'oth_ind_lang_eng': oth_ind_lang_eng

               , 'oth_ind_lang_oth_lang':oth_ind_lang_oth_lang   
               , 'oth_lang_eng': oth_lang_eng
               , 'oth_lang_oth_non_eng_lang':oth_lang_oth_non_eng_lang 
                    
               , 'eng_tml': eng_tml
               , 'year':year               
                    
                                    
               }    

        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves data related to spoken language for given planning area name and year.")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getSpokenAtHome" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=[
                                            'planning_area', 'english','mandarin'
                                            ,"chinese_dialects",'malay',"tamil"
                                            ,"other_indian_languages","others","eng_mand"
                                            ,"eng_chn_dlt", "eng_mly","eng_oth_ind_lang"
                                            ,"eng_oth_lang","mand_eng","mand_chn_dlt"
                                            ,"mand_oth_lang","chn_dlt_eng","chn_dlt_mand" 
                                            ,"chn_dlt_oth_lang","mly_eng","mly_oth_lang"      
                                            ,"tml_eng","tml_oth_lang","oth_ind_lang_eng"
                                            ,"oth_ind_lang_oth_lang","oth_lang_eng","oth_lang_oth_non_eng_lang"  
                                            ,"eng_tml","year"             
                                           ])          
   
 
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_info(custom_url, authorisation_string)
                retrieve_df = retrieve_info(custom_url, authorisation_string)

                combined_df = pd.concat([combined_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_spoken_language"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()