# ListUserPersonalAccessTokens200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**created_at** | **float** |  | 
**expires_at** | **float** |  | 

## Example

```python
from py_logto.models.list_user_personal_access_tokens200_response_inner import ListUserPersonalAccessTokens200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserPersonalAccessTokens200ResponseInner from a JSON string
list_user_personal_access_tokens200_response_inner_instance = ListUserPersonalAccessTokens200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListUserPersonalAccessTokens200ResponseInner.to_json())

# convert the object into a dict
list_user_personal_access_tokens200_response_inner_dict = list_user_personal_access_tokens200_response_inner_instance.to_dict()
# create an instance of ListUserPersonalAccessTokens200ResponseInner from a dict
list_user_personal_access_tokens200_response_inner_from_dict = ListUserPersonalAccessTokens200ResponseInner.from_dict(list_user_personal_access_tokens200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


