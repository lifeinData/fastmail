import boto3
from base import *

class SESEmailProvider(EmailProviderService):
    def __init__(self, from_address: str, client):
        super().__init__(from_address)
        self.client = client
    def send(self, email_content:EmailContent, addresses:AddressContent) -> SendResult:
        response = self.client.send_email()
        return SendResult(message_id=response['msgId'], provider_name="ses")