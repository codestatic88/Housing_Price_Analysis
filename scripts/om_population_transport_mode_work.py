'''
ONE MAP POPULATION TRANSPORT MODE TO WORK

API provides population data sets by the Department of Statistics. The types of population demographics data, based on planning area or subzone, include age group, economic status, education status, household size etc

This API data related to mode of transport to work for given planning area name and year.

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
        bus = response_dictionary["bus"]
        mrt = response_dictionary["mrt"]
        
        mrt_bus = response_dictionary["mrt_bus"]
        mrt_car = response_dictionary["mrt_car"]
        mrt_other = response_dictionary["mrt_other"]
        
        taxi = response_dictionary["taxi"]
        car = response_dictionary["car"]
        pvt_chartered_bus = response_dictionary["pvt_chartered_bus"] 
        
        lorry_pickup = response_dictionary["lorry_pickup"]
        motorcycle_scooter = response_dictionary["motorcycle_scooter"]
        others = response_dictionary["others"] 
        
        no_transport_required = response_dictionary["no_transport_required"]
        other_combi_mrt_or_bus = response_dictionary["other_combi_mrt_or_bus"]
        mrt_lrt_only = response_dictionary["mrt_lrt_only"] 
        
        mrt_lrt_and_bus = response_dictionary["mrt_lrt_and_bus"]        
        other_combi_mrt_lrt_or_bus = response_dictionary["other_combi_mrt_lrt_or_bus"] 
        taxi_pvt_hire_car_only = response_dictionary["taxi_pvt_hire_car_only"] 
        
        pvt_chartered_bus_van = response_dictionary["pvt_chartered_bus_van"]         
        year = response_dictionary["year"]         
        

       # Create temporary row for data to be added to dataframe
        temp_row = {'planning_area': planning_area
               , 'bus': bus
               , 'mrt': mrt
                    
               , 'mrt_bus': mrt_bus
               , 'mrt_car': mrt_car
               , 'mrt_other': mrt_other
                    
               , 'taxi': taxi
               , 'car':car
               , 'pvt_chartered_bus': pvt_chartered_bus      
 
               , 'lorry_pickup': lorry_pickup
               , 'motorcycle_scooter':motorcycle_scooter
               , 'others': others
 
               , 'no_transport_required': no_transport_required
               , 'other_combi_mrt_or_bus':other_combi_mrt_or_bus
               , 'mrt_lrt_only': mrt_lrt_only     
                    
               , 'mrt_lrt_and_bus': mrt_lrt_and_bus 
               , 'other_combi_mrt_lrt_or_bus': other_combi_mrt_lrt_or_bus 
               , 'taxi_pvt_hire_car_only': taxi_pvt_hire_car_only    
                    
               , 'pvt_chartered_bus_van': pvt_chartered_bus_van
               , 'year': year                    
               }             
   

        temp_df = pd.DataFrame([temp_row])

        return temp_df     
    
    else: 
        print("no data retrieved")


def main():
    print_main_info_divider()
    print("API Retrieves data related to mode of transport to work for given planning area name and year.")
    
    # run authorisation_string function
    authorisation_string = return_authorisation_string()

    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getModeOfTransportWork" # ?planningArea=Bedok&year=2020  
    
    # Set Year_String in list for "2000", "2010", "2015", "2020"
    year_list = ["2000", "2010", "2015", "2020"]  
    
    # Return unique list of planning area dervied earlier for planning_area_id.csv
    planning_area_unique = retrieve_unique_df_columns("../assets/onemap/planning_area_id.csv","planning_area")
    
    try:
        # Create an empty DataFrame
        combined_df = pd.DataFrame(columns=['planning_area', 'bus','mrt'
                                                    ,"mrt_bus",'mrt_car',"mrt_other"
                                                    ,"taxi","car","pvt_chartered_bus"
                                                    , "lorry_pickup", "motorcycle_scooter", "others"
                                                    , "no_transport_required", "other_combi_mrt_or_bus"
                                                    ,"mrt_lrt_only", "mrt_lrt_and_bus"
                                                    , "other_combi_mrt_lrt_or_bus","taxi_pvt_hire_car_only"
                                                    , "pvt_chartered_bus_van", "year"])          


 
        for area in planning_area_unique:
            for year in year_list:
                custom_url = base_url + "?" + "planningArea=" + area + "&year=" + year 
                print("custom_url",custom_url)
                retrieve_df = retrieve_info(custom_url, authorisation_string)

                combined_df = pd.concat([combined_df, retrieve_df], axis=0, ignore_index=True)
                
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/population_transport_mode_work"
        export_file_pickle_csv_check(combined_df,export_filepath)
        
        print("COMPLETE:", combined_df.info())
        
    except:        
        print("main: error has occurred")
    
if __name__ == "__main__":
    main()