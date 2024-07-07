# UpdateUserCustomDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data** | **object** | Partial custom data object to update for the given user ID. | 

## Example

```python
from py_logto.models.update_user_custom_data_request import UpdateUserCustomDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserCustomDataRequest from a JSON string
update_user_custom_data_request_instance = UpdateUserCustomDataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserCustomDataRequest.to_json())

# convert the object into a dict
update_user_custom_data_request_dict = update_user_custom_data_request_instance.to_dict()
# create an instance of UpdateUserCustomDataRequest from a dict
update_user_custom_data_request_from_dict = UpdateUserCustomDataRequest.from_dict(update_user_custom_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


