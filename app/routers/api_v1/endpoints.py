from fastapi import APIRouter

from app.config import config
from app.modules.getRichQuick.api import getRichQuick_v1


# |Public|
public_router = APIRouter(prefix=f"{config.prefixes.public}/v1")
public_routers = (getRichQuick_v1,)

for router in public_routers:
    public_router.include_router(router=router)
