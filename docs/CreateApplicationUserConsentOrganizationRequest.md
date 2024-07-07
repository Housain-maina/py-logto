# CreateApplicationUserConsentOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | A list of organization ids to be granted. | 

## Example

```python
from py_logto.models.create_application_user_consent_organization_request import CreateApplicationUserConsentOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationUserConsentOrganizationRequest from a JSON string
create_application_user_consent_organization_request_instance = CreateApplicationUserConsentOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationUserConsentOrganizationRequest.to_json())

# convert the object into a dict
create_application_user_consent_organization_request_dict = create_application_user_consent_organization_request_instance.to_dict()
# create an instance of CreateApplicationUserConsentOrganizationRequest from a dict
create_application_user_consent_organization_request_from_dict = CreateApplicationUserConsentOrganizationRequest.from_dict(create_application_user_consent_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


