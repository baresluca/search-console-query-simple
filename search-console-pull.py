from googleapiclient import sample_tools
import csv

def get_gsc_data(property_uri, start_date, end_date):
  service, flags = sample_tools.init([property_uri], 'webmasters', 'v3', __doc__, __file__, scope='https://www.googleapis.com/auth/webmasters.readonly')

  request = {
    'startDate': start_date,
    'endDate': end_date,
    'dimensions': ['query'],
    'rowLimit': 5
  }

  response = service.searchanalytics().query(siteUrl=property_uri, body=request).execute()
  
  for row in response['rows']: 
    print(row['keys'], row['clicks'], row['impressions'], row['ctr'], row['position'])

    
gsc_property = "INSERT YOUR WEBSITE HERE"
gsc_start_date = "2020-01-01"
gsc_end_date = "2020-01-01"
get_gsc_data(gsc_property, gsc_start_date, gsc_end_date)




