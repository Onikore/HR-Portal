from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, profile, vacancy, department, tags

api_router = APIRouter(prefix='/api/v1')
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(profile.router, prefix='/profile', tags=['profile'])
api_router.include_router(vacancy.router, prefix='/vacancy', tags=['vacancy'])
api_router.include_router(department.router, prefix='/department', tags=['department'])
api_router.include_router(tags.router, prefix='/tags', tags=['tags'])
