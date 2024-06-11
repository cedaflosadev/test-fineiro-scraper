import pytest
from app.core.captcha_solver import CaptchaSolver

@pytest.mark.asyncio
async def test_solve():
    url = "https://www.google.com/recaptcha/api2/demo"
    solver = CaptchaSolver(url=url)
    result = await solver.solve()
    assert result is not None
    assert "reCAPTCHA" in result
