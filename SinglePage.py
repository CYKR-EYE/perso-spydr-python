# Webscrapping for a Single Page

import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler() as crawler:

        # Start crawling from the given URL
        result = await crawler.arun(url="URL_TO_CRAWL")

        # Print the result
        print(result.markdown)

# Run the main function
asyncio.run(main())

# Note: Replace "URL_TO_CRAWL" with the actual URL you want to crawl.
# Note: Make sure to install the required packages before running the script.
# You can install the required packages and dependencies using pip:
# pip install crawl4ai then crawl4ai-setup