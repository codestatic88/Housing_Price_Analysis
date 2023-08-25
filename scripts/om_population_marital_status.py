'''
ONE MAP POPULATION MARITAL STATUS

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

API retrieves data related to marital status for given planning area name and year. If gender is not specified, then result set would contain figures for both genders, male and female.

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
        single = response_dictionary["single"]
        married = response_dictionary["married"]
        widowed = response_dictionary["widowed"]
        divorced = response_dictionary["divorced"]
        year = response_dictionary["year"]        
        gender = response_dictionary["gender"]
        
        # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'single': single
               , 'married': married
               , 'widowed': widowed
               , 'divorced': divorced
               , 'year': year                    
               , 'gender': gender}
        temp_df = pd.DataFrame([temp_row])

        return temp_df 
        
    else:
        print("no data retrieved")
     
    


def main():
    print_main_info_divider()
    print("API Retrieves maritial status by planning area with separate column for gender")
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getMaritalStatus" # ?planningArea=Bedok&year=2010&gender=male   
    print("code run ok")
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
#     planning_area_df = pd.read_csv("../assets/onemap/planning_area_id.csv")
#     planning_area_unique = planning_area_df["planning_area"].unique()
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    

    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=['planning_area', 'single','married',"widowed",'divorced','year',"gender"])
        
        
 
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
        export_filepath = "../assets/onemap/population_martial_status"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
    

        
    except:
        print("main: error has occurred")
# call main function
if __name__ == "__main__":
    main()
    
 