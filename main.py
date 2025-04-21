import sys
import asyncio
import json
from fastapi import FastAPI, HTTPException, Query
from duckduckgo_search import DDGS
from parameters import Region, LicenseImage, Size, TypeImage, Color, Layout
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.async_crawler_strategy import AsyncPlaywrightCrawlerStrategy
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

# Ajuste do event loop para suportar subprocessos no Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


async def patched_close(self):
    return


# Apply the monkey patch
AsyncPlaywrightCrawlerStrategy.close = patched_close

app = FastAPI()


@app.get("/search_web")
async def buscar_na_web(term: str, region: str = "br-pt", max_results=10):
    """Performs a web search and returns the results."""
    try:
        max_results = int(max_results)
        with DDGS() as ddgs:
            results = ddgs.text(term, region=region, max_results=max_results)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search_images")
async def buscar_imagens(
    term: str,
    region: Region = Query(Region.BR_PT),
    max_results: int = Query(10, gt=0),
    license_image: LicenseImage = Query(LicenseImage.ANY),
    size: Size = Query(None),
    type_image: TypeImage = Query(None),
    color: Color = Query(None),
    layout: Layout = Query(None),
):
    """DuckDuckGo images search. Query params: https://duckduckgo.com/params.

    Returns:
        List of dictionaries with images search results.
    """
    try:
        max_results = int(max_results)
        with DDGS() as ddgs:
            results = ddgs.images(
                term,
                region=region,
                max_results=max_results,
                license_image=license_image,
                type_image=type_image,
                layout=layout,
                color=color,
                size=size,
            )
        return {"images": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/crawl_web")
async def crawl_web(
    url: str,
    wait_for: str = None,
    exclude_external_links: bool = True,
    extraction_schema: str = None,
):
    try:
        extraction_schema_dict = (
            json.loads(extraction_schema) if extraction_schema else None
        )

        config = CrawlerRunConfig(
            wait_for=wait_for,
            exclude_external_links=exclude_external_links,
            extraction_strategy=(
                JsonCssExtractionStrategy(extraction_schema_dict)
                if extraction_schema_dict
                else None
            ),
        )
        async with AsyncWebCrawler(headless=True, js_engine="playwright") as crawler:
            result = await crawler.arun(url=url, config=config)

            if extraction_schema:
                return json.loads(result.extracted_content)
            else:
                return result.markdown.raw_markdown
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
