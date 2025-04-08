import requests

def fetch_cves(start_index=0, results_per_page=100):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "startIndex": start_index,
        "resultsPerPage": results_per_page
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    return data
