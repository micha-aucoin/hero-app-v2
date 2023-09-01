from typing import TYPE_CHECKING

from app.db.postgresql.decorators import transaction
from app.modules.getRichQuick.crud import (
    CallOptionQuoteCRUD,
    OptionChainCRUD,
    PutOptionQuoteCRUD,
    TickerCRUD,
)
from app.modules.getRichQuick.crud.models import (
    CallOptionQuote,
    OptionChain,
    PutOptionQuote,
    Ticker,
)


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.modules.getRichQuick.services.schemas import (
        OptionChainCreate,
        OptionQuoteCreate,
        TickerCreate,
    )


class GetRichQuickServices:
    """Services to get rich quick!"""

    def __init__(self, session: "AsyncSession"):
        self.session = session
        self.call = CallOptionQuoteCRUD(session=session)
        self.put = PutOptionQuoteCRUD(session=session)
        self.option_chain = OptionChainCRUD(session=session)
        self.ticker = TickerCRUD(session=session)

    @transaction
    async def create_call(
        self,
        schema: "OptionQuoteCreate",
        _commit: bool = True,
    ) -> "CallOptionQuote":
        return await self.call.insert(data=schema.dict())

    @transaction
    async def create_put(
        self,
        schema: "OptionQuoteCreate",
        _commit: bool = True,
    ) -> "PutOptionQuote":
        return await self.put.insert(data=schema.dict())

    @transaction
    async def create_option_chain(
        self,
        schema: "OptionChainCreate",
        _commit: bool = True,
    ) -> "OptionChain":
        return await self.option_chain.insert(data=schema.dict())

    @transaction
    async def create_ticker(
        self,
        schema: "TickerCreate",
        _commit: bool = True,
    ) -> "Ticker":
        return await self.ticker.insert(data=schema.dict())
