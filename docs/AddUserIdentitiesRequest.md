# AddUserIdentitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_identifier_verification_record_id** | **str** | The identifier verification record ID for the new social identity ownership verification. | 

## Example

```python
from py_logto.models.add_user_identities_request import AddUserIdentitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserIdentitiesRequest from a JSON string
add_user_identities_request_instance = AddUserIdentitiesRequest.from_json(json)
# print the JSON string representation of the object
print(AddUserIdentitiesRequest.to_json())

# convert the object into a dict
add_user_identities_request_dict = add_user_identities_request_instance.to_dict()
# create an instance of AddUserIdentitiesRequest from a dict
add_user_identities_request_from_dict = AddUserIdentitiesRequest.from_dict(add_user_identities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


