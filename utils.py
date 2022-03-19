import numpy as np

def fuzzy_search(df, mode, name):
    '''
    Input:
    mode: player/club/country
    name: the name of a player/club/country
    Output: possible names

    Used to find specific parameter for graphing function
    '''
    D = {'player':'Name', 'club':'Club', 'country':'Nationality'}
    mode = D[mode]
    mask = df[mode].notnull()
    list1 = np.array(df[mode][mask].unique()).tolist()
    data = [x for i,x in enumerate(list1) if x.find(name) != -1]

    return(data)   

def condition_search(df, rating_range = [0,100],**kwargs):
    '''
    Search by conditions, return a list of names
    The input arguments must be valid column names and values
    '''
    
    if rating_range[1] > 0:
        df1 = df[(df.Overall >= rating_range[0])&(df.Overall < rating_range[1])]
        
    condition = []

    items = [i for i in kwargs.items()]
    for item in items:
        mask = df1[item[0]]==item[1]
        df1 = df1[mask]
        
    return np.array(df1.Name).tolist()

def extract_mapping():
    # note: the mapping's classification of regions comes from a Chinese Team, so may incur some difference
    mapping = {'England': 'United Kingdom','Scotland': 'United Kingdom','Republic of Ireland': 'United Kingdom',
                'Korea Republic': 'Korea','Wales': 'United Kingdom','China PR': 'China','Czech Republic': 'Czech Rep.',
                'Ivory Coast': "Côte d'Ivoire",'Northern Ireland': 'United Kingdom','Bosnia Herzegovina': 'Bosnia and Herz.',
                'DR Congo': 'Dem. Rep. Congo','Kosovo': 'Serbia','North Macedonia': 'Macedonia',
                'Guinea Bissau': 'Guinea-Bissau','Curacao': 'Curaçao','Equatorial Guinea': 'Eq. Guinea',
                'Antigua & Barbuda': 'Antigua and Barb.','Trinidad & Tobago': 'Trinidad and Tobago',
                'Dominican Republic': 'Dominican Rep.','Faroe Islands': 'Faeroe Is.',
                'Central African Republic': 'Central African Rep.','South Sudan': 'S. Sudan',
                'Korea DPR': 'Dem. Rep. Korea','Chinese Taipei': 'China','Brunei Darussalam': 'Brunei',
                'Aruba': 'Netherlands','Hong Kong': 'China','São Tomé & Príncipe': 'São Tomé and Principe','Macau': 'China'}
    return mapping


