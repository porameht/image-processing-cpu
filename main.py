from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
import uvicorn

def create_app() -> FastAPI:
    app = FastAPI(title=settings.API_TITLE)
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["POST", "GET"],
        allow_headers=["multipart/form-data", "Content-Type", "Accept", "Authorization"],
    )
    
    app.include_router(router)
    
    return app

app = create_app()

# if __name__ == "__main__":
#     uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)