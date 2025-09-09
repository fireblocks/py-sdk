# ConnectedAccountManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_types** | [**List[ConnectedAccountAssetType]**](ConnectedAccountAssetType.md) | Asset types supported by the connected account. | 
**capabilities** | [**List[ConnectedAccountCapability]**](ConnectedAccountCapability.md) | Features supported for the connected account. Logic: - If account capabilities include ramp -&gt; TRADING - If account capabilities include transfers -&gt; DEPOSITS - If account capabilities include transfersBlockchain / transfersFiat / transfersPeerAccounts / transfersInternal -&gt; WITHDRAWALS  | 

## Example

```python
from fireblocks.models.connected_account_manifest import ConnectedAccountManifest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountManifest from a JSON string
connected_account_manifest_instance = ConnectedAccountManifest.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountManifest.to_json())

# convert the object into a dict
connected_account_manifest_dict = connected_account_manifest_instance.to_dict()
# create an instance of ConnectedAccountManifest from a dict
connected_account_manifest_from_dict = ConnectedAccountManifest.from_dict(connected_account_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


