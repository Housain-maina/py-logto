# ApiApplicationsApplicationIdRolesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ids** | **List[str]** | An array of API resource role IDs to update for the application. | 

## Example

```python
from py_logto.models.api_applications_application_id_roles_put_request import ApiApplicationsApplicationIdRolesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsApplicationIdRolesPutRequest from a JSON string
api_applications_application_id_roles_put_request_instance = ApiApplicationsApplicationIdRolesPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsApplicationIdRolesPutRequest.to_json())

# convert the object into a dict
api_applications_application_id_roles_put_request_dict = api_applications_application_id_roles_put_request_instance.to_dict()
# create an instance of ApiApplicationsApplicationIdRolesPutRequest from a dict
api_applications_application_id_roles_put_request_from_dict = ApiApplicationsApplicationIdRolesPutRequest.from_dict(api_applications_application_id_roles_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


