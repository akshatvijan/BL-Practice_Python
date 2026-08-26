import requests

def fetch_page(url):
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()

        return {
            "url":url,
            "status_code":response.status_code,
            "content":response.text
        }
    except requests.exceptions.Timeout:
        return {
            "url":url,
            "error":"timeout error"
        }
    except requests.exceptions.HTTPError:
        return {
            "url":url,
            "status_code":response.status_code,
            "error":"HTTP error"
        }

    except requests.exceptions.ConnectionError:
        return {
            "url":url,
            "error":"connection failure error"

        }
# lever_url = "https://jobs.lever.co/entrata/661bbcc5-3514-4ba3-b616-8838da6c53ec"

# ashby_url = "https://jobs.ashbyhq.com/CUBE/a67dcd6a-4309-49d7-9d1e-2d3f8ea91324"

# smartrecruiters_url = "https://jobs.smartrecruiters.com/smartrecruiters/744000114676597-senior-software-engineer-python"


# print(fetch_page(lever_url))
# print(fetch_page(ashby_url))
# print(fetch_page(smartrecruiters_url))