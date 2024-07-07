# UpdateUserRequestPrimaryEmail

Updated primary email address for the user. It should be unique across all users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from py_logto.models.update_user_request_primary_email import UpdateUserRequestPrimaryEmail

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestPrimaryEmail from a JSON string
update_user_request_primary_email_instance = UpdateUserRequestPrimaryEmail.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestPrimaryEmail.to_json())

# convert the object into a dict
update_user_request_primary_email_dict = update_user_request_primary_email_instance.to_dict()
# create an instance of UpdateUserRequestPrimaryEmail from a dict
update_user_request_primary_email_from_dict = UpdateUserRequestPrimaryEmail.from_dict(update_user_request_primary_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


