# UpdateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | [**UpdateUserRequestUsername**](UpdateUserRequestUsername.md) |  | [optional] 
**primary_email** | [**UpdateUserRequestPrimaryEmail**](UpdateUserRequestPrimaryEmail.md) |  | [optional] 
**primary_phone** | [**UpdateUserRequestPrimaryPhone**](UpdateUserRequestPrimaryPhone.md) |  | [optional] 
**name** | [**UpdateUserRequestName**](UpdateUserRequestName.md) |  | [optional] 
**avatar** | [**UpdateUserRequestAvatar**](UpdateUserRequestAvatar.md) |  | [optional] 
**custom_data** | **object** | Custom data object to update for the given user ID. Note this will replace the entire custom data object.  If you want to perform a partial update, use the &#x60;PATCH /api/users/{userId}/custom-data&#x60; endpoint instead. | [optional] 
**profile** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md) |  | [optional] 

## Example

```python
from py_logto.models.update_user_request import UpdateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequest from a JSON string
update_user_request_instance = UpdateUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequest.to_json())

# convert the object into a dict
update_user_request_dict = update_user_request_instance.to_dict()
# create an instance of UpdateUserRequest from a dict
update_user_request_from_dict = UpdateUserRequest.from_dict(update_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


