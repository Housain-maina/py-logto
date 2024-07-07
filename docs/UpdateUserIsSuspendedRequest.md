# UpdateUserIsSuspendedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_suspended** | **bool** | New suspension status for the user. | 

## Example

```python
from py_logto.models.update_user_is_suspended_request import UpdateUserIsSuspendedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserIsSuspendedRequest from a JSON string
update_user_is_suspended_request_instance = UpdateUserIsSuspendedRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserIsSuspendedRequest.to_json())

# convert the object into a dict
update_user_is_suspended_request_dict = update_user_is_suspended_request_instance.to_dict()
# create an instance of UpdateUserIsSuspendedRequest from a dict
update_user_is_suspended_request_from_dict = UpdateUserIsSuspendedRequest.from_dict(update_user_is_suspended_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


