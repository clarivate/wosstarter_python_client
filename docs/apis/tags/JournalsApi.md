<a name="__pageTop"></a>
# clarivate.wos_starter.client.apis.tags.journals_api.JournalsApi

All URIs are relative to *http://api.clarivate.com/apis/wos-starter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journals_get**](#journals_get) | **get** /journals | Query Journals by ISSN
[**journals_id_get**](#journals_id_get) | **get** /journals/{id} | Get Journal by ID

# **journals_get**
<a name="journals_get"></a>
> JournalsList journals_get()

Query Journals by ISSN

### Example

```python
import clarivate.wos_starter.client
from clarivate.wos_starter.client.apis.tags import journals_api
from clarivate.wos_starter.client.model.journals_list import JournalsList
from pprint import pprint
# Defining the host is optional and defaults to http://api.clarivate.com/apis/wos-starter
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://api.clarivate.com/apis/wos-starter"
)

# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = journals_api.JournalsApi(api_client)

    # example passing only optional values
    query_params = {
        'issn': "issn_example",
    }
    try:
        # Query Journals by ISSN
        api_response = api_instance.journals_get(
            query_params=query_params,
        )
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling JournalsApi->journals_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
issn | IssnSchema | | optional


# IssnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#journals_get.ApiResponseFor200) | OK

#### journals_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JournalsList**](../../models/JournalsList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **journals_id_get**
<a name="journals_id_get"></a>
> Journal journals_id_get(id)

Get Journal by ID

### Example

```python
import clarivate.wos_starter.client
from clarivate.wos_starter.client.apis.tags import journals_api
from clarivate.wos_starter.client.model.journal import Journal
from pprint import pprint
# Defining the host is optional and defaults to http://api.clarivate.com/apis/wos-starter
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://api.clarivate.com/apis/wos-starter"
)

# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = journals_api.JournalsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "ANAT_REC_PART_A",
    }
    try:
        # Get Journal by ID
        api_response = api_instance.journals_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling JournalsApi->journals_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#journals_id_get.ApiResponseFor200) | OK

#### journals_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Journal**](../../models/Journal.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

