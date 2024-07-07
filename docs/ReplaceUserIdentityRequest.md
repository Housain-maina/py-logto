# ReplaceUserIdentityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s social identity ID. | 
**details** | **object** | The user&#39;s social identity details. | [optional] 

## Example

```python
from py_logto.models.replace_user_identity_request import ReplaceUserIdentityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceUserIdentityRequest from a JSON string
replace_user_identity_request_instance = ReplaceUserIdentityRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceUserIdentityRequest.to_json())

# convert the object into a dict
replace_user_identity_request_dict = replace_user_identity_request_instance.to_dict()
# create an instance of ReplaceUserIdentityRequest from a dict
replace_user_identity_request_from_dict = ReplaceUserIdentityRequest.from_dict(replace_user_identity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


