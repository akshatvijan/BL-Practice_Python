from crawl4ai import AsyncWebCrawler

async def crawl_page(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return {
            "url": url,
            "markdown": result.markdown,
            "html": result.html,
            "links": result.links,
            "metadata": result.metadata,
            "structured_data": result.structured_data
        }
        
        
        