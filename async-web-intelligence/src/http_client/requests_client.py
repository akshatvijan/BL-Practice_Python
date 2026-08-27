import requests
Max_retries=3
def fetch_page(url):
    for i in  range(Max_retries):

        try:
            response=requests.get(url,timeout=10)
            response.raise_for_status()

            return {
                "url":url,
                "status_code":response.status_code,
                "content":response.text
            }
        except requests.exceptions.Timeout:
            if i==Max_retries-1:
                return {
                    "url":url,
                    "error":"timeout error"
                }
        except requests.exceptions.HTTPError:
            if 400 <= response.status_code < 500:
                return {
                    "url": url,
                    "status_code": response.status_code,
                    "error": "Client error"
                }

            elif 500 <= response.status_code < 600:
                if i==Max_retries-1:
                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "error": "Server error"
                    }
            else:
                if i==Max_retries-1:
                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "error": "HTTP error"
                    }

        except requests.exceptions.ConnectionError:
            if i==Max_retries-1:                                    
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