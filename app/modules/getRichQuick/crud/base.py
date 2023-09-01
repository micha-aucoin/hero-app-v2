from app.db.postgresql.crud import CRUD
from app.modules.getRichQuick.crud.models import (
    CallOptionQuote,
    OptionChain,
    PutOptionQuote,
    Ticker,
)


class TickerCRUD(CRUD[Ticker]):
    """CRUD operations for Ticker model."""

    table = Ticker


class OptionChainCRUD(CRUD[OptionChain]):
    """CRUD operations for OptionChain model."""

    table = OptionChain


class CallOptionQuoteCRUD(CRUD[CallOptionQuote]):
    """CRUD operations for CallOptionQuote model."""

    table = CallOptionQuote


class PutOptionQuoteCRUD(CRUD[PutOptionQuote]):
    """CRUD operations for PutOptionQuote model."""

    table = PutOptionQuote
