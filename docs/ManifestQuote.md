# ManifestQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | Indicates whether the endpoint is supported by the provider | 
**settlement_types** | [**List[DVPSettlementType]**](DVPSettlementType.md) | Supported settlement types when requesting a quote. If present - settlement is required. If absent - no need to provide settlement.  | [optional] 

## Example

```python
from fireblocks.models.manifest_quote import ManifestQuote

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestQuote from a JSON string
manifest_quote_instance = ManifestQuote.from_json(json)
# print the JSON string representation of the object
print(ManifestQuote.to_json())

# convert the object into a dict
manifest_quote_dict = manifest_quote_instance.to_dict()
# create an instance of ManifestQuote from a dict
manifest_quote_from_dict = ManifestQuote.from_dict(manifest_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


