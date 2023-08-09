# Fireblocks SDK

The Fireblocks SDK allows developers to integrate with the Fireblocks platform and perform various operations, such as managing vault accounts and executing transactions.

For detailed documentation and additional resources, please refer to the [Fireblocks Developer Portal](https://developers.fireblocks.com/).

## Installation

To use the Fireblocks SDK, follow these steps:

Install the SDK using npm:

```shell
pip3 @fireblocks/install fireblocks-api-client-python
```

## Usage
You can initialize you environment variables in your env file, or just provide them when you initialize and API module.    
```python
import importlib
import os
import sys
sys.path.insert(0, '../fireblocks-sdk-py')
os.environ["FIREBLOCKS_BASE_PATH"] = 'https://sandbox-api.fireblocks.io/v1'
os.environ["FIREBLOCKS_API_KEY"] = 'cf8e4b36-84ca-4393-9bd9-84dd9bd640c8'
os.environ["FIREBLOCKS_SECRET_KEY"]  = open("./example/fireblocks_secret.key", "r").read()
from client.api.vaults_api import VaultsApi
from client.models.vault_accounts_post_request import VaultAccountsPostRequest
```

Lets see an example. create a vault accounts and make a transaction! 
```python
import importlib
import os
import sys
sys.path.insert(0, '../fireblocks-sdk-py')
os.environ["FIREBLOCKS_BASE_PATH"] = 'https://sandbox-api.fireblocks.io/v1'
os.environ["FIREBLOCKS_API_KEY"] = 'api-key'
os.environ["FIREBLOCKS_SECRET_KEY"]  = open("./example/fireblocks_secret.key", "r").read()
from client.api.vaults_api import VaultsApi
from client.models.vault_accounts_post_request import VaultAccountsPostRequest

def __main__():
try:
body = VaultAccountsPostRequest.from_dict({
"name": "Shahar Test 1"
});
vaults = VaultsApi()
response = vaults.vault_accounts_post(body)
print(response)
response = vaults.vault_accounts_paged_get()
print(response)
except Exception as e: # work on python 3.x
print('Failed to upload to ftp: '+ str(e))

__main__()
```