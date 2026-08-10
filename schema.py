from pydantic import BaseModel, Field
from enum import Enum


class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"
        
class SellerType(str,Enum):
    dealer="Dealer"
    individual="Individual"

class TransmissionType(str,Enum):
    manual ="Manual"
    automatic ="Automatic"


class CarFeatures(BaseModel):
    Car_Name: str = Field(..., json_schema_extra={"example": "ritz"})
    Year: int = Field(..., json_schema_extra={"example": 2014})
    Present_Price: float = Field(..., json_schema_extra={"example": 5.59})
    Kms_Driven: int = Field(..., json_schema_extra={"example": 27000})
    Fuel_Type: FuelType
    Seller_Type: SellerType
    Transmission: TransmissionType
    Owner: int = Field(
        ..., ge=0, le=3, json_schema_extra={"example": 0}, description="Number of previous owners (0, 1, 2, or 3)"
    )


class PredictionResponse(BaseModel):
    prediction_price: float

