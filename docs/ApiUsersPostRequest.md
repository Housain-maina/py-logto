# ApiUsersPostRequest

User data to create a new user. All properties are optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_phone** | **str** | Primary phone number for the user. It should be unique across all users. | [optional] 
**primary_email** | **str** | Primary email address for the user. It should be unique across all users. | [optional] 
**username** | **str** | Username for the user. It should be unique across all users. | [optional] 
**password** | **str** | Plain text password for the user. | [optional] 
**password_digest** | **str** | In case you already have the password digests and not the passwords, you can use them for the newly created user via this property. The value should be generated with one of the supported algorithms. The algorithm can be specified using the &#x60;passwordAlgorithm&#x60; property. | [optional] 
**password_algorithm** | **str** | The hash algorithm used for the password. It should be one of the supported algorithms: argon2, md5, sha1, sha256. Should the encryption algorithm differ from argon2, it will automatically be upgraded to argon2 upon the user&#39;s next sign-in. | [optional] 
**name** | **str** |  | [optional] 
**avatar** | [**ApiUsersUserIdPatchRequestAvatar**](ApiUsersUserIdPatchRequestAvatar.md) |  | [optional] 
**custom_data** | **object** | arbitrary | [optional] 
**profile** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserProfile.md) |  | [optional] 

## Example

```python
from py_logto.models.api_users_post_request import ApiUsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersPostRequest from a JSON string
api_users_post_request_instance = ApiUsersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersPostRequest.to_json())

# convert the object into a dict
api_users_post_request_dict = api_users_post_request_instance.to_dict()
# create an instance of ApiUsersPostRequest from a dict
api_users_post_request_from_dict = ApiUsersPostRequest.from_dict(api_users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


