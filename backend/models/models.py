from pydantic import BaseModel


class Vendor(BaseModel):
    name: str | None
    address: str | None


class Item(BaseModel):
    name: str
    quantity: float
    unit_price: float | None
    price: float


class Invoice(BaseModel):
    invoice_number: str | None
    date: str | None
    vendor: Vendor
    table: str | None
    diners: int | None
    items: list[Item]
    subtotal: float | None
    taxes_percent: float | None
    taxes: float | None
    total: float
    discounts: float | None


    def check_total(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price == self.total