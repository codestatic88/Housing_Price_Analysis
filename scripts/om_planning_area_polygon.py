'''
ONE MAP PLANNING AREA POLYGON

- Users will be able to get the list of the 55 planning areas in Singapore delineated by the Urban Redevelopment Authority (URA). This is helpful for users who want to develop geospatial analytics solutions.
- This API retrieves all planning area polygons of Singapore in JSON format. Users could enter specified year to get planning area polygons as accordingly. If not specified, api retrieves polygon results for latest master plan year.
- Optional. If not specified, the latest data will be provided. Else, values available are 1998, 2008, 2014, and 2019.
'''

# Import Libraries
import sys
import pandas as pd

# Append utils folder file path to call function
sys.path.append("../utils")

# Import in function(s) from util
from data_extraction_util import return_authorisation_string, retrieve_response_string, convert_json_str_to_type, export_file_pickle_csv_check
from general_util import print_main_info_divider, print_sub_info_divider

# Function to get response base on year input and retrieve response text. Returns dataframe
def retrieve_planning_area(current_url,authorisation_string,year,planning_area_long_lat_df):
    print(current_url,authorisation_string)
    
    # Retrieve response string
    response_string = retrieve_response_string(current_url,authorisation_string)

    # Convert response string to type
    response_dictionary = convert_json_str_to_type(response_string)    
    


    # Run for loop to retrieve Planning area, Longitude, Latitude
    for i in response_dictionary["SearchResults"]:
        retrieve_planning_area = i['pln_area_n']
        retrieve_geojson = i['geojson']
        if (retrieve_geojson != None):
            retrieve_geojson_dict = convert_json_str_to_type(retrieve_geojson)
            coordinates_list = retrieve_geojson_dict["coordinates"][0][0]
            for i in coordinates_list:
                retrieved_longitude = i[0]
                retrieved_latitude = i[1]
                temp_row = {'planning_area': retrieve_planning_area
                           , 'longitude': retrieved_longitude
                           , 'latitude': retrieved_latitude
                           , 'year': year}
                temp_df = pd.DataFrame([temp_row])
                planning_area_long_lat_df = pd.concat([planning_area_long_lat_df, temp_df], axis=0, ignore_index=True)
        
    # Print Retrieve Dataframe 
    print_main_info_divider()
    print("DATAFRAME BEFORE EXPORT: ",year)
    print("Dataframe Info: \n",planning_area_long_lat_df.info())        
    print_sub_info_divider()
    print("Dataframe First 5 rows \n", planning_area_long_lat_df.head())
    return planning_area_long_lat_df
    


# create main() function
def main():
    print_main_info_divider()
    print("API Retrieves all planning area polygons in JSON Format")
    # run authorisation_string function
    authorisation_string = return_authorisation_string()
    
    # initialised url variable:
    base_url = "https://www.onemap.gov.sg/api/public/popapi/getAllPlanningarea"    
    
    # Set Year_String in list for 1998, 2008, 2014 and 2019
    year_list = ["1998", "2008", "2014", "2019"]  # 


    # Returns response string based on URL
    try:
        # Create an empty DataFrame
        planning_area_long_lat_df = pd.DataFrame(columns=['planning_area', 'longitude','latitude','year'])
        # Loop through the year to get the information
        for year in year_list:
            print_main_info_divider()
            print(f'Retrieving Data for year {year}')
            current_url = base_url + "?" + year
            print(current_url)
            
#             retrieved_df = retrieve_planning_area(current_url,authorisation_string,year,planning_area_long_lat_df)
#             planning_area_long_lat_df = pd.concat([planning_area_long_lat_df, retrieved_df], axis=0, ignore_index=True)

            planning_area_long_lat_df = retrieve_planning_area(current_url,authorisation_string,year,planning_area_long_lat_df)

            
        # Print out information on Joined Dataset    
        print_main_info_divider()
        print("JOINED DATAFRAME BEFORE EXPORT: ")
        print("Dataframe Info: \n",planning_area_long_lat_df.info())        
        print_sub_info_divider()
        print("Dataframe First 5 rows \n", planning_area_long_lat_df.head())
        
        # Export Joined Dataset and Reimport to Check
        export_filepath = "../assets/onemap/planning_area_polygons"
        export_file_pickle_csv_check(planning_area_long_lat_df,export_filepath)
       
             
    except:
        print("main: error has occurred")

# call main function
if __name__ == "__main__":
    main()