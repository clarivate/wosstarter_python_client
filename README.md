# clarivate-wos-starter-python-client
The Web of Science™ Starter API provides basic metadata and search functionality for Web of Science™ Documents and Journals. Based on your subscription, this API can return times cited of documents.

## Resouces
This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.

The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-starter). You can find more details about the subscription and the Plans.

## Content

You can learn more about content at [Web of Science™ Product Page](https://clarivate.com/webofsciencegroup/solutions/web-of-science/) or in the [Web of Science™ Help](https://webofscience.help.clarivate.com/en-us/Content/home.htm).
The following attributes are available from in the API.
* UID (Unique Identifier)
* Title
* Issue
* Pages
* DOI
* Volume
* Times Cited
* ISSN/eISSN
* ISBN
* PubMed ID
* Source
* Web of Science URL
* Citing Articles Web of Science URL
* Publication Date
* Authors
* Author Keywords
* [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html)
* Cited References Web of Science URL
* ResearcherID
* Book DOI
* Related Records Web of Science URL
* Journal Citations Reports URL



## Credentials

All requests require authentication with an API Key authentication flow. For more details, check the [Guide][https://developer.clarivate.com/help/api-access#key_access].

## Search and field tags for Web of Science documents
Web of Science™ offers [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). This API does not support all field tags for documents. [Web of Science API Expanded](https://developer.clarivate.com/apis/wos) offers all available field tags. The following table lists the field tags that are supported by this API.
| Field Tag | Description                                                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TI        | Title of document                                                                                                                                           |
| IS        | ISSN or ISBN                                                                                                                                                |
| SO        | Source title - The result contains all source titles within product database (for example, journal titles and/or book titles if the product includes books) |
| VL        | Volume                                                                                                                                                      |
| PG        | Page                                                                                                                                                        |
| CS        | Issue                                                                                                                                                       |
| PY        | Year Published                                                                                                                                              |
| AU        | Author                                                                                                                                                      |
| AI        | Author Identifier                                                                                                                                                      |
| UT        | Accession Number                                                                                                                                            |
| DO        | DOI                                                                                                                                                         |
| DT        | [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html)                                                                                                                                                         |
| PMID      | PubMed ID                                                                                                                                                   |
| OG        | Search for preferred organization names and/or their name variants from the Preferred Organization Index. <p> A search on a preferred organization name returns all records that contain the preferred name and all records that contain its name variants. A search on a name variant returns all records that contain the variant. For example, Cornell Law Sch returns all records that contain Cornell Law Sch in the Addresses field. <p> When searching for organization names that contain a Boolean (AND, NOT, NEAR, and SAME), always enclose the word in quotation marks ( \" \" ). For example: <p>   - OG=(Japan Science \"and\" Technology Agency (JST))      <br>   - OG=(\"Near\" East Univ)         <br> - OG=(\"OR\" Hlth Sci Univ)                           |
| TS        | Searches for topic terms in the following fields within a document: <p> - Title <br> - Abstract <br> - Author keywords <br> - Keywords Plus
| SUR       | Searches records in DRCI by repository \"SourceURL\". Search values must be inside double quotes

## Pagination
To ensure fast response time, each search or multiple entity calls (such as `/documents`) retrieve only a certain number of hits/records.

There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.

- limit&#58; Number of returned results, ranging from 0 to 50 (default **10**)
- page&#58; Specifying a page to retrieve (default **1**)

Moreover, this information is shown in the response body, in the tag **metadata**&#58;

```json
\"metadata\": {
  \"total\": 91,
  \"page\": 1,
  \"limit\": 10
}
```

## Errors
The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.

| Code  | Title  | Description |
|---|---|---|
| 400  | Bad request  | Request syntax error |
| 401  | Unauthorized  | The API key is invalid or missed |
| 404  | Not found  | The resource is not found |
| 405 | Method not allowed | Method other than GET is not allowed |
| 50X  | Server errors  | Technical error with servers|

Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:

```json
  \"error\": {
    \"status\": 404,
    \"title\": \"Resource couldn't be found\",
    \"details\": \"There is no record found in the Web of Science database. Please check your query.\"
  }
```
For the `401 Unauthorized` error the response body is a little bit different:
```json
{
  \"error_description\": \"The access token is missing\",
  \"error\": \"invalid_request\"
}
```

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clarivate.wos_starter.client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clarivate.wos_starter.client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import os
import time
import clarivate.wos_starter.client
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
    modified_time_span = None # str | Defines a date range in which the results were most recently modified. Beginning and end dates must be specified in the yyyy-mm-dd format separated by '+' or ' ', e.g. 2023-01-01+2023-12-31. This parameter is not compatible with the all databases search, i.e. db=WOK is not compatible with this parameter. (optional)
    tc_modified_time_span = None # str | Defines a date range in which times cited counts were modified. Beginning and end dates must be specified in the yyyy-mm-dd format separated by '+' or ' ', e.g. 2023-01-01+2023-12-31. This parameter is not compatible with the all databases search, i.e. db=WOK is not compatible with this parameter. (optional)
    detail = None # str | it will returns the full data by default, if detail=short it returns the limited data (optional)

    try:
        # Query Web of Science documents 
        api_response = api_instance.documents_get(q, db=db, limit=limit, page=page, sort_field=sort_field, modified_time_span=modified_time_span, tc_modified_time_span=tc_modified_time_span, detail=detail)
        print("The response of DocumentsApi->documents_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->documents_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://api.clarivate.com/apis/wos-starter/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DocumentsApi* | [**documents_get**](docs/DocumentsApi.md#documents_get) | **GET** /documents | Query Web of Science documents 
*DocumentsApi* | [**documents_uid_get**](docs/DocumentsApi.md#documents_uid_get) | **GET** /documents/{uid} | Get Web of Science document by Accesssion Number (UID)
*JournalsApi* | [**journals_get**](docs/JournalsApi.md#journals_get) | **GET** /journals | Query Journals by ISSN
*JournalsApi* | [**journals_id_get**](docs/JournalsApi.md#journals_id_get) | **GET** /journals/{id} | Get Journal by ID


## Documentation For Models

 - [AuthorName](docs/AuthorName.md)
 - [Document](docs/Document.md)
 - [DocumentCitationsInner](docs/DocumentCitationsInner.md)
 - [DocumentIdentifiers](docs/DocumentIdentifiers.md)
 - [DocumentKeywords](docs/DocumentKeywords.md)
 - [DocumentLinks](docs/DocumentLinks.md)
 - [DocumentNames](docs/DocumentNames.md)
 - [DocumentSource](docs/DocumentSource.md)
 - [DocumentSourcePages](docs/DocumentSourcePages.md)
 - [DocumentsList](docs/DocumentsList.md)
 - [Journal](docs/Journal.md)
 - [JournalLinksInner](docs/JournalLinksInner.md)
 - [JournalsList](docs/JournalsList.md)
 - [Metadata](docs/Metadata.md)
 - [OtherName](docs/OtherName.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ClarivateApiKeyAuth"></a>
### ClarivateApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-ApiKey
- **Location**: HTTP header


## Author




