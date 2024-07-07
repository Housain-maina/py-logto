# ReplaceApplicationUserConsentOrganizationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | A list of organization ids to be granted. &lt;br/&gt; All the existing organizations&#39; access will be revoked if not in the list. &lt;br/&gt; If the list is empty, all the organizations&#39; access will be revoked. | 

## Example

```python
from py_logto.models.replace_application_user_consent_organizations_request import ReplaceApplicationUserConsentOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceApplicationUserConsentOrganizationsRequest from a JSON string
replace_application_user_consent_organizations_request_instance = ReplaceApplicationUserConsentOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceApplicationUserConsentOrganizationsRequest.to_json())

# convert the object into a dict
replace_application_user_consent_organizations_request_dict = replace_application_user_consent_organizations_request_instance.to_dict()
# create an instance of ReplaceApplicationUserConsentOrganizationsRequest from a dict
replace_application_user_consent_organizations_request_from_dict = ReplaceApplicationUserConsentOrganizationsRequest.from_dict(replace_application_user_consent_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


