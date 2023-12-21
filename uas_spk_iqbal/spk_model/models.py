from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class InfinixPhone(Base):
    __tablename__ = "infinix_phones"

    id : Mapped[int] = mapped_column(primary_key=True)
    model : Mapped[str]
    ram : Mapped[int]
    processor : Mapped[str]
    storage : Mapped[int]
    battery : Mapped[int]
    price : Mapped[int]
    screen_size : Mapped[float]

    def __repr__(self) -> str :
        return f"id={self.id}, model={self.model}, ram={self.ram}, processor={self.processor}, storage={self.storage}, battery={self.battery}, price={self.price}, screen_size={self.screen_size}"
