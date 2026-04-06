# ListVaultsForRegistrationResponse

Response containing vault account IDs assigned to a legal entity registration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of legal entity registrations (optional) | [optional] 
**data** | **List[str]** | List of vault account IDs assigned to the legal entity registration | 
**next** | **str** | Cursor to pass as &#x60;pageCursor&#x60; to retrieve the next page | [optional] 
**prev** | **str** | Cursor to pass as &#x60;pageCursor&#x60; to retrieve the previous page | [optional] 

## Example

```python
from fireblocks.models.list_vaults_for_registration_response import ListVaultsForRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListVaultsForRegistrationResponse from a JSON string
list_vaults_for_registration_response_instance = ListVaultsForRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(ListVaultsForRegistrationResponse.to_json())

# convert the object into a dict
list_vaults_for_registration_response_dict = list_vaults_for_registration_response_instance.to_dict()
# create an instance of ListVaultsForRegistrationResponse from a dict
list_vaults_for_registration_response_from_dict = ListVaultsForRegistrationResponse.from_dict(list_vaults_for_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


