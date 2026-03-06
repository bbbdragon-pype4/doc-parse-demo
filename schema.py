'''
python3 watch_file.py -p1 python3 schema.py -d .
'''
from pydantic import BaseModel,Field
from datetime import date
from typing import Optional,Literal,Annotated

class Name(BaseModel):
    '''
    Object to represent a person by their first and last names.
    '''
    firstName: str
    lastName: str


class Deposit(BaseModel):
    '''
    Object to represent a deposit, indicating a floating-point value denominated in US dollars,
    and a form through which the deposit is made - check, money order, transfer.
    '''
    depositAmount: float
    form: Literal['check','money order','transfer']


class Property(BaseModel):
    '''
    Object to represent the geographic information about the property in question.
    '''
    streetNumber: int
    street: str
    city: str
    state: str
    county: str
    zipCode: Annotated[str,Field(pattern=r'^\d{5}$')]


class Contract(BaseModel):
    '''
    Object to represent the contract which is described in the JPEG file.
    '''
    dt:  Optional[date]
    buyer: Optional[Name]
    seller: Optional[Name]
    deposit: Optional[Deposit]
    prprty: Optional[Property]
    taxId: Optional[Annotated[str,Field(pattern=r'^\d{3}-\d{3}-\d{2}$')]]


