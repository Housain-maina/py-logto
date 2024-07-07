# AddOrganizationApplicationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** | The application IDs to add. | 

## Example

```python
from py_logto.models.add_organization_applications_request import AddOrganizationApplicationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrganizationApplicationsRequest from a JSON string
add_organization_applications_request_instance = AddOrganizationApplicationsRequest.from_json(json)
# print the JSON string representation of the object
print(AddOrganizationApplicationsRequest.to_json())

# convert the object into a dict
add_organization_applications_request_dict = add_organization_applications_request_instance.to_dict()
# create an instance of AddOrganizationApplicationsRequest from a dict
add_organization_applications_request_from_dict = AddOrganizationApplicationsRequest.from_dict(add_organization_applications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


