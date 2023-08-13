# fireblocks_client.model.transfer_peer_path.TransferPeerPath

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | must be one of ["VAULT_ACCOUNT", "EXCHANGE_ACCOUNT", "INTERNAL_WALLET", "EXTERNAL_WALLET", "NETWORK_CONNECTION", "FIAT_ACCOUNT", "COMPOUND", "GAS_STATION", "ONE_TIME_ADDRESS", "UNKNOWN", "END_USER_WALLET", ] 
**subType** | str,  | str,  |  | [optional] must be one of ["BINANCE", "BINANCEUS", "BITFINEX", "BITHUMB", "BITMEX", "BITSO", "BITSTAMP", "BITTREX", "BLINC", "BYBIT", "CIRCLE", "COINBASEEXCHANGE", "COINBASEPRO", "COINMETRO", "COINSPRO", "CRYPTOCOM", "DERIBIT", "GEMINI", "HITBTC", "HUOBI", "INDEPENDENTRESERVE", "KORBIT", "KRAKEN", "KRAKENINTL", "KUCOIN", "LIQUID", "OKCOIN", "OKEX", "PAXOS", "POLONIEX", "External", "Internal", ] 
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**walletId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

