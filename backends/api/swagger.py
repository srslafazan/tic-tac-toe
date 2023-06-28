import os
from flasgger import Swagger
from importlib.metadata import distribution

dist = distribution("api")


def InitSwagger(app):
    Swagger(
        app,
        config={
            "headers": [],
            "specs": [
                {
                    "endpoint": "root",
                    "route": "/root.json",
                    "rule_filter": lambda rule: True,  # all in
                    "model_filter": lambda tag: True,  # all in
                }
            ],
            "static_url_path": "/flasgger_static",
            "swagger_ui": True,
            "specs_route": "/docs/",
            "servers": [
                {
                    "url": "https://tic-tac-toe-backends.fly.dev",
                    "description": "Production server",
                }
            ],
            "title": "Tic Tac Toe API - Docs",
        },
        template={
            "swagger": "2.0",
            "info": {
                "title": dist.metadata["Summary"],
                "description": dist.metadata["Summary"],
                "contact": {
                    "responsibleOrganization": dist.metadata["Author"],
                    "responsibleDeveloper": dist.metadata["Author"],
                    "email": dist.metadata["Author-email"],
                    "url": "https://shainlafazan.com",
                },
                "version": dist.version,
            },
            "host": os.getenv("SWAGGER_HOST", "localhost:5000"),
            "basePath": "/",
            "schemes": ["http", "https"],
        },
    )
