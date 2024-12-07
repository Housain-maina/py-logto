# ResetUserPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The new password to update. The password must meet the password policy requirements and can not be the same as the current password. | 

## Example

```python
from py_logto.models.reset_user_password_request import ResetUserPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResetUserPasswordRequest from a JSON string
reset_user_password_request_instance = ResetUserPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(ResetUserPasswordRequest.to_json())

# convert the object into a dict
reset_user_password_request_dict = reset_user_password_request_instance.to_dict()
# create an instance of ResetUserPasswordRequest from a dict
reset_user_password_request_from_dict = ResetUserPasswordRequest.from_dict(reset_user_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


