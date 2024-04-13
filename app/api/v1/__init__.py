from fastapi import APIRouter
from .endpoints import router as endpoints_router
from .image_upload import router as image_upload_router

router = APIRouter()
router.include_router(endpoints_router)
router.include_router(image_upload_router)
