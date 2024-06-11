import asyncio
from playwright.async_api import async_playwright


class CaptchaSolver:
    def __init__(self, url: str):
        self.url = url

    async def solve(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(self.url)
            title = await page.title()
            await browser.close()
            return title
