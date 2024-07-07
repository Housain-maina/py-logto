# UpdateUserRequestPrimaryPhone

Updated primary phone number for the user. It should be unique across all users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from py_logto.models.update_user_request_primary_phone import UpdateUserRequestPrimaryPhone

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestPrimaryPhone from a JSON string
update_user_request_primary_phone_instance = UpdateUserRequestPrimaryPhone.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestPrimaryPhone.to_json())

# convert the object into a dict
update_user_request_primary_phone_dict = update_user_request_primary_phone_instance.to_dict()
# create an instance of UpdateUserRequestPrimaryPhone from a dict
update_user_request_primary_phone_from_dict = UpdateUserRequestPrimaryPhone.from_dict(update_user_request_primary_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


