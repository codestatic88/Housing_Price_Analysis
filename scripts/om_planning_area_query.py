# Import Libraries
import sys
import pandas as pd
import csv

# Append utils folder file path to call function
sys.path.append("../utils")

# Import in function(s) from util
from data_extraction_util import return_authorisation_string_2, retrieve_response_string, convert_json_str_to_type, write_text_file, update_csv_cell
from general_util import print_main_info_divider, print_sub_info_divider


# create function to retrieve planning area based on latitude and longitude
def retrieve_planning_area(authorisation_string,latitude,longitude):
    # update url with unique latitude and longitude information
    url = "https://www.onemap.gov.sg/api/public/popapi/getPlanningarea?latitude="+latitude+"&longitude="+longitude

    try:       
        # Retrieve response string
        response_string = retrieve_response_string(url,authorisation_string)
        response_list = convert_json_str_to_type(response_string)   
        planning_area = response_list[0]['pln_area_n']
        print("planning area",planning_area)
        if len(planning_area) > 0:
            return planning_area
        else:
            return None 
    except:
        return None


# create main() function
def main():
    
    # Create a seperate file for the resale price longitude and latitude data and create a separate column for status tracking.
    resale_flat_lat_long_df = pd.read_csv("../assets/resale_flat_gen/resale_long_lat_fmt_only.csv")
    temp_df = resale_flat_lat_long_df.copy()
    # Create a column status to be updated on extraction progress
    temp_df = temp_df.assign(status=None)
    # Export file specifically for the tracking of extraction status for the planning area query.
    temp_df.to_csv('../assets/status_tracker/resale_long_lat_fmt_only_status_om_parea_query.csv', encoding='utf-8', index=False)
    
   
    # Instantiate text file path
    text_filepath = 'om_planning_area_query_write.txt'
#     file_object = open('om_planning_area_query_write.txt','a')
#     file_object.write('hello')
    
    print_main_info_divider()
    print("API Retrieves query planning area based on longitude and latitude")
    # run authorisation_string function
    authorisation_string = return_authorisation_string_2()
    
    try:
        # Instantiate Longitude List
        longitude_list = list(resale_flat_lat_long_df['longitude'])
        latitude_list = list(resale_flat_lat_long_df['latitude'])
        # Instantiate and append list containing latitude and longitude.
        lat_long_list = []
        lat_long_list.append(longitude_list)
        lat_long_list.append(latitude_list)
        
        # Instantiate list
        month_list = list(resale_flat_lat_long_df['month'])
        town_list = list(resale_flat_lat_long_df['town'])
        
        #Initialise counter
        counter = 0
        index = 0
        
        # Initialise data length
        data_length = len(lat_long_list[0])
        print(data_length)
#         write_text_file(text_filepath,'text_to_print')

        # Initialised Update Filepath
        update_filepath = '../assets/status_tracker/resale_long_lat_fmt_only_status_om_parea_query.csv'

        
        for index in range(0,data_length):
            counter += 1
            temp_longitude = str(lat_long_list[0][index])
            temp_latitude = str(lat_long_list[1][index])
            value_retrieved = retrieve_planning_area(authorisation_string,temp_latitude,temp_longitude)
#             # update csv file with status on data extraction
#             update_csv_cell(update_filepath,index,'status','yes')

            
            text = str(value_retrieved) + " retrieved at row " + str(counter) + " out of " + str(data_length) + " rows" 
            write_text_file(text_filepath,text)

            # Data we want to write to the CSV file
            line = [month_list[index], town_list[index],longitude_list[index],latitude_list[index],value_retrieved]

            with open("../assets/onemap/planning_area_query.csv","a", newline="") as infile: 
                # Create a writer object for csv
                writer = csv.writer(infile)
                # Write the row the CSV file.
                # Note that this line updates the file in-place
                writer.writerow(line)
            index += 1

        print_main_info_divider()
        print("Reimport File Check")
        reimport_df = pd.read_csv("../assets/onemap/planning_area_query.csv")
        print(reimport_df.info())
        print_sub_info_divider()
        print(reimport_df.head(10))

    except:
        print("main: error has occurred")
    
    
    
# call main function
if __name__ == "__main__":
    main()