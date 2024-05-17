# ApiApplicationsApplicationIdRolesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ids** | **List[str]** | An array of API resource role IDs to assign. | 

## Example

```python
from py_logto.models.api_applications_application_id_roles_post_request import ApiApplicationsApplicationIdRolesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsApplicationIdRolesPostRequest from a JSON string
api_applications_application_id_roles_post_request_instance = ApiApplicationsApplicationIdRolesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsApplicationIdRolesPostRequest.to_json())

# convert the object into a dict
api_applications_application_id_roles_post_request_dict = api_applications_application_id_roles_post_request_instance.to_dict()
# create an instance of ApiApplicationsApplicationIdRolesPostRequest from a dict
api_applications_application_id_roles_post_request_from_dict = ApiApplicationsApplicationIdRolesPostRequest.from_dict(api_applications_application_id_roles_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


