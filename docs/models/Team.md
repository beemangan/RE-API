# openapi_client.model.team.Team

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | str,  | str,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**program** | [**IdInfo**](IdInfo.md) | [**IdInfo**](IdInfo.md) |  | 
**team_name** | str,  | str,  |  | [optional] 
**robot_name** | str,  | str,  |  | [optional] 
**organization** | str,  | str,  |  | [optional] 
**location** | [**Location**](Location.md) | [**Location**](Location.md) |  | [optional] 
**registered** | bool,  | BoolClass,  |  | [optional] 
**grade** | [**Grade**](Grade.md) | [**Grade**](Grade.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

