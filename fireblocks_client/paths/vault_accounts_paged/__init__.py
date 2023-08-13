# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from fireblocks_client.paths.vault_accounts_paged import Api

from fireblocks_client.paths import PathValues

path = PathValues.VAULT_ACCOUNTS_PAGED