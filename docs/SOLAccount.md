# SOLAccount

The accounts involved in the instruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the account | 
**signer** | **bool** | Indicates if the account needs to sign the instruction. If true a signature for this account must be provided | [optional] 
**writable** | **bool** | Indicates if the account&#39;s data can be changed by the instruction. | [optional] 
**address** | **str** | The address of the account | [optional] 

## Example

```python
from fireblocks.models.sol_account import SOLAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SOLAccount from a JSON string
sol_account_instance = SOLAccount.from_json(json)
# print the JSON string representation of the object
print(SOLAccount.to_json())

# convert the object into a dict
sol_account_dict = sol_account_instance.to_dict()
# create an instance of SOLAccount from a dict
sol_account_from_dict = SOLAccount.from_dict(sol_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


