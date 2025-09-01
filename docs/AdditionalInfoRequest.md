# AdditionalInfoRequest

External wallet request with additional payment information for various payment rails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | [**AdditionalInfoRequestAdditionalInfo**](AdditionalInfoRequestAdditionalInfo.md) |  | 

## Example

```python
from fireblocks.models.additional_info_request import AdditionalInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalInfoRequest from a JSON string
additional_info_request_instance = AdditionalInfoRequest.from_json(json)
# print the JSON string representation of the object
print(AdditionalInfoRequest.to_json())

# convert the object into a dict
additional_info_request_dict = additional_info_request_instance.to_dict()
# create an instance of AdditionalInfoRequest from a dict
additional_info_request_from_dict = AdditionalInfoRequest.from_dict(additional_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


