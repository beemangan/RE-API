# openapi_client.model.event.Event

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**season** | [**IdInfo**](IdInfo.md) | [**IdInfo**](IdInfo.md) |  | 
**location** | [**Location**](Location.md) | [**Location**](Location.md) |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**program** | [**IdInfo**](IdInfo.md) | [**IdInfo**](IdInfo.md) |  | 
**sku** | str,  | str,  |  | 
**start** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**end** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[divisions](#divisions)** | list, tuple,  | tuple,  |  | [optional] 
**level** | [**EventLevel**](EventLevel.md) | [**EventLevel**](EventLevel.md) |  | [optional] 
**ongoing** | bool,  | BoolClass,  |  | [optional] 
**awards_finalized** | bool,  | BoolClass,  |  | [optional] 
**event_type** | [**EventType**](EventType.md) | [**EventType**](EventType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# divisions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Division**](Division.md) | [**Division**](Division.md) | [**Division**](Division.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

