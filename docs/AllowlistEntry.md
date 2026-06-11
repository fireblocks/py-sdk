# AllowlistEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the allowlist entry | 
**address** | **str** | The blockchain address | 
**assets** | **List[str]** | Assets approved for this address.  Each value is either a Fireblocks asset ID (when the provider&#39;s asset maps to a Fireblocks-supported asset) or the raw provider asset symbol (when no mapping exists). Treat values as opaque strings.  Possible combinations:   - One or more specific asset values (e.g., &#x60;[\&quot;BTC\&quot;, \&quot;ETH\&quot;]&#x60;)  See [List assets](https://developers.fireblocks.com/reference/listassets) for the canonical list of Fireblocks asset IDs.  | 
**networks** | **List[str]** | Networks approved for this address.  Each value is either a Fireblocks network ID (when the provider&#39;s network maps to a Fireblocks-supported blockchain) or the raw provider blockchain identifier (when no mapping exists). Treat values as opaque strings.  Possible combinations:   - One or more specific network values (e.g., &#x60;[\&quot;ETHEREUM\&quot;, \&quot;POLYGON\&quot;]&#x60;)  See [List blockchains](https://developers.fireblocks.com/reference/listblockchains) for the canonical list of Fireblocks blockchain identifiers.  | 
**label** | **str** | Human-readable label for the address | [optional] 
**address_identifier** | **str** | Additional identifier (e.g., memo, destination tag) | [optional] 
**status** | [**AllowlistEntryStatus**](AllowlistEntryStatus.md) |  | 
**added_at** | **datetime** | ISO 8601 timestamp when entry was added | 
**provider_reference_id** | **str** | Provider&#39;s internal reference ID | [optional] 
**provider_metadata** | **Dict[str, object]** | Provider-specific pass-through data for this address. Treat as an opaque blob: the shape, set of keys, and value types vary by provider, by entry, and over time. Keys may be added, renamed, or removed without notice as providers evolve their integrations or as new providers are added. The example below illustrates one possible shape and is not a contract — do not program against specific keys.  | [optional] 

## Example

```python
from fireblocks.models.allowlist_entry import AllowlistEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AllowlistEntry from a JSON string
allowlist_entry_instance = AllowlistEntry.from_json(json)
# print the JSON string representation of the object
print(AllowlistEntry.to_json())

# convert the object into a dict
allowlist_entry_dict = allowlist_entry_instance.to_dict()
# create an instance of AllowlistEntry from a dict
allowlist_entry_from_dict = AllowlistEntry.from_dict(allowlist_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


