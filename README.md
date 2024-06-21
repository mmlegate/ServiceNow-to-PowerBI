# ServiceNow to Power BI Data Analysis

This project leverages the Python integration within Power BI to perform an API call to ServiceNow. The code provided is the API call used to pull data from ServiceNow, as well as the preprocessing of the data in order to make the results human-readable. When pasted into Power BI, the result is a data visualization board of key insights from the data pulled from ServiceNow.
For security reasons, the API key used for the project has been redacted.

## Introduction

At my IT job, I realized it was relatively difficult for consultants to get an understanding of the work that they've done. Meanwhile ServiceNow holds a lot of rich data that documents the lifetime and attributes of tickets. If I bridged the gap between these two entities, I would be able to provide consultants with a useful report of their work and productivity while also making use of the data stored in ServiceNow.

## Installation

Instructions on how to set up the project locally.

1. Clone the repository:
    ```bash
    git clone https://github.com/mmlegate/ServiceNow-to-PowBI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ServiceNow-to-PowBI
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

This project cannot be replicated outright for security reasons. I imagine that instances of ServiceNow outside of UW have similar ticket structures and data features, thus by replacing the API key in the .py document you might be able to get something. I definitely recommend running the code outside of Power BI first in order to debug any potential issues.

Helpful Microsoft documentation on utilizing the Python integration in Power BI:
https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-scripts

## Technologies Used

- ServiceNow
- Python
- Power BI
