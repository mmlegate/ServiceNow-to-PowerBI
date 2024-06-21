import numpy as np
import pandas as pd
import datetime
from random import randrange
from datetime import timedelta

# Define dummy parameters
N = 186
initial_ticket = 5212965
final_ticket = 8323864

initial_date = datetime.datetime(2021, 11, 29)
final_date = datetime.datetime(2024, 3, 28)

lms_options = ['Canvas', 'Zoom', 'Panopto', 'Poll Everywhere', 'Other']
task_options = ['REQ', 'INC', 'RTASK']

def random_dates(start, end, N):
    delta = end - start
    rand_date_str = [str(initial_date)]

    for i in range(N-2):
        random_day = randrange(delta.days)
        random_day = start + timedelta(days=random_day)
        rand_date_str.append(str(random_day))
    rand_date_str.append(str(final_date))
    return rand_date_str

tickets_data = {
    'Number':['REQ' + str(i) for i in np.random.randint(initial_ticket, final_ticket, N)],
    'LMS':[lms_options[i] for i in np.random.randint(0, 5, N)],
    'Last Modified':[random_dates(initial_date, final_date, N)],
    'Task Type':[task_options[i] for i in np.random.randint(0, 3, N)]
}

# Convert dictionary to dataframe
tickets_dataframe = pd.DataFrame.from_dict(tickets_data)

# Dataframe 'Last Modified' column needs to be in timestamp format for Power BI analysis
tickets_dataframe['Last Modified'] = pd.to_datetime(tickets_dataframe['Last Modified'] , errors='ignore')

print(tickets_data)