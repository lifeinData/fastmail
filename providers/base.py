from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class EmailContent:
    subject: str
    html_body: str | None = None
    txt_body: str | None = None

@dataclass
class AddressContent:
    to_address: str

@dataclass
class SendResult:
    message_id: str
    provider_name:str

class EmailProviderService(ABC):
    def __init__(self, from_address):
        self.from_address = from_address

    @abstractmethod
    def send(self, email_content:EmailContent, addresses:AddressContent) -> SendResult:
        ...