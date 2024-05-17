# ApiUsersUserIdIdentitiesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** | The Logto connector ID. | 
**connector_data** | **Dict[str, object]** | A json object constructed from the url query params returned by the social platform. Typically it contains &#x60;code&#x60;, &#x60;state&#x60; and &#x60;redirectUri&#x60; fields. | 

## Example

```python
from py_logto.models.api_users_user_id_identities_post_request import ApiUsersUserIdIdentitiesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersUserIdIdentitiesPostRequest from a JSON string
api_users_user_id_identities_post_request_instance = ApiUsersUserIdIdentitiesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUsersUserIdIdentitiesPostRequest.to_json())

# convert the object into a dict
api_users_user_id_identities_post_request_dict = api_users_user_id_identities_post_request_instance.to_dict()
# create an instance of ApiUsersUserIdIdentitiesPostRequest from a dict
api_users_user_id_identities_post_request_from_dict = ApiUsersUserIdIdentitiesPostRequest.from_dict(api_users_user_id_identities_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


