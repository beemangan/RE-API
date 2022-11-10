# openapi_client.model.award.Award

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**event** | [**IdInfo**](IdInfo.md) | [**IdInfo**](IdInfo.md) |  | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**title** | str,  | str,  |  | [optional] 
**[qualifications](#qualifications)** | list, tuple,  | tuple,  |  | [optional] 
**designation** | None, str,  | NoneClass, str,  | Some awards are given out per tournament or division | [optional] must be one of ["tournament", "division", ] 
**classification** | None, str,  | NoneClass, str,  |  | [optional] must be one of ["champion", "finalist", "semifinalist", "quarterfinalist", ] 
**[teamWinners](#teamWinners)** | list, tuple,  | tuple,  |  | [optional] 
**[individualWinners](#individualWinners)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# qualifications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# teamWinners

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TeamAwardWinner**](TeamAwardWinner.md) | [**TeamAwardWinner**](TeamAwardWinner.md) | [**TeamAwardWinner**](TeamAwardWinner.md) |  | 

# individualWinners

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

