# ApiUsersUserIdIdentitiesTargetPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s social identity ID. | 
**details** | **object** | The user&#39;s social identity details. | [optional] 

## Example

```python
from py_logto.models.api_users_user_id_identities_target_put_request import ApiUsersUserIdIdentitiesTargetPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdIdentitiesTargetPutRequest from a JSON string
api_users_user_id_identities_target_put_request_instance = ApiUsersUserIdIdentitiesTargetPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdIdentitiesTargetPutRequest.to_json())

# convert the object into a dict
api_users_user_id_identities_target_put_request_dict = api_users_user_id_identities_target_put_request_instance.to_dict()
# create an instance of ApiUsersUserIdIdentitiesTargetPutRequest from a dict
api_users_user_id_identities_target_put_request_from_dict = ApiUsersUserIdIdentitiesTargetPutRequest.from_dict(api_users_user_id_identities_target_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


