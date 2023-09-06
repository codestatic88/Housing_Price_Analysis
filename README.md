PROJECT OVERVIEW
=====================================================================================================================================
1) BACKGROUND
 When Singapore first gained indepedence in 1965 housing was one of the challenges faced. The living conditions of Singaporeans where dominated by kampongs and haphazardly constructed squtter housings with deplorable living conditions. [1]. An example of the dangers of staying in Kampong houses can be exemplified by the Bukit Ho Swee Fire 
that broke out in 1961 which destroyed 16,000 homes and took 4 lives. [2]
In 1960, Housing and Development Board (HDB) was established. [3]. Public housing in Singapore focuses on considerations of universal homeownership as an overarching principle.
This is a shift from the public housing inheritied from the British Colonial administration which was oriented to having public housing at an affordable rent. In the late 
1960s the HDB policy has shifted towards selling public housing and by 1980s, homeownership has grown [4]
In recent years 2022, Singapore homeownership was at 89.3 percent which has increased from the previous years. Home ownership continues to play a part in the life of 
Singaporeans and property prices in Singapore has increased over the years.

This project takes into account information one map and resale flat prices to better understand what are the features that are related to the modeling of housing price

2) PROBLEM STATEMENT
Modelling to understand how does the factors cause the HDB prices to fluctuate and recommendations for the purchase of HDB
Analysis will also be done across town to better understand how the resale flat feature changes by town such as floor area. Findings will also be done to find out how the prices 
changes across the year. 

3) MODEL EVAULATION CRITERIA
Model will be evaluated using the Root Mean Squared Error.

The Model with the best performing RMSE score will be selected. The model fit will be evaluated to analyse if Underfitting or Overfitting of model occurs.


DATA EXTRACTION
=====================================================================================================================================
1) DATA EXTRACTION
# RESALE FLAT INFO AND PRICE
## DOWNLOAD RESALE PRICE DATASETS
- Resale flat price information is downloaded from the webpage: https://beta.data.gov.sg/datasets/189/view
= The following csv files has been downloaded from the webpage.
- The downloaded files are placed under ("assets/resale_flat" folder)
	1. ResaleFlatPricesBasedonApprovalDate19901999.csv
	2. ResaleFlatPricesBasedonApprovalDate2000Feb2012.csv
	3. ResaleFlatPricesBasedonRegistrationDateFromMar2012toDec2014.csv
	4. ResaleFlatPricesBasedonRegistrationDateFromJan2015toDec2016.csv
	5. ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv

## CONCATENATE RESALE FLAT PRICE AND ADD IN LATITUDE AND LONGITUDE DATA FROM ONEMAP
- Files (in "code" folder):
	1. 2_Data_Extraction_(resale_flat_lat_long).ipynb
- Datasets across the years are concatenated into a dataframe
- Uses Onemap api to retrieve "Latitude" and "Longitude" data base an the address given.

--------------------------------------------------------------------------------------------------------------------------------------
# SCRIPTS OVERVIEW
# DATA EXTRACTION FROM ONEMAP
- OneMap information is retrieved from the website: https://www.onemap.gov.sg/apidocs/apidocs

## [ONE MAP: PLANNING AREA]
## ONE MAP PLANNING AREA POLYGON
- Data contains planning area polygons of Singapore for the year 1998, 2008, 2014 and 2019.
- Data extracted is exported to csv file and pickle file with the columns.
	1. planning_area e.g. Bedok.
	2. longitude
	3. latitude
	4. year
- Files(in "scripts" folder):
	1. om_planning_area_polygon.py: Script for pulling out data for One Map planning area polygon.

- Files(in "assets/onemap" folder):
	1. planning_area_polygons.csv
	2. planning_area_polygons.pkl

## ONE MAP PLANNING AREA ID 
- Data contains names of all planning area and id in Singapore for the year 1998, 2008, 2014 and 2019.
- Data extracted is exported to csv file and pickle file with the columns.
	1. planning_area_id
	2. planning_area
	3. year
- Files(in "scripts" folder):
	1. om_planning_area_id.py: Script for pulling out data for One planning area names and id
- Files(in "assets/onemap" folder):
	1. planning_area_id.csv
	2. planning_area_id.pkl
	
## ONE MAP PLANNING AREA QUERY
- API retrieve planning area based on latitude and longitude.
- Data extracted is export to csv file with the columns:
	1. month
	2. town 
	3. longitude 
	4. latitude 
	5. planning_query_town
- Files(in "scripts" folder):
	1. om_planning_area_query.py: Script for pulling out planning area town based on query of latitude and longitude.
- Files(in "assets/onemap" folder):
	1. planning_area_query.csv
	
	
## [ONE MAP: POPULATION QUERY]

## ONE MAP ECONOMIC STATUS
- API retrieves data related to economic status for given planning area name, year and gender. 
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data is exported to csv file with the columns:
	1. planning_area
	2. employed
	3. unemployed
	4. inactive
	5. year
	6. gender

- Files(in "scripts" folder):
	1. om_population_economic_status.py: Script for getting population economic status based on planning area, year and gender. 
- Files(in "assets/onemap" folder):
	1. population_economic_status.csv
	2. population_economic_status.pkl

## ONE MAP EDUCATION STATUS
- API retrieves data related to economic status for given planning area name and year. 
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. pre_primary 
	3. primary 
	4. secondary 
	5. post_secondary
	6. polytechnic
	7. prof_qualification_diploma
	8. university
	9. year
- Files(in "scripts" folder):
	1. om_population_education_status.py: Script for getting population education status based on planning area and year. 
- Files(in "assets/onemap" folder):
	1. population_education_status.csv
	2. population_education_status.pkl
	
## ONE MAP ETHNIC STATUS
- API retrieves data related to ethnic distribution for given planning area name and year for the specified gender.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. chinese
	3. malays
	4. indian
	5. others
	6. year
	7. gender
- Files(in "scripts" folder):
	1. om_population_ethnic_status.py: Script for getting population ethnic status based on planning area,year and gender. 
- Files(in "assets/onemap" folder):
	1. population_ethnic_status.csv
	2. population_ethnic_status.pkl
	
## WORK INCOME FOR HOUSEHOLD (MONTHLY)
- API retrieves data related monthly household income for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. total
	3. below_sgd_1000
	4. no_working_person
	5. sgd_10000_over
	6. sgd_10000_to_10999
	7. sgd_11000_to_11999
	8. sgd_1000_to_1999
	9. sgd_12000_to_12999
	10. sgd_13000_to_13999
	11. sgd_14000_to_14999
	12. sgd_15000_to_17499
	13. sgd_17500_to_19999
	14. sgd_20000_over
	15. sgd_2000_to_2999
	16. sgd_3000_to_3999
	17. sgd_4000_to_4999
	18. sgd_5000_to_5999
	19. sgd_6000_to_6999
	20. sgd_7000_to_7999
	21. sgd_8000_over
	22. sgd_8000_to_8999
	23. sgd_9000_to_9999
	24. year

- Files(in "scripts" folder):
	1. om_population_household_mthly_income_status.py: Script for getting population household monthly work income based on planning area and year. 
- Files(in "assets/onemap" folder):
	1. population_household_monthly_income_status.csv
	2. population_household_monthly_income_status.pkl
	
## POPULATION HOUSEHOLD STRUCTURE
- API retrieves data related to household structure for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. no_family_nucleus
	3. ofn_1_gen
	4. ofn_2_gen
	5. ofn_3_more_gen
	6. tfn_1to2_gen
	7. tfn_3_more_gen
	8. three_more_fam_nucleus
	9. year
- Files(in "scripts" folder):
	1. om_population_household_structure.py: Script for getting population household structure information based on planning area and year. 
- Files(in "assets/onemap" folder):
	1. population_household_structure.csv
	2. population_household_structure.pkl	

## POPULATION INCOME FROM WORK DATA
- API retrieves data related income from work data for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. total
	3. below_sgd_1000
	4. sgd_10000_to_10999
	5. sgd_11000_to_11999
	6. sgd_12000_over
	7. sgd_1000_to_1499
	8. sgd_1500_to_1999
	9. sgd_2000_to_2499
	10. sgd_2500_to_2999
	11. sgd_3000_to_3999
	12. sgd_4000_to_4999
	13. sgd_5000_to_5999
	14. sgd_6000_over
	15. sgd_6000_to_6999
	16. sgd_7000_to_7999
	17. sgd_8000_over
	18. sgd_8000_to_8999
	19. sgd_9000_to_9999
	20. sgd_1000_to_1999
	21. sgd_2000_to_2999
	22. sgd_12000_14999
	23. sgd_15000_over
	24. year
	
- Files(in "scripts" folder):
	1. om_population_income_from_work.py: Script for getting population income from work data based on planning area and year. 
- Files(in "assets/onemap" folder):
	1. population_income_from_work.csv
	2. population_income_from_work.pkl	
	
## POPULATION PLANNING AREA INDUSTRY
- API retrieves data related to industry of population for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. manufacturing
	3. construction
	4. wholesale_retail_trade
	5. transportation_storage
	6. accommodation_food_services
	7. information_communications
	8. financial_insurance_services
	9. real_estate_services
	10. professional_services
	11. admin_support_services
	12. public_admin_education
	13. health_social_services
	14. arts_entertainment_recreation
	15. other_comm_social_personal
	16. others
	17. hotels_restaurants
	18. transport_communications
	19. business_services
	20. other_services_industries
	21. year

- Files(in "scripts" folder):
	1. om_population_planning_area_industry.py: Script for getting industry of population for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_planning_area_industry.csv
	2. population_planning_area_industry.pkl

### POPULATION LANGUAGE LITERACY 
- API retrieves data related to language literacy for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. no_literate
	3. l1_chi
	4. l1_eng
	5. l1_mal
	6. l1_tam
	7. l1_non_off
	8. l2_eng_chi
	9. l2_eng_mal
	10. l2_eng_tam
	11. l2_other_two
	12. l3_eng_chi_mal
	13. l3_eng_mal_tam
	14. l3_other_three
	15. year
	16. l2_eng_non_off
	
- Files(in "scripts" folder):
	1. om_population_language_literacy.py: Script for getting data related to language literacy for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_language_literacy.csv
	2. population_language_literacy.pkl
	
	
# POPULATION MARTIAL STATUS
- API retrieves data related to marital status for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. single
	3. married
	4. widowed
	5. divorced
	6. year
	7. gender
- Files(in "scripts" folder):
	1. om_population_marital_status.py: Script for getting data related to marital status for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_martial_status.csv
	2. population_martial_status.pkl
	
# POPULATION TRANSPORT MODE TO SCHOOL
- API data related to mode of transport to school for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. bus
	3. mrt
	4. mrt_bus
	5. mrt_car
	6. mrt_other
	7. taxi
	8. car
	9. pvt_chartered_bus
	10. lorry_pickup
	11. motorcycle_scooter
	12. others
	13. no_transport_required
	14. other_combi_mrt_or_bus
	15. mrt_lrt_only
	16. mrt_lrt_and_bus
	17. other_combi_mrt_lrt_or_bus
	18. taxi_pvt_hire_car_only
	19. pvt_chartered_bus_van
	20. year

- Files(in "scripts" folder):
	1. om_population_transport_mode_school.py: Script for getting data related to marital status for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_transport_mode_school.csv
	2. population_transport_mode_school.pkl

# POPULATION TRANSPORT MODE TO WORK
- API retrieve data related to mode of transport to work for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. bus
	3. mrt
	4. mrt_bus
	5. mrt_car
	6. mrt_other
	7. taxi
	8. car
	9. pvt_chartered_bus
	10. lorry_pickup
	11. motorcycle_scooter
	12. others
	13. no_transport_required
	14. other_combi_mrt_or_bus
	15. mrt_lrt_only
	16. mrt_lrt_and_bus
	17. other_combi_mrt_lrt_or_bus
	18. taxi_pvt_hire_car_only
	19. pvt_chartered_bus_van
	20. year

- Files(in "scripts" folder):
	1. om_population_transport_mode_work.py: Script for getting data related to marital status for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_transport_mode_work.csv
	2. population_transport_mode_work.pkl
	
# POPULATION AGE GROUP
- API retrieves data related to age group for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. age_0_4
	3. age_5_9
	4. age_10_14
	5. age_15_19
	6. age_20_24
	7. age_25_29
	8. age_30_34
	9. age_35_39
	10. age_40_44
	11. age_45_49
	12. age_50_54
	13. age_55_59
	14. age_60_64
	15. age_65_69
	16. age_70_74
	17. age_75_79
	18. age_80_84
	19. age_85_over
	20. total
	21. gender
	22. year

- Files(in "scripts" folder):
	1. om_population_age_group.py: Script for getting data related to age group for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_age_group.csv
	2. population_age_group.pkl
	
# POPULATION RELIGION
- API retrieves data related to religion for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. no_religion
	3. buddhism
	4. taoism
	5. islam
	6. hinduism
	7. sikhism
	8. catholic_christian
	9. other_christians
	10. other_religions
	11. year
	
- Files(in "scripts" folder):
	1. om_population_religion.py: Script for getting data related to religion for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_religion.csv
	2. population_religion.pkl	

# POPULATION SPOKEN LANGUAGE
- API retrieves data related to spoken language for given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. english
	3. mandarin
	4. chinese_dialects
	5. malay
	6. tamil
	7. other_indian_languages
	8. others
	9. eng_mand
	10. eng_chn_dlt
	11. eng_mly
	12. eng_oth_ind_lang
	13. eng_oth_lang
	14. mand_eng
	15. mand_chn_dlt
	16. mand_oth_lang
	17. chn_dlt_eng
	18. chn_dlt_mand
	19. chn_dlt_oth_lang
	20. mly_eng
	21. mly_oth_lang
	22. tml_eng
	23. tml_oth_lang
	24. oth_ind_lang_eng
	25. oth_ind_lang_oth_lang
	26. oth_lang_eng
	27. oth_lang_oth_non_eng_lang
	28. eng_tml
	29. year

- Files(in "scripts" folder):`
	1. om_population_spoken_language.py: Script for getting data related to spoken language for given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_spoken_language.csv
	2. population_spoken_language.pkl	
	
# POPULATION TENANCY
- API retrieves data related to tenancy for the given planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. owner
	3. tenant
	4. others
	5. year

- Files(in "scripts" folder):
	1. om_population_tenancy.py: Script for getting data related to tenancy for the given planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_tenancy.csv
	2. population_tenancy.pkl	
	
# POPULATION DWELLING TYPE HOUSEHOLD DATA
- API retrieves data related to dwelling type household for given the planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. hdb_1_and_2_room_flats
	3. hdb_3_room_flats
	4. hdb_4_room_flats
	5. hdb_5_room_and_executive_flats
	6. condominiums_and_other_apartments
	7. landed_properties
	8. others
	9. year
	10. total_hdb

- Files(in "scripts" folder):
	1. om_population_dwelling_type_household.py: Script for getting data related to dwelling type household for given the planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_dwelling_type_household.csv
	2. population_dwelling_type_household.pkl	
	

# POPULATION DWELLLING TYPE POPULATION DATA
- API retrieves data related to dwelling type population for given the planning area name and year.
- Data is available for the year 2000, 2010, 2015, and 2020.
- Data extracted is exported to csv file with the columns:
	1. planning_area
	2. year
	3. hdb_1_and_2_room_flats
	4. hdb_3_room_flats
	5 hdb_4_room_flats
	6. hdb_5_room_and_executive_flats
	7. condominiums_and_other_apartments
	8. landed_properties
	9. others
	10. total_hdb
	11. total

- Files(in "scripts" folder):
	1. om_population_dwelling_type_population.py: Script for getting data related to dwelling type population for given the planning area name and year. 
- Files(in "assets/onemap" folder):
	1. population_dwelling_type_population.csv
	2. population_dwelling_type_population.pkl	
	
	
CONCLUSION
=====================================================================================================================================
1) Overall Analysis
- Observed that in modelling the data, there are neglible changes between the RMSE Train and RMSE Test Score.
- The data has a high number of features. This results in high variance and low biasesness. The data is less likely to be overfitted.
- This is also in in the r2 score which shows that both Train and Test has similar school, indicated that the data is not overfitted.

2) Conclusion and Recommendation
- After modelling and doing analysis on the data, it is concluded that the current amount of data is insufficient to model accurately with low RMSE score. 
- The dataset used has multiple features and several insights can be derived such as:
    - Overall resale flat price has increased across the years.
    - Pasir Ris has larger flats followed by Woodlands and Choa Chu Kang. Should floor size be of priority. These areas can be considered when purchasing a flat.
    - Resale flat size has overall increase between 1990 to 2000. After 2000, the size of resale flat has not increase drastically and fluctuates above 95sqm
	
3) Model Limitation and Next Steps
- Current features are insufficient to model the data to a higher RMSE score
- Next Step:
    - Create a new price column to take into account inflation across the years.
    - Retrieve Latitude and Longitude on places of interest. Distance can be calculate between the resale flat and places of interest to be used for analysis.
    - Further Analysis and get insights from the features such as education, religion, population literacy, spoken language
    - Explore different models such as Prophet and Time Series Analysis.
