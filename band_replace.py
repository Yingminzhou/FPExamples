__author__ = 'yingminzhou'

bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def format_bands(bands):
    for band in bands:
        band['country'] = 'Canada'
        band['name'] = band['name'].replace('.', ' ')
        band['name'] = band['name'].title()


# format_bands(bands)
# print(bands)


def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d


'''
def set_canada_as_country(band):
    return assoc(band,'country','Canada')

def strip_punctuation_from_name(band):
    return assoc(band,'name',band['name'].replace(',',' '))

def capitalize_names(band):
    return assoc(band,'name',band['name'].title)
'''


def call(fn, key):
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))

    return apply_fn


set_canada_as_country = call(lambda x: 'Canada', 'country')
strip_punctuation_from_name = call(lambda x: x.replace(',', ' '), 'name')
capitalize_names = call(lambda x: x.title(), 'name')


def pipeline_each(data, fns):
    from functools import reduce
    return list(reduce(lambda a, x: map(x, a), fns, data))


# print(pipeline_each(bands,[set_canada_as_country,strip_punctuation_from_name,capitalize_names]))

'''
def extract_name_and_country(band):
    plucked_band = {}
    plucked_band['name'] = band['name']
    plucked_band['country'] = band['country']
    return plucked_band
'''


# print(pipeline_each(bands,[set_canada_as_country,strip_punctuation_from_name,capitalize_names,extract_name_and_country]))

def pluck(keys):
    def pluck_func(record):
        from functools import reduce
        return reduce(lambda a, x: assoc(a, x, record[x]), keys, {})
    return pluck_func

print(pipeline_each(bands,[set_canada_as_country,strip_punctuation_from_name,capitalize_names,pluck(['name','country'])]))