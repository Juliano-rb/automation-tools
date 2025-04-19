from fastapi import FastAPI, HTTPException
from duckduckgo_search import DDGS

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
    region: str = "br-pt",
    max_results: int = 10,
    license_image: str = "any",
    size: str = None,
    type_image: str = None,
    color: str = None,
    layout: str = None,
):
    """Performs an image search and returns the results."""
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
