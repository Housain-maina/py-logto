# ApiRolesIdApplicationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** | An array of application IDs to be assigned. | 

## Example

```python
from py_logto.models.api_roles_id_applications_post_request import ApiRolesIdApplicationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRolesIdApplicationsPostRequest from a JSON string
api_roles_id_applications_post_request_instance = ApiRolesIdApplicationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiRolesIdApplicationsPostRequest.to_json())

# convert the object into a dict
api_roles_id_applications_post_request_dict = api_roles_id_applications_post_request_instance.to_dict()
# create an instance of ApiRolesIdApplicationsPostRequest from a dict
api_roles_id_applications_post_request_from_dict = ApiRolesIdApplicationsPostRequest.from_dict(api_roles_id_applications_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


