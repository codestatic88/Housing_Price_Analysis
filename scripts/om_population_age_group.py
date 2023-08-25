'''
ONE MAP POPULATION AGE DATA

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

API retrieves data related to age group for given planning area name and year. If gender is not specified, then result set would contain figures for both genders, male and female.

For the purpose of the project, gender will be specified for both male and female.

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

# Function to return info.
def retrieve_info(current_url, authorisation_string):
    # Retrieve response string
    response_string = retrieve_response_string(current_url,authorisation_string)
    
       
    print("CURRENT_URL",current_url) 
    # Convert response string to type
    response_retrieve = convert_json_str_to_type(response_string)
    
    # Check that response string has data
    if isinstance(response_retrieve, list):
        print("List Proceed")
        response_dictionary = response_retrieve[0]
        # Retrieve variables from dictionary
        planning_area = response_dictionary["planning_area"]
        age_0_4 = response_dictionary["age_0_4"]
        age_5_9 = response_dictionary["age_5_9"]
        age_10_14 = response_dictionary["age_10_14"]
        age_15_19 = response_dictionary["age_15_19"]
        age_20_24 = response_dictionary["age_20_24"]        
        age_25_29 = response_dictionary["age_25_29"]
        
        age_30_34 = response_dictionary["age_30_34"]
        age_35_39 = response_dictionary["age_35_39"]        
        age_40_44 = response_dictionary["age_40_44"]
        
        age_45_49 = response_dictionary["age_45_49"]
        age_50_54 = response_dictionary["age_50_54"]        
        age_55_59 = response_dictionary["age_55_59"] 
        
        age_60_64 = response_dictionary["age_60_64"]
        age_65_69 = response_dictionary["age_65_69"]        
        age_70_74 = response_dictionary["age_70_74"]  
        
        age_75_79 = response_dictionary["age_75_79"]
        age_80_84 = response_dictionary["age_80_84"]        
        age_85_over = response_dictionary["age_85_over"]   
        
        total = response_dictionary["total"]
        gender = response_dictionary["gender"]        
        year = response_dictionary["year"]
        
        # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'age_0_4': age_0_4
               , 'age_5_9': age_5_9
               , 'age_10_14': age_10_14
               , 'age_15_19': age_15_19
               , 'age_20_24': age_20_24                    
               , 'age_25_29': age_25_29
 
               , 'age_15_19': age_15_19
               , 'age_20_24': age_20_24                    
               , 'age_25_29': age_25_29
                    
               , 'age_30_34': age_30_34
               , 'age_35_39': age_35_39                    
               , 'age_40_44': age_40_44     
                    
               , 'age_45_49': age_45_49
               , 'age_50_54': age_50_54                    
               , 'age_55_59': age_55_59   
                    
               , 'age_60_64': age_60_64
               , 'age_65_69': age_65_69                    
               , 'age_70_74': age_70_74    
                    
               , 'age_75_79': age_75_79
               , 'age_80_84': age_80_84                    
               , 'age_85_over': age_85_over  
                    
               , 'total': total
               , 'gender': gender                    
               , 'year': year                      
                    
               }
        temp_df = pd.DataFrame([temp_row])

        
        
        return temp_df 
        
    else:
        print("no data retrieved")
     
    


def main():
    print_main_info_divider()
    print("API Retrieves population age data by planning area with separate column for gender")
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getPopulationAgeGroup" # ?planningArea=Bedok&year=2010&gender=male   
    print("code run ok")
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
   
    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=['planning_area', 'age_0_4','age_5_9',"age_10_14",'age_15_19','age_20_24',"age_25_29"
                                            ,"age_30_34","age_35_39","age_40_44","age_45_49","age_50_54","age_55_59","age_60_64"
                                            ,"age_65_69","age_70_74","age_75_79","age_80_84","age_85_over","total","gender"
                                            , "year"
                                           ])
        
        
 
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                custom_url_female = custom_url + "&gender=female"
                custom_url_male = custom_url + "&gender=male"   

        #     print(custom_url)
                # Retrieve information by year, area and gender as female to concatenate
                retrieve_status_female_df = retrieve_info(custom_url_female, authorisation_string)
                combined_df = pd.concat([combined_df, retrieve_status_female_df], axis=0, ignore_index=True)
                
                # Retrieve information by year, area and gender as male to concatenate
                rerieve_status_male_df = retrieve_info(custom_url_male, authorisation_string)
                combined_df = pd.concat([combined_df, rerieve_status_male_df], axis=0, ignore_index=True)


        #     print(type(planning_area_unique))
        
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_age_group"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
    

        
    except:
        print("main: error has occurred")
# call main function
if __name__ == "__main__":
    main()
    
 