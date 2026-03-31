# ManifestQuoteInfo

Defines requirements for the POST /quotes endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_types** | [**List[DVPSettlementType]**](DVPSettlementType.md) | Supported settlement types when requesting a quote. If present - settlement is required. If absent - no need to provide settlement.  | [optional] 

## Example

```python
from fireblocks.models.manifest_quote_info import ManifestQuoteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestQuoteInfo from a JSON string
manifest_quote_info_instance = ManifestQuoteInfo.from_json(json)
# print the JSON string representation of the object
print(ManifestQuoteInfo.to_json())

# convert the object into a dict
manifest_quote_info_dict = manifest_quote_info_instance.to_dict()
# create an instance of ManifestQuoteInfo from a dict
manifest_quote_info_from_dict = ManifestQuoteInfo.from_dict(manifest_quote_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


