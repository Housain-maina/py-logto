# AddUserProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of profile data to add. &#x60;email&#x60;, &#x60;phone&#x60;, &#x60;username&#x60;, &#x60;password&#x60;, etc. | [optional] 
**value** | **object** | The plain text value of the profile data. Only supported for profile data types that does not require verification, such as &#x60;username&#x60; and &#x60;password&#x60;. | [optional] 
**verification_id** | **object** | The ID of the verification record used to verify the profile data. Required for profile data types that require verification, such as &#x60;email&#x60;, &#x60;phone&#x60; and &#x60;social&#x60;. | [optional] 

## Example

```python
from py_logto.models.add_user_profile_request import AddUserProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserProfileRequest from a JSON string
add_user_profile_request_instance = AddUserProfileRequest.from_json(json)
# print the JSON string representation of the object
print(AddUserProfileRequest.to_json())

# convert the object into a dict
add_user_profile_request_dict = add_user_profile_request_instance.to_dict()
# create an instance of AddUserProfileRequest from a dict
add_user_profile_request_from_dict = AddUserProfileRequest.from_dict(add_user_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


