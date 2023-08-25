'''
File contains functions used for data extraction
'''

# Import in libraries to be used in Function
import logging
import datetime


# Function returns the most recent authorisation string
def return_authorisation_string():
    authorisation_string = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlM2U4NjI0NGFmNDJhODY4MTY2ZjFiNWJhMmZjNDBiMCIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNjkwNjEyNDU3LCJleHAiOjE2OTA4NzE2NTcsIm5iZiI6MTY5MDYxMjQ1NywianRpIjoiR1ZvNTdGcFd6ZnVudkxjeSIsInVzZXJfaWQiOjE5MywiZm9yZXZlciI6ZmFsc2V9.WVyROLSMkDF1hHP3lX1npQ1634l8tOEqPI-35JLijnk"
    print("helloworld")
    return authorisation_string


def helloworld2():
     print("helloworld2")
        
def print_test(printme):
     print(printme,"text to be printed")
        
def loggingtest():
    #logging.basicConfig(filename="../logs/mylogtest.log")
    #create a logger
    logger = logging.getLogger('mylogger')
    #set logger level
    logger.setLevel(logging.INFO)
    #or you can set the following level
    #logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('../logs/mylogtest.log')
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    #write a info message
    logger.info('This is an INFO message')
    print('logging test run start')
    