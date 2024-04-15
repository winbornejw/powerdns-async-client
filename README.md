# powerdns-async-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.15
- Package version: 5.0.3
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import powerdns_async_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import powerdns_async_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import powerdns_async_client
from powerdns_async_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = powerdns_async_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = powerdns_async_client.AutoprimaryApi(powerdns_async_client.ApiClient(configuration))
body = powerdns_async_client.Autoprimary() # Autoprimary | autoprimary entry to add
server_id = 'server_id_example' # str | The id of the server to manage the list of autoprimaries on

try:
    # Add an autoprimary
    api_instance.create_autoprimary(body, server_id)
except ApiException as e:
    print("Exception when calling AutoprimaryApi->create_autoprimary: %s\n" % e)

# Configure API key authorization: APIKeyHeader
configuration = powerdns_async_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = powerdns_async_client.AutoprimaryApi(powerdns_async_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to delete the autoprimary from
ip = 'ip_example' # str | IP address of autoprimary
nameserver = 'nameserver_example' # str | DNS name of the autoprimary

try:
    # Delete the autoprimary entry
    api_instance.delete_autoprimary(server_id, ip, nameserver)
except ApiException as e:
    print("Exception when calling AutoprimaryApi->delete_autoprimary: %s\n" % e)

# Configure API key authorization: APIKeyHeader
configuration = powerdns_async_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = powerdns_async_client.AutoprimaryApi(powerdns_async_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to manage the list of autoprimaries on

try:
    # Get a list of autoprimaries
    api_response = api_instance.get_autoprimaries(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoprimaryApi->get_autoprimaries: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutoprimaryApi* | [**create_autoprimary**](docs/AutoprimaryApi.md#create_autoprimary) | **POST** /servers/{server_id}/autoprimaries | Add an autoprimary
*AutoprimaryApi* | [**delete_autoprimary**](docs/AutoprimaryApi.md#delete_autoprimary) | **DELETE** /servers/{server_id}/autoprimaries/{ip}/{nameserver} | Delete the autoprimary entry
*AutoprimaryApi* | [**get_autoprimaries**](docs/AutoprimaryApi.md#get_autoprimaries) | **GET** /servers/{server_id}/autoprimaries | Get a list of autoprimaries
*ConfigApi* | [**get_config**](docs/ConfigApi.md#get_config) | **GET** /servers/{server_id}/config | Returns all ConfigSettings for a single server
*ConfigApi* | [**get_config_setting**](docs/ConfigApi.md#get_config_setting) | **GET** /servers/{server_id}/config/{config_setting_name} | Returns a specific ConfigSetting for a single server
*DefaultApi* | [**error**](docs/DefaultApi.md#error) | **GET** /error | Will always generate an error
*SearchApi* | [**search_data**](docs/SearchApi.md#search_data) | **GET** /servers/{server_id}/search-data | Search the data inside PowerDNS
*ServersApi* | [**cache_flush_by_name**](docs/ServersApi.md#cache_flush_by_name) | **PUT** /servers/{server_id}/cache/flush | Flush a cache-entry by name
*ServersApi* | [**list_server**](docs/ServersApi.md#list_server) | **GET** /servers/{server_id} | List a server
*ServersApi* | [**list_servers**](docs/ServersApi.md#list_servers) | **GET** /servers | List all servers
*StatsApi* | [**get_stats**](docs/StatsApi.md#get_stats) | **GET** /servers/{server_id}/statistics | Query statistics.
*TsigkeyApi* | [**create_tsig_key**](docs/TsigkeyApi.md#create_tsig_key) | **POST** /servers/{server_id}/tsigkeys | Add a TSIG key
*TsigkeyApi* | [**delete_tsig_key**](docs/TsigkeyApi.md#delete_tsig_key) | **DELETE** /servers/{server_id}/tsigkeys/{tsigkey_id} | Delete the TSIGKey with tsigkey_id
*TsigkeyApi* | [**get_tsig_key**](docs/TsigkeyApi.md#get_tsig_key) | **GET** /servers/{server_id}/tsigkeys/{tsigkey_id} | Get a specific TSIGKeys on the server, including the actual key
*TsigkeyApi* | [**list_tsig_keys**](docs/TsigkeyApi.md#list_tsig_keys) | **GET** /servers/{server_id}/tsigkeys | Get all TSIGKeys on the server, except the actual key
*TsigkeyApi* | [**put_tsig_key**](docs/TsigkeyApi.md#put_tsig_key) | **PUT** /servers/{server_id}/tsigkeys/{tsigkey_id} | 
*ZonecryptokeyApi* | [**create_cryptokey**](docs/ZonecryptokeyApi.md#create_cryptokey) | **POST** /servers/{server_id}/zones/{zone_id}/cryptokeys | Creates a Cryptokey
*ZonecryptokeyApi* | [**delete_cryptokey**](docs/ZonecryptokeyApi.md#delete_cryptokey) | **DELETE** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method deletes a key specified by cryptokey_id.
*ZonecryptokeyApi* | [**get_cryptokey**](docs/ZonecryptokeyApi.md#get_cryptokey) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | Returns all data about the CryptoKey, including the privatekey.
*ZonecryptokeyApi* | [**list_cryptokeys**](docs/ZonecryptokeyApi.md#list_cryptokeys) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys | Get all CryptoKeys for a zone, except the privatekey
*ZonecryptokeyApi* | [**modify_cryptokey**](docs/ZonecryptokeyApi.md#modify_cryptokey) | **PUT** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method (de)activates a key from zone_name specified by cryptokey_id
*ZonemetadataApi* | [**create_metadata**](docs/ZonemetadataApi.md#create_metadata) | **POST** /servers/{server_id}/zones/{zone_id}/metadata | Creates a set of metadata entries
*ZonemetadataApi* | [**delete_metadata**](docs/ZonemetadataApi.md#delete_metadata) | **DELETE** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Delete all items of a single kind of domain metadata.
*ZonemetadataApi* | [**get_metadata**](docs/ZonemetadataApi.md#get_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Get the content of a single kind of domain metadata as a Metadata object.
*ZonemetadataApi* | [**list_metadata**](docs/ZonemetadataApi.md#list_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata | Get all the Metadata associated with the zone.
*ZonemetadataApi* | [**modify_metadata**](docs/ZonemetadataApi.md#modify_metadata) | **PUT** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Replace the content of a single kind of domain metadata.
*ZonesApi* | [**axfr_export_zone**](docs/ZonesApi.md#axfr_export_zone) | **GET** /servers/{server_id}/zones/{zone_id}/export | Returns the zone in AXFR format.
*ZonesApi* | [**axfr_retrieve_zone**](docs/ZonesApi.md#axfr_retrieve_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/axfr-retrieve | Retrieve slave zone from its master.
*ZonesApi* | [**create_zone**](docs/ZonesApi.md#create_zone) | **POST** /servers/{server_id}/zones | Creates a new domain, returns the Zone on creation.
*ZonesApi* | [**delete_zone**](docs/ZonesApi.md#delete_zone) | **DELETE** /servers/{server_id}/zones/{zone_id} | Deletes this zone, all attached metadata and rrsets.
*ZonesApi* | [**list_zone**](docs/ZonesApi.md#list_zone) | **GET** /servers/{server_id}/zones/{zone_id} | zone managed by a server
*ZonesApi* | [**list_zones**](docs/ZonesApi.md#list_zones) | **GET** /servers/{server_id}/zones | List all Zones in a server
*ZonesApi* | [**notify_zone**](docs/ZonesApi.md#notify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/notify | Send a DNS NOTIFY to all slaves.
*ZonesApi* | [**patch_zone**](docs/ZonesApi.md#patch_zone) | **PATCH** /servers/{server_id}/zones/{zone_id} | Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.
*ZonesApi* | [**put_zone**](docs/ZonesApi.md#put_zone) | **PUT** /servers/{server_id}/zones/{zone_id} | Modifies basic zone data.
*ZonesApi* | [**rectify_zone**](docs/ZonesApi.md#rectify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/rectify | Rectify the zone data.

## Documentation For Models

 - [Autoprimary](docs/Autoprimary.md)
 - [CacheFlushResult](docs/CacheFlushResult.md)
 - [Comment](docs/Comment.md)
 - [ConfigSetting](docs/ConfigSetting.md)
 - [Cryptokey](docs/Cryptokey.md)
 - [Error](docs/Error.md)
 - [MapStatisticItem](docs/MapStatisticItem.md)
 - [Metadata](docs/Metadata.md)
 - [RRSet](docs/RRSet.md)
 - [Record](docs/Record.md)
 - [RingStatisticItem](docs/RingStatisticItem.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultComment](docs/SearchResultComment.md)
 - [SearchResultRecord](docs/SearchResultRecord.md)
 - [SearchResultZone](docs/SearchResultZone.md)
 - [SearchResults](docs/SearchResults.md)
 - [Server](docs/Server.md)
 - [Servers](docs/Servers.md)
 - [SimpleStatisticItem](docs/SimpleStatisticItem.md)
 - [StatisticItem](docs/StatisticItem.md)
 - [TSIGKey](docs/TSIGKey.md)
 - [Zone](docs/Zone.md)
 - [Zones](docs/Zones.md)

## Documentation For Authorization


## APIKeyHeader

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author

