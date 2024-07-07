# CreateUserRequest

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
**avatar** | [**UpdateUserRequestAvatar**](UpdateUserRequestAvatar.md) |  | [optional] 
**custom_data** | **object** | arbitrary | [optional] 
**profile** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md) |  | [optional] 

## Example

```python
from py_logto.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequest.to_json())

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_from_dict = CreateUserRequest.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


