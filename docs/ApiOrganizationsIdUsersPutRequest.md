# ApiOrganizationsIdUsersPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to replace existing users. | 

## Example

```python
from py_logto.models.api_organizations_id_users_put_request import ApiOrganizationsIdUsersPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsIdUsersPutRequest from a JSON string
api_organizations_id_users_put_request_instance = ApiOrganizationsIdUsersPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsIdUsersPutRequest.to_json())

# convert the object into a dict
api_organizations_id_users_put_request_dict = api_organizations_id_users_put_request_instance.to_dict()
# create an instance of ApiOrganizationsIdUsersPutRequest from a dict
api_organizations_id_users_put_request_from_dict = ApiOrganizationsIdUsersPutRequest.from_dict(api_organizations_id_users_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


