# WebhookMtlsKeyAlgorithm

Algorithm of the Fireblocks-held mTLS private key. A workspace may hold one key of each type, so a CSR is always returned for the type requested, and the type is echoed back on the response. ECDSA keys are smaller and quicker to issue, but the certificate authority signing the request has to accept an EC subject key, which some do not by default.

## Enum

* `RSA` (value: `'RSA'`)

* `ECDSA` (value: `'ECDSA'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


