from fastapi import FastAPI, HTTPException, Query
from duckduckgo_search import DDGS

from parameters import Region, LicenseImage, Size, TypeImage, Color, Layout

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
