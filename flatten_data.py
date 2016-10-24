import json

attrs = [
    'PGTM',
    'AWND',
    'TMAX',
    # 'WDF2',
    'PRCP'
]

use_seasons = False

seasons = {
    '1': [1, 2, 3],
    '2': [4, 5, 6],
    '3': [7, 8, 9],
    '4': [10, 11, 12]
}

def get_classification(num_month):
    if(use_seasons):
        for s, season in seasons.iteritems():
            if int(num_month) in season:
                return int(s)
    else:
        return int(num_month)

def flatten_year(year):
    filename = './rawdata/' + year + '.json'
    with open(filename) as data_file:
        yeardata = json.load(data_file)
    flattened = []
    for m, month in yeardata.iteritems():
        for d, day in month.iteritems():
            item = {}
            item['features'] = []
            for f, feature in day.iteritems():
                if (f in attrs):
                    item['features'].append(feature)
            item['classification'] = get_classification(m)
            if(len(item['features']) == len(attrs)):
                flattened.append(item)
    return flattened

def write_flattened(weatherdata, filename):
    with open('./flatteneddata/' + filename + '.json', 'w') as outfile:
        json.dump(weatherdata, outfile)

def flatten_data(filename, startYear, endYear):
    alldata = []
    for year in range(startYear, endYear):
        year = str(year)
        flattened = flatten_year(year)
        alldata.extend(flattened)
    print len(alldata), 'items'
    write_flattened(alldata, filename)

flatten_data('2000-2010', 2000, 2011)

flatten_data('2011', 2011, 2012)
