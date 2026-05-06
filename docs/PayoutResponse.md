# PayoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** |  | 
**payment_account** | [**PaymentAccountResponse**](PaymentAccountResponse.md) |  | 
**created_at** | **float** |  | 
**state** | [**PayoutState**](PayoutState.md) |  | 
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**reason_of_failure** | **str** | - INSUFFICIENT_BALANCE - SOURCE_TRANSLATION - SOURCE_NOT_UNIQUE - SOURCE_NOT_FOUND - SOURCE_TYPE_NOT_SUPPORTED - EMPTY_SOURCE - DESTINATION_TRANSLATION - DESTINATION_NOT_UNIQUE - DESTINATION_NOT_FOUND - EMPTY_DESTINATION - PARSING - UNKNOWN - FIREBLOCKS_CLIENT - TRANSACTION_SUBMISSION  | [optional] 
**init_method** | [**PayoutInitMethod**](PayoutInitMethod.md) |  | [optional] 
**instruction_set** | [**List[PayoutInstructionResponse]**](PayoutInstructionResponse.md) |  | 
**report_url** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.payout_response import PayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutResponse from a JSON string
payout_response_instance = PayoutResponse.from_json(json)
# print the JSON string representation of the object
print(PayoutResponse.to_json())

# convert the object into a dict
payout_response_dict = payout_response_instance.to_dict()
# create an instance of PayoutResponse from a dict
payout_response_from_dict = PayoutResponse.from_dict(payout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


