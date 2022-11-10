# rec.model.match_obj.MatchObj

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**division** | [**IdInfo**](IdInfo.md) | [**IdInfo**](IdInfo.md) |  | 
**instance** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**matchnum** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**round** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**scored** | bool,  | BoolClass,  |  | 
**name** | str,  | str,  |  | 
**[alliances](#alliances)** | list, tuple,  | tuple,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**event** | [**IdInfo**](IdInfo.md) | [**IdInfo**](IdInfo.md) |  | 
**scheduled** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**started** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**field** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# alliances

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Alliance**](Alliance.md) | [**Alliance**](Alliance.md) | [**Alliance**](Alliance.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

