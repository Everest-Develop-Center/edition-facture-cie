from typing import Optional

from pydantic import BaseModel

# Other class
class Block(BaseModel):
    consumption: str
    amount: str
    cost: str

class ConsumptionDetails(BaseModel):
    # Energy bill
    period_start_date: str
    period_end_date: str
    old_index: str
    new_index: str
    fixed_fee: str
    block_1: Block
    block_2: Block
    last_year_consumption: str
    amount_excluding_fee: str
    vat: str
    amount_including_fee: str
    kWh_variation: str
    bill_energy_amount: str
    # Tax and fees
    rer: str
    treom: str
    rti_fee: str
    cash_payment_fee: str
    tax_amount: str

class CustomerInfo(BaseModel):
    id: str
    firstname: str
    lastname: str
    agency: str
    contracted_power: str
    connection_type: str
    meter_number: str
    reference : str
    address: str

# Main class
class InvoiceDTO(BaseModel):
    id: str
    period: str
    payment_deadline: str
    bill_amount: str
    customer_info: Optional[CustomerInfo] = None
    regional_direction: str
    consumption_details : Optional[ConsumptionDetails] = None
    message_to_the_customer: str
    message_to_the_customer: str
    credit_notes: str
    outstanding_amount: str