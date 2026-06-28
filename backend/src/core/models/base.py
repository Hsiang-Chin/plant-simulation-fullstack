import datetime

from sqlalchemy import DateTime, func ,String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Dock(Base):
    __tablename__ = "docks"

    dock_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(200))

class InboundShipment(Base):
    __tablename__ = "inbound_shipments"

    inbound_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    arrival_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    dock_id: Mapped[int] = mapped_column(Integer, ForeignKey("docks.dock_id"))


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )