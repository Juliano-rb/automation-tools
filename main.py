from fastapi import FastAPI, HTTPException
from duckduckgo_search import DDGS

app = FastAPI()


@app.get("/search_web")
async def buscar_na_web(term: str):
    """Performs a web search and returns the results."""
    try:
        with DDGS() as ddgs:
            results = ddgs.text(term, max_results=10)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search_images")
async def buscar_imagens(term: str):
    """Performs an image search and returns the results."""
    try:
        with DDGS() as ddgs:
            results = ddgs.images(term, max_results=10)
        return {"images": resultados}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
