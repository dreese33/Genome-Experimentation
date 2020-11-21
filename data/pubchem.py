# Uses pubchem api to get NCBI datasets
import requests

base_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/'

def find_compound_cid(compound):
    url_extension = 'compound/name/' + compound + '/cids/TXT'
    endpoint = base_url + url_extension
    try:
        r = requests.get(endpoint)
        cid = r.text.strip()
        return cid
    except Exception as exc:
        print('An exception occurred in find_compound_cid')
        return -1


def compound_information_cid(cid):
    url_extension = 'compound/cid/' + cid + '/assaysummary/XML'
    endpoint = base_url + url_extension
    try:
        r = requests.get(endpoint)
        return r.text
    except Exception as exc:
        print('An exception occurred in search_compound_cid')
        return -1


def compound_information(compound):
    print('Getting compound cid')
    cid = find_compound_cid(compound)
    if cid == -1:
        return -1
    return compound_information_cid(cid)
