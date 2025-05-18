# SOLAccountWithValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the account | 
**signer** | **bool** | Indicates if the account needs to sign the instruction. If true a signature for this account must be provided | [optional] 
**writable** | **bool** | Indicates if the account&#39;s data can be changed by the instruction. | [optional] 
**address** | **str** | The address of the account | 

## Example

```python
from fireblocks.models.sol_account_with_value import SOLAccountWithValue

# TODO update the JSON string below
json = "{}"
# create an instance of SOLAccountWithValue from a JSON string
sol_account_with_value_instance = SOLAccountWithValue.from_json(json)
# print the JSON string representation of the object
print(SOLAccountWithValue.to_json())

# convert the object into a dict
sol_account_with_value_dict = sol_account_with_value_instance.to_dict()
# create an instance of SOLAccountWithValue from a dict
sol_account_with_value_from_dict = SOLAccountWithValue.from_dict(sol_account_with_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


