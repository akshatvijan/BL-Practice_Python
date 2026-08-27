import httpx
import asyncio
Max_Retries=3
Max_concurrent=5
semaphore=asyncio.Semaphore(Max_concurrent)
timeout=httpx.Timeout(
    connect=5.0,
    read=10.0,
    write=5.0,
    pool=5.0

)
   


async def async_fetch(url):
    async with semaphore:
        for i in range(Max_Retries):
            try:
                async with httpx.AsyncClient() as client:
                    response=await client.get(url,timeout=timeout)
                    response.raise_for_status()

                    return {
                        "url":url,
                        "status_code":response.status_code,
                        "content":response.text
                    }
            except httpx.TimeoutException:
                if i==Max_Retries-1:
                    return {
                        "url":url,
                        "error":"timeout error",

                    }
            except httpx.HTTPStatusError:
                if 400 <= response.status_code < 500:
                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "error": "Client error"
                    }

                elif 500 <= response.status_code < 600:
                    if i==Max_Retries-1:
                        return {
                            "url": url,
                            "status_code": response.status_code,
                            "error": "Server error"
                        }

                else:
                    if i==Max_Retries-1:
                        return {
                            "url": url,
                            "status_code": response.status_code,
                            "error": "HTTP error"
                        }
            except httpx.ConnectError:
                if i==Max_Retries-1:
                    return {
                        "url":url,
                        "error":"Connection errro"
                    }
            




async def async_fetch_many(urls):
    task=[]
    for url in urls:
        task.append(async_fetch(url))
    result=await asyncio.gather(*task)
    return result
        


# lever_url = "https://jobs.lever.co/entrata/661bbcc5-3514-4ba3-b616-8838da6c53ec"
# ashby_url = "https://jobs.ashbyhq.com/CUBE/a67dcd6a-4309-49d7-9d1e-2d3f8ea91324"
# smartrecruiters_url = "https://jobs.smartrecruiters.com/smartrecruiters/744000114676597-senior-software-engineer-python"



# urls = [
#     lever_url,
#     ashby_url,
#     smartrecruiters_url
# ]

# result=asyncio.run(async_fetch_many(urls))
# print(result)