# ApiUsersUserIdPasswordVerifyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password to verify. | 

## Example

```python
from py_logto.models.api_users_user_id_password_verify_post_request import ApiUsersUserIdPasswordVerifyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdPasswordVerifyPostRequest from a JSON string
api_users_user_id_password_verify_post_request_instance = ApiUsersUserIdPasswordVerifyPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdPasswordVerifyPostRequest.to_json())

# convert the object into a dict
api_users_user_id_password_verify_post_request_dict = api_users_user_id_password_verify_post_request_instance.to_dict()
# create an instance of ApiUsersUserIdPasswordVerifyPostRequest from a dict
api_users_user_id_password_verify_post_request_from_dict = ApiUsersUserIdPasswordVerifyPostRequest.from_dict(api_users_user_id_password_verify_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


