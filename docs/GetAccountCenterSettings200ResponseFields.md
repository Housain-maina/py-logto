# GetAccountCenterSettings200ResponseFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**social** | **str** |  | [optional] 
**custom_data** | **str** |  | [optional] 

## Example

```python
from py_logto.models.get_account_center_settings200_response_fields import GetAccountCenterSettings200ResponseFields

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountCenterSettings200ResponseFields from a JSON string
get_account_center_settings200_response_fields_instance = GetAccountCenterSettings200ResponseFields.from_json(json)
# print the JSON string representation of the object
print(GetAccountCenterSettings200ResponseFields.to_json())

# convert the object into a dict
get_account_center_settings200_response_fields_dict = get_account_center_settings200_response_fields_instance.to_dict()
# create an instance of GetAccountCenterSettings200ResponseFields from a dict
get_account_center_settings200_response_fields_from_dict = GetAccountCenterSettings200ResponseFields.from_dict(get_account_center_settings200_response_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


