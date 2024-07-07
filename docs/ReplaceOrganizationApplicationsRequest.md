# ReplaceOrganizationApplicationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** | An array of application IDs to replace existing applications. | 

## Example

```python
from py_logto.models.replace_organization_applications_request import ReplaceOrganizationApplicationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationApplicationsRequest from a JSON string
replace_organization_applications_request_instance = ReplaceOrganizationApplicationsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationApplicationsRequest.to_json())

# convert the object into a dict
replace_organization_applications_request_dict = replace_organization_applications_request_instance.to_dict()
# create an instance of ReplaceOrganizationApplicationsRequest from a dict
replace_organization_applications_request_from_dict = ReplaceOrganizationApplicationsRequest.from_dict(replace_organization_applications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


