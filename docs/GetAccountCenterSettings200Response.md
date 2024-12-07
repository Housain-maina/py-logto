# GetAccountCenterSettings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**enabled** | **bool** |  | 
**fields** | [**GetAccountCenterSettings200ResponseFields**](GetAccountCenterSettings200ResponseFields.md) |  | 

## Example

```python
from py_logto.models.get_account_center_settings200_response import GetAccountCenterSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountCenterSettings200Response from a JSON string
get_account_center_settings200_response_instance = GetAccountCenterSettings200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountCenterSettings200Response.to_json())

# convert the object into a dict
get_account_center_settings200_response_dict = get_account_center_settings200_response_instance.to_dict()
# create an instance of GetAccountCenterSettings200Response from a dict
get_account_center_settings200_response_from_dict = GetAccountCenterSettings200Response.from_dict(get_account_center_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


