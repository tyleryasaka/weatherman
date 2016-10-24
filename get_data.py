import python_http_client
import json
from dateutil.parser import parse

def gen_path(year, datatype):
    return '/cdo-web/api/v2/data?datasetid=GHCND&startdate=' + year + '-01-01&enddate=' + year + '-12-31&locationid=CITY:US410014&stationid=GHCND:USW00024229&datatypeid=' + datatype + '&limit=1000'

host = 'http://www.ncdc.noaa.gov'
global_headers = {"token": "xkrKoANfZOSKiQyTEoWtysWzmvcqnyeR"}
attributes = [
    'PGTM',
    'AWND',
    'TMAX',
    'TMIN',
    'WDF2',
    'PRCP'
]
startYear = 2000
endYear = 2012

def attrs_for_year(year):
    records = {}
    for m in range(1, 13):
        records[m] = {}
        for d in range(1, 32):
            records[m][d] = {}
    for attr in attributes:
        path = gen_path(year, attr)
        url = host + path
        client = python_http_client.Client(host=url, request_headers=global_headers)
        response = client.get()
        if response.status_code != 200:
            raise Exception('Got a nasty response')
        json_response = json.loads(response.body)
        for result in json_response['results']:
            date = parse(result['date'])
            records[date.month][date.day][attr] = result['value']
    return records

def write_year(year, weatherdata):
    with open('./rawdata/' + year + '.json', 'w') as outfile:
        json.dump(weatherdata, outfile)

def get_data():
    for year in range(startYear, endYear):
        year = str(year)
        yeardata = attrs_for_year(year)
        write_year(year, yeardata)

get_data()
