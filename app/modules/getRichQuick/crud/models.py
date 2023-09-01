from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.postgresql.base import Base
from app.db.postgresql.models import ID, Deleted, Timestamp


class Ticker(Base, Deleted, Timestamp, ID):
    __tablename__ = "ticker"

    ticker: Mapped[str] = mapped_column(
        String(10),
        unique=False,
        nullable=False,
        index=False,
    )

    option_chains: Mapped[list["OptionChain"]] = relationship(
        back_populates="ticker"
    )

    def __repr__(self):
        return f"<Ticker uuid={self.uuid} ticker={self.ticker}>"


class OptionChain(Base, Deleted, Timestamp, ID):
    __tablename__ = "option_chain"

    expiration_date: Mapped[datetime] = mapped_column(
        unique=True,
        nullable=False,
        index=True,
    )

    call_option_chain: Mapped[list["CallOptionQuote"]] = relationship(
        back_populates="option_chain",
    )

    put_option_chain: Mapped[list["PutOptionQuote"]] = relationship(
        back_populates="option_chain",
    )

    ticker: Mapped["Ticker"] = relationship(back_populates="option_chains")

    ticker_uuid: Mapped[UUID] = mapped_column(ForeignKey("ticker.uuid"))


class CallOptionQuote(Base, Deleted, Timestamp, ID):
    __tablename__ = "call_option_quote"

    contractSymbol: Mapped[str] = mapped_column(
        String(50),
        unique=False,
        nullable=False,
        index=False,
    )
    lastTradeDate: Mapped[datetime] = mapped_column(
        unique=True,
        nullable=False,
        index=True,
    )
    strike: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    lastPrice: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    bid: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    ask: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    change: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    percentChange: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    volume: Mapped[Optional[float]]
    openInterest: Mapped[Optional[float]]
    impliedVolatility: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    inTheMoney: Mapped[bool]
    middle: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    BidAskSpread: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )

    option_chain: Mapped[OptionChain] = relationship(
        back_populates="call_option_chain"
    )
    option_chain_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("option_chain.uuid")
    )


class PutOptionQuote(Base, Deleted, Timestamp, ID):
    __tablename__ = "put_option_quote"

    contractSymbol: Mapped[str] = mapped_column(
        String(50),
        unique=False,
        nullable=False,
        index=False,
    )
    lastTradeDate: Mapped[datetime] = mapped_column(
        unique=True,
        nullable=False,
        index=True,
    )
    strike: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    lastPrice: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    bid: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    ask: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    change: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    percentChange: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    volume: Mapped[Optional[float]]
    openInterest: Mapped[Optional[float]]
    impliedVolatility: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    inTheMoney: Mapped[bool]
    middle: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )
    BidAskSpread: Mapped[float] = mapped_column(
        unique=False,
        nullable=False,
        index=True,
    )

    option_chain: Mapped[OptionChain] = relationship(
        back_populates="put_option_chain"
    )
    option_chain_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("option_chain.uuid")
    )
