# UpdateUserRequestUsername

Updated username for the user. It should be unique across all users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from py_logto.models.update_user_request_username import UpdateUserRequestUsername

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestUsername from a JSON string
update_user_request_username_instance = UpdateUserRequestUsername.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestUsername.to_json())

# convert the object into a dict
update_user_request_username_dict = update_user_request_username_instance.to_dict()
# create an instance of UpdateUserRequestUsername from a dict
update_user_request_username_from_dict = UpdateUserRequestUsername.from_dict(update_user_request_username_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


