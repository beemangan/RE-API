<a name="__pageTop"></a>
# rec.apis.tags.program_api.ProgramApi

All URIs are relative to *https://www.robotevents.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**program_get_program**](#program_get_program) | **get** /programs/{id} | 
[**program_get_programs**](#program_get_programs) | **get** /programs | 

# **program_get_program**
<a name="program_get_program"></a>
> Program program_get_program(id)



Find a single Program by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import rec
from rec.apis.tags import program_api
from rec.model.program import Program
from pprint import pprint
# Defining the host is optional and defaults to https://www.robotevents.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = rec.Configuration(
    host = "https://www.robotevents.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = rec.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with rec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = program_api.ProgramApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        api_response = api_instance.program_get_program(
            path_params=path_params,
        )
        pprint(api_response)
    except rec.ApiException as e:
        print("Exception when calling ProgramApi->program_get_program: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#program_get_program.ApiResponseFor200) | Single Program

#### program_get_program.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Program**](../../models/Program.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **program_get_programs**
<a name="program_get_programs"></a>
> PaginatedProgram program_get_programs()



Gets a List of Programs

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import rec
from rec.apis.tags import program_api
from rec.model.paginated_program import PaginatedProgram
from pprint import pprint
# Defining the host is optional and defaults to https://www.robotevents.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = rec.Configuration(
    host = "https://www.robotevents.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = rec.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with rec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = program_api.ProgramApi(api_client)

    # example passing only optional values
    query_params = {
        'id[]': [
        1
    ],
    }
    try:
        api_response = api_instance.program_get_programs(
            query_params=query_params,
        )
        pprint(api_response)
    except rec.ApiException as e:
        print("Exception when calling ProgramApi->program_get_programs: %s\n" % e)
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
id[] | IdSchema | | optional


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#program_get_programs.ApiResponseFor200) | List of Programs

#### program_get_programs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedProgram**](../../models/PaginatedProgram.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

