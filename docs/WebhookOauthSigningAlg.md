# WebhookOauthSigningAlg

Algorithm of the key pairs Fireblocks holds for OAuth credentials using `private_key_jwt`, and so of the JWT assertions signed with them. `RS256` and `PS256` use RSA 2048-bit keys, `ES256` uses EC P-256 keys. `RS256` is what most authorization servers expect; `PS256` and `ES256` suit servers on a stricter profile, such as FAPI.

## Enum

* `RS256` (value: `'RS256'`)

* `PS256` (value: `'PS256'`)

* `ES256` (value: `'ES256'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


