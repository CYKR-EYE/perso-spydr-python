from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, CrawlerMonitor, DisplayMode, MemoryAdaptiveDispatcher
import asyncio

async def crawl_batch():
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        check_robots_txt=True,
        stream=False
    )

    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70,
        check_interval=1.0,
        max_session_permit=10,
        monitor=CrawlerMonitor(
            display_mode = DisplayMode.DETAILED,
        )
    )

    urls = [
        "URL_TO_CRAWL_1",
        "URL_TO_CRAWL_2",
        "URL_TO_CRAWL_3",
        # Add more URLs as needed
    ]

    async with AsyncWebCrawler(config=browser_config) as crawler:

        # Get the results for each URL
        results = await crawler.arun_many(
            urls=urls,
            config=run_config,
            dispatcher=dispatcher
        )

        # Process the results after crawling
        for result in results:
            if result.sucess:
                await process_result(result)
            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")

async def process_result(result):

    # Extract basic infos
    print(f"\nProcessing; {result.url}...")
    print(f"Status Code: {result.status_code}")

    # Extract and process text content
    if result.markdown:
        # Remove whitespaces and first 150 chracters (clearer)
        clean_text = ' '.join(result.markdown.split())
        preview = clean_text[:150] + '...' if len(clean_text) > 150 else clean_text
        print(f"Content Preview: {preview}")

    # Process metadata
    if result.metadata:
        print("\nMetadata:")
        for key, value in result.metadata.items():
            print(f"{key}: {value}")
    
    # Process links
    if result.links:
        print("\links:")
        internal_links = result.links.get('internal', [])
        external_links = result.links.get('external', [])
        print(f"Found {len(internal_links)} internal links")
        print(f"Found {len(external_links)} external links")

    # Spacer
    print("-" * 80)

asyncio.run(crawl_batch())

# Note: Replace "URL_TO_CRAWL_1", "URL_TO_CRAWL_2", etc. with the actual URLs you want to crawl.
# Note: Make sure to install the required packages before running the script.
# You can install the required packages and dependencies using pip:
# pip install crawl4ai then crawl4ai-setup
