# clarivate.wos_starter.client.DocumentsApi

All URIs are relative to *http://api.clarivate.com/apis/wos-starter/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_get**](DocumentsApi.md#documents_get) | **GET** /documents | Query Web of Science documents 
[**documents_uid_get**](DocumentsApi.md#documents_uid_get) | **GET** /documents/{uid} | Get Web of Science document by Accesssion Number (UID)


# **documents_get**
> DocumentsList documents_get(q, db=db, limit=limit, page=page, sort_field=sort_field, modified_time_span=modified_time_span, tc_modified_time_span=tc_modified_time_span, detail=detail)

Query Web of Science documents 

The endpoint allows to search, filter, or browse across the Web of Science document content by using [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). The following table lists the field tags that are supported by this API. | Field Tag | Description                                                                                                                                                 | |-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------| | TI        | Title of document                                                                                                                                           | | IS        | ISSN or ISBN                                                                                                                                                | | SO        | Source title - The result contains all source titles within product database (for example, journal titles and/or book titles if the product includes books) | | VL        | Volume                                                                                                                                                      | | PG        | Page                                                                                                                                                        | | CS        | Issue                                                                                                                                                       | | PY        | Year Published                                                                                                                                              | | AU        | Author                                                                                                                                                      | | AI        | Author Identifier                                                                                                                                                      | | UT        | Accession Number                                                                                                                                            | | DO        | DOI                                                                                                                                                         | | DT        | Document Type                                                                                                                                                          | | PMID      | PubMed ID                                                                                                                                                   | | OG        | Search for preferred organization names and/or their name variants from the Preferred Organization Index. <p> A search on a preferred organization name returns all records that contain the preferred name and all records that contain its name variants. A search on a name variant returns all records that contain the variant. For example, Cornell Law Sch returns all records that contain Cornell Law Sch in the Addresses field. <p> When searching for organization names that contain a Boolean (AND, NOT, NEAR, and SAME), always enclose the word in quotation marks ( \" \" ). For example: <p>   - OG=(Japan Science \"and\" Technology Agency (JST))      <br>   - OG=(\"Near\" East Univ)         <br> - OG=(\"OR\" Hlth Sci Univ)                           | | TS        | Searches for topic terms in the following fields within a document: <p> - Title <br> - Abstract <br> - Author keywords <br> - Keywords Plus | SUR       | Searches records in DRCI by repository \"SourceURL\". Search values must be inside double quotes 

### Example

* Api Key Authentication (ClarivateApiKeyAuth):

```python
import time
import os
import clarivate.wos_starter.client
from clarivate.wos_starter.client.models.documents_list import DocumentsList
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
    api_instance = clarivate.wos_starter.client.DocumentsApi(api_client)
    q = 'PY=2020' # str | Web of Science advanced [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). The supported field tags are listed in description.
    db = 'WOS' # str | Web of Science Database abbreviation * WOS - Web of Science Core collection * BIOABS - Biological Abstracts * BCI - BIOSIS Citation Index * BIOSIS - BIOSIS Previews * CCC - Current Contents Connect * DIIDW - Derwent Innovations Index * DRCI - Data Citation Index * MEDLINE - MEDLINE The U.S. National Library of Medicine® (NLM®) premier life sciences database. * ZOOREC - Zoological Records * PPRN - Preprint Citation Index * WOK - All databases  (optional) (default to 'WOS')
    limit = 10 # int | set the limit of records on the page (1-50) (optional) (default to 10)
    page = 1 # int | set the result page (optional) (default to 1)
    sort_field = 'LD+D' # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. Supported fields:  * **LD** - Load Date * **PY** - Publication Year * **RS** - Relevance * **TC** - Times Cited  (optional)
    modified_time_span = 'modified_time_span_example' # str | Defines a date range in which the results were most recently modified. Beginning and end dates must be specified in the yyyy-mm-dd format separated by '+' or ' ', e.g. 2023-01-01+2023-12-31. This parameter is not compatible with the all databases search, i.e. db=WOK is not compatible with this parameter. (optional)
    tc_modified_time_span = 'tc_modified_time_span_example' # str | Defines a date range in which times cited counts were modified. Beginning and end dates must be specified in the yyyy-mm-dd format separated by '+' or ' ', e.g. 2023-01-01+2023-12-31. This parameter is not compatible with the all databases search, i.e. db=WOK is not compatible with this parameter. (optional)
    detail = 'detail_example' # str | it will returns the full data by default, if detail=short it returns the limited data (optional)

    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(q, db=db, limit=limit, page=page, sort_field=sort_field, modified_time_span=modified_time_span, tc_modified_time_span=tc_modified_time_span, detail=detail)
        print("The response of DocumentsApi->documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Web of Science advanced [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). The supported field tags are listed in description. | 
 **db** | **str**| Web of Science Database abbreviation * WOS - Web of Science Core collection * BIOABS - Biological Abstracts * BCI - BIOSIS Citation Index * BIOSIS - BIOSIS Previews * CCC - Current Contents Connect * DIIDW - Derwent Innovations Index * DRCI - Data Citation Index * MEDLINE - MEDLINE The U.S. National Library of Medicine® (NLM®) premier life sciences database. * ZOOREC - Zoological Records * PPRN - Preprint Citation Index * WOK - All databases  | [optional] [default to &#39;WOS&#39;]
 **limit** | **int**| set the limit of records on the page (1-50) | [optional] [default to 10]
 **page** | **int**| set the result page | [optional] [default to 1]
 **sort_field** | **str**| Order by field(s). Field name and order by clause separated by &#39;+&#39;, use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. Supported fields:  * **LD** - Load Date * **PY** - Publication Year * **RS** - Relevance * **TC** - Times Cited  | [optional] 
 **modified_time_span** | **str**| Defines a date range in which the results were most recently modified. Beginning and end dates must be specified in the yyyy-mm-dd format separated by &#39;+&#39; or &#39; &#39;, e.g. 2023-01-01+2023-12-31. This parameter is not compatible with the all databases search, i.e. db&#x3D;WOK is not compatible with this parameter. | [optional] 
 **tc_modified_time_span** | **str**| Defines a date range in which times cited counts were modified. Beginning and end dates must be specified in the yyyy-mm-dd format separated by &#39;+&#39; or &#39; &#39;, e.g. 2023-01-01+2023-12-31. This parameter is not compatible with the all databases search, i.e. db&#x3D;WOK is not compatible with this parameter. | [optional] 
 **detail** | **str**| it will returns the full data by default, if detail&#x3D;short it returns the limited data | [optional] 

### Return type

[**DocumentsList**](DocumentsList.md)

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

# **documents_uid_get**
> Document documents_uid_get(uid, detail=detail)

Get Web of Science document by Accesssion Number (UID)

Get Web of Science document by Accesssion Number (UID)

### Example

* Api Key Authentication (ClarivateApiKeyAuth):

```python
import time
import os
import clarivate.wos_starter.client
from clarivate.wos_starter.client.models.document import Document
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
    api_instance = clarivate.wos_starter.client.DocumentsApi(api_client)
    uid = 'WOS:000267144200002' # str | Web of Science unique identifier (Accession Number)
    detail = 'detail_example' # str | it will returns the full data by default, if detail=short it returns the limited data (optional)

    try:
        # Get Web of Science document by Accesssion Number (UID)
        api_response = api_instance.documents_uid_get(uid, detail=detail)
        print("The response of DocumentsApi->documents_uid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_uid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Web of Science unique identifier (Accession Number) | 
 **detail** | **str**| it will returns the full data by default, if detail&#x3D;short it returns the limited data | [optional] 

### Return type

[**Document**](Document.md)

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

