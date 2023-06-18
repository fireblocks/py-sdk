# DispatchPayoutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** |  | 

## Example

```python
from fireblocks_client.models.dispatch_payout_response import DispatchPayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchPayoutResponse from a JSON string
dispatch_payout_response_instance = DispatchPayoutResponse.from_json(json)
# print the JSON string representation of the object
print DispatchPayoutResponse.to_json()

# convert the object into a dict
dispatch_payout_response_dict = dispatch_payout_response_instance.to_dict()
# create an instance of DispatchPayoutResponse from a dict
dispatch_payout_response_form_dict = dispatch_payout_response.from_dict(dispatch_payout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


