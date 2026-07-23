# GetBillingInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_blockchains_limit** | **float** | Maximum number of activated blockchains allowed for this tenant (0 &#x3D; not purchased). | 
**activated_blockchains_used** | **float** | Number of blockchains currently in Activating, Activated, or Deactivating state for this tenant. Filter-independent (ignores list filters/pagination). | 

## Example

```python
from fireblocks.models.get_billing_info_response import GetBillingInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBillingInfoResponse from a JSON string
get_billing_info_response_instance = GetBillingInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetBillingInfoResponse.to_json())

# convert the object into a dict
get_billing_info_response_dict = get_billing_info_response_instance.to_dict()
# create an instance of GetBillingInfoResponse from a dict
get_billing_info_response_from_dict = GetBillingInfoResponse.from_dict(get_billing_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


