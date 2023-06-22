<a name="__pageTop"></a>
# clarivate.wos_starter.client.apis.tags.documents_api.DocumentsApi

All URIs are relative to *http://api.clarivate.com/apis/wos-starter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_get**](#documents_get) | **get** /documents | Query Web of Science documents 
[**documents_uid_get**](#documents_uid_get) | **get** /documents/{uid} | Get Web of Science document by Accesssion Number (UID)

# **documents_get**
<a name="documents_get"></a>
> DocumentsList documents_get(q)

Query Web of Science documents 

The endpoint allows to search, filter, or browse across the Web of Science document content by using [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). The following table lists the field tags that are supported by this API. | Field Tag | Description                                                                                                                                                 | |-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------| | TI        | Title of document                                                                                                                                           | | IS        | ISSN or ISBN                                                                                                                                                | | SO        | Source title - The result contains all source titles within product database (for example, journal titles and/or book titles if the product includes books) | | VL        | Volume                                                                                                                                                      | | PG        | Page                                                                                                                                                        | | CS        | Issue                                                                                                                                                       | | PY        | Year Published                                                                                                                                              | | AU        | Author                                                                                                                                                      | | AI        | Author Identifier                                                                                                                                                      | | UT        | Accession Number                                                                                                                                            | | DO        | DOI                                                                                                                                                         | | DT        | Document Type                                                                                                                                                          | | PMID      | PubMed ID                                                                                                                                                   | | OG        | Search for preferred organization names and/or their name variants from the Preferred Organization Index. <p> A search on a preferred organization name returns all records that contain the preferred name and all records that contain its name variants. A search on a name variant returns all records that contain the variant. For example, Cornell Law Sch returns all records that contain Cornell Law Sch in the Addresses field. <p> When searching for organization names that contain a Boolean (AND, NOT, NEAR, and SAME), always enclose the word in quotation marks ( \" \" ). For example: <p>   - OG=(Japan Science \"and\" Technology Agency (JST))      <br>   - OG=(\"Near\" East Univ)         <br> - OG=(\"OR\" Hlth Sci Univ)                           | | TS        | Searches for topic terms in the following fields within a document: <p> - Title <br> - Abstract <br> - Author keywords <br> - Keywords Plus 

### Example

```python
import clarivate.wos_starter.client
from clarivate.wos_starter.client.apis.tags import documents_api
from clarivate.wos_starter.client.model.documents_list import DocumentsList
from pprint import pprint
# Defining the host is optional and defaults to http://api.clarivate.com/apis/wos-starter
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://api.clarivate.com/apis/wos-starter"
)

# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'q': "PY=2020",
    }
    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(
            query_params=query_params,
        )
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'db': "WOS",
        'q': "PY=2020",
        'limit': 10,
        'page': 1,
        'sortField': "sortField_example",
    }
    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(
            query_params=query_params,
        )
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)
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
db | DbSchema | | optional
q | QSchema | | 
limit | LimitSchema | | optional
page | PageSchema | | optional
sortField | SortFieldSchema | | optional


# DbSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["BCI", "BIOABS", "BIOSIS", "CCC", "DIIDW", "DRCI", "MEDLINE", "PPRN", "WOK", "WOS", "ZOOREC", ] if omitted the server will use the default value of "WOS"

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#documents_get.ApiResponseFor200) | OK

#### documents_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DocumentsList**](../../models/DocumentsList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **documents_uid_get**
<a name="documents_uid_get"></a>
> Document documents_uid_get(uid)

Get Web of Science document by Accesssion Number (UID)

Get Web of Science document by Accesssion Number (UID)

### Example

```python
import clarivate.wos_starter.client
from clarivate.wos_starter.client.apis.tags import documents_api
from clarivate.wos_starter.client.model.document import Document
from pprint import pprint
# Defining the host is optional and defaults to http://api.clarivate.com/apis/wos-starter
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_starter.client.Configuration(
    host = "http://api.clarivate.com/apis/wos-starter"
)

# Enter a context with an instance of the API client
with clarivate.wos_starter.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uid': "WOS:000267144200002",
    }
    try:
        # Get Web of Science document by Accesssion Number (UID)
        api_response = api_instance.documents_uid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except clarivate.wos_starter.client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_uid_get: %s\n" % e)
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
uid | UidSchema | | 

# UidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#documents_uid_get.ApiResponseFor200) | OK

#### documents_uid_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Document**](../../models/Document.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

