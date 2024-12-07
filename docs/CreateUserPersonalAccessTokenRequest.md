# CreateUserPersonalAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The personal access token name. Must be unique within the user. | 
**expires_at** | **float** | The epoch time in milliseconds when the token will expire. If not provided, the token will never expire. | [optional] 

## Example

```python
from py_logto.models.create_user_personal_access_token_request import CreateUserPersonalAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserPersonalAccessTokenRequest from a JSON string
create_user_personal_access_token_request_instance = CreateUserPersonalAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserPersonalAccessTokenRequest.to_json())

# convert the object into a dict
create_user_personal_access_token_request_dict = create_user_personal_access_token_request_instance.to_dict()
# create an instance of CreateUserPersonalAccessTokenRequest from a dict
create_user_personal_access_token_request_from_dict = CreateUserPersonalAccessTokenRequest.from_dict(create_user_personal_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


