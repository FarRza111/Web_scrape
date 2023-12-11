from dataclasses import dataclass

@dataclass
class Item:
    city: str
    date: str
    price: int
    location: str
    currency: str
    room_size: Optional[str] = None
    # def __post_init__(self):
    #     if isinstance(self.price, str):
    #         raise TypeError('string is not a valid attribute type for price')
    #     if isinstance(self.currency, int):
    #         raise TypeError(f'string is not a valid attribute type for currency')
    #     else:
    #         ...
