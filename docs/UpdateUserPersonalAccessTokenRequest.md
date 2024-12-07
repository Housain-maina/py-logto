# UpdateUserPersonalAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The token name to update. Must be unique within the user. | 

## Example

```python
from py_logto.models.update_user_personal_access_token_request import UpdateUserPersonalAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserPersonalAccessTokenRequest from a JSON string
update_user_personal_access_token_request_instance = UpdateUserPersonalAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserPersonalAccessTokenRequest.to_json())

# convert the object into a dict
update_user_personal_access_token_request_dict = update_user_personal_access_token_request_instance.to_dict()
# create an instance of UpdateUserPersonalAccessTokenRequest from a dict
update_user_personal_access_token_request_from_dict = UpdateUserPersonalAccessTokenRequest.from_dict(update_user_personal_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


