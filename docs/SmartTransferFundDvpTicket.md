# SmartTransferFundDvpTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **str** | Transaction fee | [optional] 
**fee_level** | **str** | Transaction fee level. | [optional] 
**note** | **str** | Transaction note | [optional] 

## Example

```python
from fireblocks.models.smart_transfer_fund_dvp_ticket import SmartTransferFundDvpTicket

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferFundDvpTicket from a JSON string
smart_transfer_fund_dvp_ticket_instance = SmartTransferFundDvpTicket.from_json(json)
# print the JSON string representation of the object
print(SmartTransferFundDvpTicket.to_json())

# convert the object into a dict
smart_transfer_fund_dvp_ticket_dict = smart_transfer_fund_dvp_ticket_instance.to_dict()
# create an instance of SmartTransferFundDvpTicket from a dict
smart_transfer_fund_dvp_ticket_from_dict = SmartTransferFundDvpTicket.from_dict(smart_transfer_fund_dvp_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


