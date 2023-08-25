'''
ONE MAP POPULATION PLANNING AREA INDUSTRY

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API retrieves data related to industry of population for given planning area name and year.

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
        manufacturing = response_dictionary["manufacturing"]
        construction = response_dictionary["construction"]
        
        wholesale_retail_trade = response_dictionary["wholesale_retail_trade"]
        transportation_storage = response_dictionary["transportation_storage"]
        accommodation_food_services = response_dictionary["accommodation_food_services"]
        
        information_communications = response_dictionary["information_communications"]
        financial_insurance_services = response_dictionary["financial_insurance_services"]
        real_estate_services = response_dictionary["real_estate_services"] 
        
        professional_services = response_dictionary["professional_services"]
        admin_support_services = response_dictionary["admin_support_services"]
        public_admin_education = response_dictionary["public_admin_education"] 
        
        health_social_services = response_dictionary["health_social_services"]
        arts_entertainment_recreation = response_dictionary["arts_entertainment_recreation"]
        other_comm_social_personal = response_dictionary["other_comm_social_personal"] 
        
        others = response_dictionary["others"]
        hotels_restaurants = response_dictionary["hotels_restaurants"]
        transport_communications = response_dictionary["transport_communications"] 
 
        business_services = response_dictionary["business_services"]
        other_services_industries = response_dictionary["other_services_industries"]
        year = response_dictionary["year"] 
        
       
                

       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'manufacturing': manufacturing
               , 'construction': construction
                    
               , 'wholesale_retail_trade': wholesale_retail_trade
               , 'transportation_storage': transportation_storage
               , 'accommodation_food_services': accommodation_food_services
                    
               , 'information_communications': information_communications
               , 'financial_insurance_services':financial_insurance_services
               , 'real_estate_services': real_estate_services      
 
               , 'professional_services': professional_services
               , 'admin_support_services':admin_support_services
               , 'public_admin_education': public_admin_education
 
               , 'health_social_services': health_social_services
               , 'arts_entertainment_recreation':arts_entertainment_recreation
               , 'other_comm_social_personal': other_comm_social_personal     
                    
               , 'others': others
               , 'hotels_restaurants':hotels_restaurants
               , 'transport_communications': transport_communications 

               , 'business_services': business_services
               , 'other_services_industries':other_services_industries
               , 'year': year        
                   
                
               }             
        


        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves data related to industry of population for given planning area name and year")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getIndustry" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=['planning_area', 'manufacturing','construction'
                                                    ,"wholesale_retail_trade",'transportation_storage',"accommodation_food_services"
                                                    ,"information_communications","financial_insurance_services","real_estate_services"
                                                    , "professional_services", "admin_support_services", "public_admin_education"
                                                    , "health_social_services", "arts_entertainment_recreation"
                                                    ,"other_comm_social_personal"
                                                    , "others", "hotels_restaurants", "transport_communications"
                                                    , "business_services", "other_services_industries","year"])        
        

     
       
 
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_df = retrieve_info(custom_url, authorisation_string)

                combined_df = pd.concat([combined_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_planning_area_industry"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()