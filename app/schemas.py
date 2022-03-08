from enum import IntEnum
from ipaddress import IPv4Address
from typing import Optional

from pydantic import BaseModel
from pydantic.class_validators import validator

# Example of Schemas for req-res:


class Fuzzing_Result(BaseModel):
    message: str
    total: int
    data: list

    class Config:
        orm_mode = True


# --- ZAP ---
class ZapRequestModel(BaseModel):
    """
    Zap service request model:
    - url: string
    - option: "base" | "full"
    """

    url: str
    option: Optional[str] = "base"


# --- Amass ---


class EnumMode(IntEnum):
    DEFAULT = 0
    PASSIVE = 1
    ACTIVE = 2


class EnumConfigModel(BaseModel):
    mode: Optional[EnumMode] = EnumMode.DEFAULT
    timeout: Optional[int] = None
    dnsResolvers: Optional[list[IPv4Address]] = None

    @validator("dnsResolvers")
    def convert_dns_server(cls, dns: Optional[list[IPv4Address]]):
        if dns == None or len(dns) == 0:
            return None

        return list(map(str, dns))


class EnumRequestModel(BaseModel):
    domain: str
    config: Optional[EnumConfigModel] = None
