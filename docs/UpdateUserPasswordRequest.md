# UpdateUserPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | New password for the user. | 

## Example

```python
from py_logto.models.update_user_password_request import UpdateUserPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserPasswordRequest from a JSON string
update_user_password_request_instance = UpdateUserPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserPasswordRequest.to_json())

# convert the object into a dict
update_user_password_request_dict = update_user_password_request_instance.to_dict()
# create an instance of UpdateUserPasswordRequest from a dict
update_user_password_request_from_dict = UpdateUserPasswordRequest.from_dict(update_user_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


