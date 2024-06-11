from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.captcha_solver import CaptchaSolver

# Crear una instancia de APIRouter para definir las rutas de la API
router = APIRouter()

# Definir un modelo de datos utilizando Pydantic


class ScrapeRequest(BaseModel):
    """
    Modelo de datos para la solicitud de scraping.

    Atributos:
    - url: str - La URL del sitio web a hacer scraping.
    """
    url: str


@router.post("/scrape", response_model=dict)
async def scrape(data: ScrapeRequest):
    """
    Endpoint para realizar scraping en un sitio web protegido por reCAPTCHA.

    Args:
    - data (ScrapeRequest): El cuerpo de la solicitud debe contener la URL del sitio web.

    Returns:
    - dict: Un diccionario con el resultado del scraping.

    Raises:
    - HTTPException: Si ocurre un error durante el proceso de scraping.
    """
    solver = CaptchaSolver(url=data.url)
    try:
        # Intentar resolver el captcha y obtener el resultado
        result = await solver.solve()
        return {"result": result}
    except Exception as e:
        # Si ocurre un error, lanzar una excepción HTTP con el código de estado 500
        raise HTTPException(status_code=500, detail=str(e))
