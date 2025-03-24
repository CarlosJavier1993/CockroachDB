from app import app

# Esta función handler será el punto de entrada que invoca tu aplicación Flask.
def handler(environ, start_response):
    return app(environ, start_response)
