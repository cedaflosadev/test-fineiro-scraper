from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.captcha_solver import CaptchaSolver

router = APIRouter()


class ScrapeRequest(BaseModel):
    url: str


@router.post("/scrape")
async def scrape(data: ScrapeRequest):
    solver = CaptchaSolver(url=data.url)
    try:
        result = await solver.solve()
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
