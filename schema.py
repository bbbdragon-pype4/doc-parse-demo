'''
python3 watch_file.py -p1 python3 schema.py -d .
'''
from pydantic import BaseModel,Field
from datetime import date
from typing import Optional,Literal,Annotated

class Name(BaseModel):

    firstName: str
    lastName: str


class Deposit(BaseModel):

    depositAmount: float
    form: Literal['check','money order','transfer']


class Property(BaseModel):

    streetNumber: int
    street: str
    city: str
    state: str
    county: str
    zipCode: Annotated[str,Field(pattern=r'^\d{5}$')]


class Contract(BaseModel):

    dt:  Optional[date]
    buyer: Optional[Name]
    seller: Optional[Name]
    deposit: Optional[Deposit]
    prprty: Optional[Property]
    taxId: Optional[Annotated[str,Field(pattern=r'^\d{3}-\d{3}-\d{2}$')]]


