# IssueApiUserPairingTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the user | 
**name** | **str** | The name of the user | [optional] 
**role** | [**UserRole**](UserRole.md) |  | 
**enabled** | **bool** | Whether the user is enabled | 
**user_type** | [**UserType**](UserType.md) |  | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**pairing_token** | **str** | The device pairing token issued for the given user | 

## Example

```python
from fireblocks.models.issue_api_user_pairing_token_response import IssueApiUserPairingTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssueApiUserPairingTokenResponse from a JSON string
issue_api_user_pairing_token_response_instance = IssueApiUserPairingTokenResponse.from_json(json)
# print the JSON string representation of the object
print(IssueApiUserPairingTokenResponse.to_json())

# convert the object into a dict
issue_api_user_pairing_token_response_dict = issue_api_user_pairing_token_response_instance.to_dict()
# create an instance of IssueApiUserPairingTokenResponse from a dict
issue_api_user_pairing_token_response_from_dict = IssueApiUserPairingTokenResponse.from_dict(issue_api_user_pairing_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


