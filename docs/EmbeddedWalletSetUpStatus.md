# EmbeddedWalletSetUpStatus

embedded wallet setup status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | status | 

## Example

```python
from fireblocks.models.embedded_wallet_set_up_status import EmbeddedWalletSetUpStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletSetUpStatus from a JSON string
embedded_wallet_set_up_status_instance = EmbeddedWalletSetUpStatus.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletSetUpStatus.to_json())

# convert the object into a dict
embedded_wallet_set_up_status_dict = embedded_wallet_set_up_status_instance.to_dict()
# create an instance of EmbeddedWalletSetUpStatus from a dict
embedded_wallet_set_up_status_from_dict = EmbeddedWalletSetUpStatus.from_dict(embedded_wallet_set_up_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


