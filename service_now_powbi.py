import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
# Important notes:
    # Power BI Python script cannot contain functions (may change in future)
    # Power BI only identifies pandas dataframes as data
    # Power BI also doesn't accept if and for statements after a dataframe has been generated
    # (it ignores everything after df generation, except built-in df functions)
    
# Define API username and password
username= 'username'
password= 'password'

#Change netID for person you are doing the search for
netid = 'mlegat' 
api_url = 'https://uw.service-now.com/api/now/table/task' # Link to API table where we will extract tasks
query_params = {
    'sysparm_query': '123TEXTQUERY321='+ netid +'^numberNOT LIKEREF',       # Search Service Now for all tasks with Keywords = netid and Number not containing REF
    'sysparm_display_value': 'false',                                       
    'sysparm_exclude_reference_link': 'true',                               # Gets rid of links to Service Now in data results, we don't need them
    'sysparm_fields': 'number, sys_updated_on, sys_class_name, cmdb_ci',    # The data fields we are extracting
    'sysparm_limit': '2000'                                                 # Limit of records to obtain
}
headers = {'X-Api-Name': username}

response = requests.get(api_url, params=query_params, headers=headers, auth=HTTPBasicAuth(username, password))
tickets_data = response.json().get('result', [])

# Convert data in dictionary to different values based off codes below
N = len(tickets_data)
lms_code = [['646d17156f621100328c8bec5d3ee49d', 'Canvas'], ['540eb98a6ff536c41b9f77131c3ee436', 'Zoom'], ['c26d17156f621100328c8bec5d3ee4c5', 'Panopto'], ['5c9e246e6ff9a500bd4906267b3ee429', 'Poll Everywhere']]
type_code = [['requests', 'REQ'], ['incident', 'INC'], ['request_task', 'RTASK'], ['knowledge', 'KB']]

for i in range(N):
    lms_link = str(tickets_data[i]['cmdb_ci'])
    for j in lms_code:
        if j[0] in lms_link:
            tickets_data[i]['cmdb_ci'] = j[1]
            break
        elif j == lms_code[-1]:
            tickets_data[i]['cmdb_ci'] = 'Other'
            
    type_link = str(tickets_data[i]['sys_class_name'])
    for j in type_code:
        if j[0] in type_link:
            tickets_data[i]['sys_class_name'] = j[1]
            break
        elif j == lms_code[-1]:
            tickets_data[i]['sys_class_name'] = 'Other'

# Convert dictionary to dataframe
tickets_dataframe = pd.DataFrame.from_dict(tickets_data)

# Rename columns in dataframe
tickets_dataframe.rename({'number':'Number', 'cmdb_ci':'LMS','sys_updated_on':'Last Modified', 'sys_class_name':'Task Type'}, axis='columns', inplace=True)

# Dataframe 'Last Modified' column needs to be in timestamp format for Power BI analysis
tickets_dataframe['Last Modified'] = pd.to_datetime(tickets_dataframe['Last Modified'] , errors='ignore')

print(tickets_data)