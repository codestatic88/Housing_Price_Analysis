'''
ONE MAP POPULATION MONTHLY HOUSEHOLD INCOME STATUS

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API retrieves data related monthly household income for given planning area name and year.

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

# Function to retrieve household income status

def retrieve_household_income_status(custom_url, authorisation_string):
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
        total = response_dictionary["total"]
        below_sgd_1000 = response_dictionary["below_sgd_1000"]
        
        no_working_person = response_dictionary["no_working_person"]
        sgd_10000_over = response_dictionary["sgd_10000_over"]
        sgd_10000_to_10999 = response_dictionary["sgd_10000_to_10999"]
        
        sgd_11000_to_11999 = response_dictionary["sgd_11000_to_11999"]
        sgd_1000_to_1999 = response_dictionary["sgd_1000_to_1999"]
        sgd_12000_to_12999 = response_dictionary["sgd_12000_to_12999"] 
        
        sgd_13000_to_13999 = response_dictionary["sgd_13000_to_13999"]
        sgd_14000_to_14999 = response_dictionary["sgd_14000_to_14999"]
        sgd_15000_to_17499 = response_dictionary["sgd_15000_to_17499"]
        
        sgd_17500_to_19999 = response_dictionary["sgd_17500_to_19999"]
        sgd_20000_over = response_dictionary["sgd_20000_over"]
        sgd_2000_to_2999 = response_dictionary["sgd_2000_to_2999"]
        
        sgd_3000_to_3999 = response_dictionary["sgd_3000_to_3999"]
        sgd_4000_to_4999 = response_dictionary["sgd_4000_to_4999"]
        sgd_5000_to_5999 = response_dictionary["sgd_5000_to_5999"]
        
        sgd_6000_to_6999 = response_dictionary["sgd_6000_to_6999"]
        sgd_7000_to_7999 = response_dictionary["sgd_7000_to_7999"]
        sgd_8000_over = response_dictionary["sgd_8000_over"]
        
        sgd_8000_to_8999 = response_dictionary["sgd_8000_to_8999"]
        sgd_9000_to_9999 = response_dictionary["sgd_9000_to_9999"]
        year = response_dictionary["year"]
        
       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'total': total
               , 'below_sgd_1000': below_sgd_1000
                    
               , 'no_working_person': no_working_person
               , 'sgd_10000_over': sgd_10000_over
               , 'sgd_10000_to_10999': sgd_10000_to_10999
                    
               , 'sgd_11000_to_11999': sgd_11000_to_11999
               , 'sgd_1000_to_1999':sgd_1000_to_1999
               , 'sgd_12000_to_12999': sgd_12000_to_12999
                    
               , 'sgd_13000_to_13999':sgd_13000_to_13999
               , 'sgd_14000_to_14999': sgd_14000_to_14999                    
               , 'sgd_15000_to_17499': sgd_15000_to_17499
                    
               , 'sgd_17500_to_19999': sgd_17500_to_19999
               , 'sgd_20000_over': sgd_20000_over                    
               , 'sgd_2000_to_2999': sgd_2000_to_2999
               
               , 'sgd_3000_to_3999': sgd_3000_to_3999
               , 'sgd_4000_to_4999': sgd_4000_to_4999
               , 'sgd_5000_to_5999': sgd_5000_to_5999
                    
               , 'sgd_6000_to_6999': sgd_6000_to_6999
               , 'sgd_7000_to_7999':sgd_7000_to_7999
               , 'sgd_8000_over': sgd_8000_over
                    
               , 'sgd_8000_to_8999': sgd_8000_to_8999
               , 'sgd_9000_to_9999': sgd_9000_to_9999
               , 'year': year}       
        
        

        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves monthly household income by planning area and year")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getHouseholdMonthlyIncomeWork" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        household_mthly_income_df = pd.DataFrame(columns=['planning_area', 'total','below_sgd_1000'
                                                    ,"no_working_person",'sgd_10000_over',"sgd_10000_to_10999"
                                                   ,"sgd_11000_to_11999","sgd_1000_to_1999","sgd_12000_to_12999"
                                                   ,"sgd_13000_to_13999","sgd_14000_to_14999","sgd_15000_to_17499"
                                                   ,"sgd_17500_to_19999","sgd_20000_over","sgd_2000_to_2999"
                                                   ,"sgd_3000_to_3999","sgd_4000_to_4999","sgd_5000_to_5999"
                                                   ,"sgd_6000_to_6999","sgd_7000_to_7999","sgd_8000_over"
                                                   ,"sgd_8000_to_8999","sgd_9000_to_9999","year"])
        
 
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_df = retrieve_household_income_status(custom_url, authorisation_string)

                household_mthly_income_df = pd.concat([household_mthly_income_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_household_monthly_income_status"
        export_file_pickle_csv_check(household_mthly_income_df,export_filepath)
        
        print("COMPLETE:", household_mthly_income_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()