from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.utils.schemas import BaseInput, BaseOutput, BaseSearch


####################################################
#      O P T I O N  Q U O T E S  S C H E M A S     #
####################################################


class OptionQuoteBase(BaseModel):
    """Common fields for serialisation and validation."""

    contractSymbol: str
    lastTradeDate: datetime
    strike: float
    lastPrice: float
    bid: float
    ask: float
    change: float
    percentChange: float
    volume: Optional[float]
    openInterest: Optional[float]
    impliedVolatility: float
    inTheMoney: bool
    middle: float
    BidAskSpread: float


class OptionQuoteCreate(BaseInput, OptionQuoteBase):
    """Validation schema to create option quote record."""

    option_chain_uuid: UUID


class OptionQuoteUpdate(OptionQuoteCreate):
    """Validation schema to create/update option quote record."""


class OptionQuotePatch(BaseInput, OptionQuoteBase):
    """Validation schema to patch option quote record."""


class OptionQuoteRetrieve(BaseOutput, OptionQuoteBase):
    """Serialisation schema to retrieve option quote records."""

    uuid: UUID

    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class OptionQuoteSearch(BaseSearch, OptionQuoteBase):
    """Schema to validate option quote search parameters."""


class OptionQuoteSearchResult(BaseModel):
    """Schema to serialise search results for option quotes."""

    count: int
    items: list[OptionQuoteRetrieve]


####################################################
#      O P T I O N  C H A I N  S C H E M A S       #
####################################################


class OptionChainBase(BaseModel):
    expiration_date: date


class OptionChainCreate(BaseInput, OptionChainBase):
    """Validation schema to create option chain record."""

    call_option_chain: list[OptionQuoteCreate] = []
    put_option_chain: list[OptionQuoteCreate] = []
    ticker_uuid: UUID


class OptionChainUpdate(OptionChainCreate):
    """Validation schema to create/update option chain record."""


class OptionChainPatch(BaseInput, OptionChainBase):
    """Validation schema to patch option chain record."""


class OptionChainRetrieve(BaseOutput, OptionChainBase):
    """Serialisation schema to retrieve option chain records."""

    uuid: UUID

    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class OptionChainSearch(BaseSearch, OptionChainBase):
    """Schema to validate option chain search parameters."""


class OptionChainSearchResult(BaseModel):
    """Schema to serialise search results for option chains."""

    count: int
    items: list[OptionChainRetrieve]


####################################################
#        S T O C K  I N F O  S C H E M A S         #
####################################################


class TickerBase(BaseModel):
    ticker: str


class TickerCreate(BaseInput, TickerBase):
    """Validation schema to create stock market info record."""

    option_chains: list[OptionChainCreate] = []


class TickerUpdate(TickerCreate):
    """Validation schema to create/update stock market info record."""


class TickerPatch(BaseInput, TickerBase):
    """Validation schema to patch stock market info record."""


class TickerRetrieve(BaseOutput, TickerBase):
    """Serialisation schema to retrieve stock market info records."""

    uuid: UUID

    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class TickerSearch(BaseSearch, TickerBase):
    """Schema to validate stock market info search parameters."""


class TickerSearchResult(BaseModel):
    """Schema to serialise search results for stock market info."""

    count: int
    items: list[TickerRetrieve]
