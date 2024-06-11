## Configuración

1. Clona el repositorio
2. Instala las dependencias: `pip install -r requirements.txt`
3. Necesario para descargar e instalar estos navegadores: `python -m playwright install`
4. Ejecuta la aplicación: `uvicorn app.main:app --reload`

## Dockerización

1. Construye la imagen Docker: `docker build -t scraping-api .`
2. Ejecuta el contenedor: `docker run -p 8000:8000 scraping-api`

## Uso

### Endpoint: /api/scrape

#### Método: POST

#### Parámetros:

- url (string): URL del sitio a hacer scraping.

Ejemplo de solicitud:

```json
{
  "url": "https://www.google.com/recaptcha/api2/demo"
}
```
