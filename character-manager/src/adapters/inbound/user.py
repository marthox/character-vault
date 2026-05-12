from fastapi import APIRouter

user_router = APIRouter(prefix="/user")

@user_router.get('/{user_id}/characters/')
async def get_character(character_id: str):
    pass

@user_router.post('/{user_id}/characters/')
async def create_character(character_data: dict):
    pass

@user_router.get('/{user_id}/characters/{character_id}/')
async def get_character_by_id(character_id: str):
    pass

@user_router.put('/{user_id}/characters/{character_id}/')
async def update_character(character_id: str, character_data: dict):
    pass

@user_router.delete('/{user_id}/characters/{character_id}/')
async def delete_character(character_id: str):
    pass
