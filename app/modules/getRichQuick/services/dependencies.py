from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.postgresql.dependencies import get_async_session
from app.modules.getRichQuick.services import GetRichQuickServices


async def get_rich_services(
    session: AsyncSession = Depends(get_async_session),
) -> GetRichQuickServices:
    return GetRichQuickServices(session=session)
