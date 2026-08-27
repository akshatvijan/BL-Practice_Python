import time
import asyncio
from http_client.requests_client import fetch_page
from http_client.httpx_client import async_fetch_many
from crawler.crawler import crawl_page
from processing.parser import parse_job_data
from processing.normalizer import normalize_data
async def main():
    lever_url = "https://jobs.lever.co/entrata/661bbcc5-3514-4ba3-b616-8838da6c53ec"
    ashby_url = "https://job-boards.greenhouse.io/singlestore/jobs/7534083"
    smartrecruiters_url = "https://jobs.smartrecruiters.com/smartrecruiters/744000114676597-senior-software-engineer-python"



    urls = [
        lever_url,
        ashby_url,
        smartrecruiters_url
    ]
    start_time=time.time()
    results=[]
    for url in urls:
        result=fetch_page(url)
        results.append(result)

    end_time=time.time()
    execution_Sequential=end_time-start_time


    failed=0
    successful=0
    for result in results:
        if "error" in result:
            failed+=1
        else:
            successful+=1


    start_time=time.time()
    results=await async_fetch_many(urls)
    end_time=time.time()
    execution_Aync=end_time-start_time

    crawler_result=[]
    for url in urls:
        result=await crawl_page(url)
        crawler_result.append(result)

    parsed_result=parse_job_data(crawler_result)
    normalize_data(parsed_result)

    

    







    print("="*50)
    print("ASYNC WEB INTELLIGENCE COLLECTOR")
    print("="*50)
    print("\n")
    print("URLs processed: ",len(urls))
    print("Successful: ",successful)
    print("failed: ",failed)
    print("\n")
    print("Execution")
    
    print("Sequential ",execution_Sequential)
    print("Async ",execution_Aync)
    improvement = (
        (execution_Sequential - execution_Aync)
        / execution_Sequential
    ) * 100
    print("improvement",improvement)
    normalize_data(parsed_result)
    
    
    

if __name__=="__main__":
    asyncio.run(main())