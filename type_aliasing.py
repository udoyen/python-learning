from typing import Union, Literal


# Assume BankDetails is a class defined somewhere in the code
class BankDetails:
    account_number: str
    bank_name: str
    
AddressOrBankDetails = Union[str, BankDetails]

Position = Literal['Chef', 'Sous Chef', 'Host', 'Server', 'Delivery Driver']

# Now AddressOrBankDetails can be either a string or a BankDetails object
address_or_bank: AddressOrBankDetails = "123 Main St, Springfield"
address_or_bank: AddressOrBankDetails = BankDetails(account_number="123456", bank_name="Springfield Bank")
