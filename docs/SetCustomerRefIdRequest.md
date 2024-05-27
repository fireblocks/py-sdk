# SetCustomerRefIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ref_id** | **str** | Customer reference ID | [optional] 

## Example

```python
from fireblocks_client.models.set_customer_ref_id_request import SetCustomerRefIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomerRefIdRequest from a JSON string
set_customer_ref_id_request_instance = SetCustomerRefIdRequest.from_json(json)
# print the JSON string representation of the object
print SetCustomerRefIdRequest.to_json()

# convert the object into a dict
set_customer_ref_id_request_dict = set_customer_ref_id_request_instance.to_dict()
# create an instance of SetCustomerRefIdRequest from a dict
set_customer_ref_id_request_form_dict = set_customer_ref_id_request.from_dict(set_customer_ref_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


