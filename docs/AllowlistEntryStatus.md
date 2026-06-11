# AllowlistEntryStatus

Current status of the allowlist entry.   - `ACTIVE` — Entry is approved and usable.   - `PENDING_PROVIDER_COOLDOWN` — Entry was recently added or modified and is in the provider-enforced cooldown window before becoming active.   - `PENDING_PROVIDER_REVIEW` — Entry is awaiting provider-side review.   - `PENDING_APPROVAL` — Entry is awaiting customer/admin approval on the Fireblocks side.   - `REJECTED` — Entry was rejected at submission time and will not become active.   - `REMOVED` — Entry was deactivated after previously being active. May still appear in results for audit purposes. 

## Enum

* `ACTIVE` (value: `'ACTIVE'`)

* `PENDING_PROVIDER_COOLDOWN` (value: `'PENDING_PROVIDER_COOLDOWN'`)

* `PENDING_PROVIDER_REVIEW` (value: `'PENDING_PROVIDER_REVIEW'`)

* `PENDING_APPROVAL` (value: `'PENDING_APPROVAL'`)

* `REJECTED` (value: `'REJECTED'`)

* `REMOVED` (value: `'REMOVED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


