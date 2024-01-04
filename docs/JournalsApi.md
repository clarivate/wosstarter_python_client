# clarivate.wos_starter.client.JournalsApi

All URIs are relative to *http://api.clarivate.com/apis/wos-starter/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journals_get**](JournalsApi.md#journals_get) | **GET** /journals | Query Journals by ISSN
[**journals_id_get**](JournalsApi.md#journals_id_get) | **GET** /journals/{id} | Get Journal by ID


# **journals_get**
> JournalsList journals_get(issn=issn)

Query Journals by ISSN

### Example

* Api Key Authentication (ClarivateApiKeyAuth):

```python
import time
import os
import clarivate.wos_starter.client
from clarivate.wos_starter.client.models.journals_list import JournalsList
from clarivate.wos_starter.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.clarivate.com/apis/wos-starter/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://api.clarivate.com/apis/wos-starter/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ClarivateApiKeyAuth
configuration.api_key['ClarivateApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClarivateApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clarivate.wos_starter.client.JournalsApi(api_client)
    issn = 'issn_example' # str | Query Journal by ISSN (optional)

    try:
        # Query Journals by ISSN
        api_response = api_instance.journals_get(issn=issn)
        print("The response of JournalsApi->journals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->journals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issn** | **str**| Query Journal by ISSN | [optional] 

### Return type

[**JournalsList**](JournalsList.md)

### Authorization

[ClarivateApiKeyAuth](../README.md#ClarivateApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journals_id_get**
> Journal journals_id_get(id)

Get Journal by ID

### Example

* Api Key Authentication (ClarivateApiKeyAuth):

```python
import time
import os
import clarivate.wos_starter.client
from clarivate.wos_starter.client.models.journal import Journal
from clarivate.wos_starter.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.clarivate.com/apis/wos-starter/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://api.clarivate.com/apis/wos-starter/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ClarivateApiKeyAuth
configuration.api_key['ClarivateApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClarivateApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clarivate.wos_starter.client.JournalsApi(api_client)
    id = 'ANAT_REC_PART_A' # str | 

    try:
        # Get Journal by ID
        api_response = api_instance.journals_id_get(id)
        print("The response of JournalsApi->journals_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->journals_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Journal**](Journal.md)

### Authorization

[ClarivateApiKeyAuth](../README.md#ClarivateApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

