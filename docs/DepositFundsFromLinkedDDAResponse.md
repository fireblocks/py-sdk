# DepositFundsFromLinkedDDAResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether the funds were successfully deposited from the linked DDA | 

## Example

```python
from fireblocks_client.models.deposit_funds_from_linked_dda_response import DepositFundsFromLinkedDDAResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DepositFundsFromLinkedDDAResponse from a JSON string
deposit_funds_from_linked_dda_response_instance = DepositFundsFromLinkedDDAResponse.from_json(json)
# print the JSON string representation of the object
print DepositFundsFromLinkedDDAResponse.to_json()

# convert the object into a dict
deposit_funds_from_linked_dda_response_dict = deposit_funds_from_linked_dda_response_instance.to_dict()
# create an instance of DepositFundsFromLinkedDDAResponse from a dict
deposit_funds_from_linked_dda_response_form_dict = deposit_funds_from_linked_dda_response.from_dict(deposit_funds_from_linked_dda_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


