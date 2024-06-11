import asyncio
from playwright.async_api import async_playwright


class CaptchaSolver:
    """
    Clase CaptchaSolver para resolver captchas en sitios web.

    Atributos:
    - url (str): La URL del sitio web que contiene el captcha.
    """

    def __init__(self, url: str):
        """
        Inicializa una nueva instancia de CaptchaSolver.

        Args:
        - url (str): La URL del sitio web que contiene el captcha.
        """
        self.url = url

    async def solve(self):
        """
        Resuelve el captcha en la URL proporcionada.

        Returns:
        - str: El título de la página después de resolver el captcha.
        """
        async with async_playwright() as p:
            # Lanzar un nuevo navegador Chromium
            browser = await p.chromium.launch()
            # Crear una nueva página en el navegador
            page = await browser.new_page()
            # Navegar a la URL especificada
            await page.goto(self.url)
            # Obtener el título de la página
            title = await page.title()
            # Cerrar el navegador
            await browser.close()
            return title
