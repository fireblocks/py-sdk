# CreatePayoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | 
**instruction_set** | [**List[PayoutInstruction]**](PayoutInstruction.md) |  | 

## Example

```python
from fireblocks.models.create_payout_request import CreatePayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayoutRequest from a JSON string
create_payout_request_instance = CreatePayoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePayoutRequest.to_json())

# convert the object into a dict
create_payout_request_dict = create_payout_request_instance.to_dict()
# create an instance of CreatePayoutRequest from a dict
create_payout_request_from_dict = CreatePayoutRequest.from_dict(create_payout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


