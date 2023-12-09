from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid1

from sqlalchemy import DateTime, ForeignKey, Identity
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .schema import Country, Gender


class Base(DeclarativeBase):
    pass


class Verband(Base):
    __tablename__: str = "verbaende"

    veid: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    verband_name: Mapped[str]
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return f"Verband(veid={self.veid}, verband_name={self.verband_name})"


class Club(Base):
    __tablename__: str = "clubs"

    clid: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    veid: Mapped[int | None] = mapped_column(ForeignKey("verbaende.veid"))
    club_name: Mapped[str]
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return f"Club(veid={self.clid}, club_name={self.club_name})"


class Event(Base):
    __tablename__: str = "events"

    evid: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    veid: Mapped[int | None] = mapped_column(ForeignKey("verbaende.veid"))
    event_name: Mapped[str]
    event_start: Mapped[datetime]
    event_place: Mapped[str]
    address_line_1: Mapped[str]
    address_line_2: Mapped[str]
    postcode: Mapped[str]
    place: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    country: Mapped[Country]
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    competitions: Mapped[list["Competition"]] = relationship(
        back_populates="event",
        cascade="all, delete-orphan",
    )


class Competition(Base):
    __tablename__: str = "competitions"

    coid: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    evid: Mapped[int] = mapped_column(ForeignKey("events.evid"))
    gender: Mapped[Gender]
    min_birthyear: Mapped[int]
    max_birthyear: Mapped[int]

    fee_flat: Mapped[Decimal]
    fee_participant: Mapped[Decimal]

    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    teams: Mapped[list["Team"]] = relationship(back_populates="competition")
    event: Mapped["Event"] = relationship(back_populates="competitions")


class Team(Base):
    __tablename__: str = "teams"

    tid: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    coid: Mapped[int] = mapped_column(ForeignKey("competitions.coid"))
    clid: Mapped[int | None] = mapped_column(ForeignKey("clubs.clid"))
    secret: Mapped[UUID] = mapped_column(default=uuid1())

    team_name: Mapped[str]
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    participants: Mapped[list["Participant"]] = relationship(
        back_populates="team",
        cascade="all, delete-orphan",
    )
    competition: Mapped["Competition"] = relationship(
        back_populates="teams",
    )
    club: Mapped["Club"] = relationship(
        back_populates="teams",
    )

    def __repr__(self) -> str:
        return f"Team(tid={self.tid}, team_name={self.team_name})"


class Participant(Base):
    __tablename__: str = "participants"

    pid: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    tid: Mapped[int]

    first_name: Mapped[str]
    last_name: Mapped[str]
    gender: Mapped[Gender]
    birth_year: Mapped[int]
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    team: Mapped["Team"] = relationship(
        back_populates="participants",
    )
