from fastapi import APIRouter, Depends, status

from app.modules.auth.api_token import get_api_key
from app.modules.getRichQuick.services import (
    GetRichQuickServices,
    get_rich_services,
)
from app.modules.getRichQuick.services.schemas import (
    OptionChainCreate,
    OptionChainRetrieve,
    OptionQuoteCreate,
    OptionQuoteRetrieve,
    TickerCreate,
    TickerRetrieve,
)


# |Public|
public_router = APIRouter(prefix="/GetRickQuick", tags=["public/GetRickQuick"])


@public_router.post(
    "/ticker",
    response_model=TickerRetrieve,
    status_code=status.HTTP_201_CREATED,
)
async def create_ticker(
    schema: TickerCreate,
    service: GetRichQuickServices = Depends(get_rich_services),
):
    return await service.create_ticker(schema=schema)


@public_router.post(
    "/option_chain",
    response_model=OptionChainRetrieve,
    status_code=status.HTTP_201_CREATED,
)
async def create_option_chain(
    schema: OptionChainCreate,
    service: GetRichQuickServices = Depends(get_rich_services),
):
    return await service.create_option_chain(schema=schema)


@public_router.post(
    "/call",
    response_model=OptionQuoteRetrieve,
    status_code=status.HTTP_201_CREATED,
)
async def create_call(
    schema: OptionQuoteCreate,
    service: GetRichQuickServices = Depends(get_rich_services),
):
    return await service.create_call(schema=schema)


@public_router.post(
    "/put",
    response_model=OptionQuoteRetrieve,
    status_code=status.HTTP_201_CREATED,
)
async def create_put(
    schema: OptionQuoteCreate,
    service: GetRichQuickServices = Depends(get_rich_services),
):
    return await service.create_put(schema=schema)
