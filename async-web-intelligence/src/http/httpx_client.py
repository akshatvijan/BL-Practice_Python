import httpx
import asyncio

async def async_fetch(url):
    try:
        async with httpx.AsyncClient() as client:
            response=await client.get(url,timeout=10)
            response.raise_for_status()

            return {
                "url":url,
                "status_code":response.status_code,
                "content":response.text
            }
    except httpx.TimeoutException:
        return {
            "url":url,
            "error":"timeout error",

        }
    except httpx.HTTPStatusError:
        return {
            "url":url,
            "status_code":response.status_code,
            "error":"Http status error"
        }
    except httpx.ConnectError:
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