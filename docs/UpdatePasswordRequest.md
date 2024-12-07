# UpdatePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The new password for the user. | 

## Example

```python
from py_logto.models.update_password_request import UpdatePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordRequest from a JSON string
update_password_request_instance = UpdatePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePasswordRequest.to_json())

# convert the object into a dict
update_password_request_dict = update_password_request_instance.to_dict()
# create an instance of UpdatePasswordRequest from a dict
update_password_request_from_dict = UpdatePasswordRequest.from_dict(update_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


