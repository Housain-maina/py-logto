# ListUserMfaVerifications200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **str** |  | 
**type** | **str** |  | 
**agent** | **str** |  | [optional] 
**remain_codes** | **float** |  | [optional] 

## Example

```python
from py_logto.models.list_user_mfa_verifications200_response_inner import ListUserMfaVerifications200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserMfaVerifications200ResponseInner from a JSON string
list_user_mfa_verifications200_response_inner_instance = ListUserMfaVerifications200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListUserMfaVerifications200ResponseInner.to_json())

# convert the object into a dict
list_user_mfa_verifications200_response_inner_dict = list_user_mfa_verifications200_response_inner_instance.to_dict()
# create an instance of ListUserMfaVerifications200ResponseInner from a dict
list_user_mfa_verifications200_response_inner_from_dict = ListUserMfaVerifications200ResponseInner.from_dict(list_user_mfa_verifications200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


