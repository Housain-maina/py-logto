# ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | A list of organization ids to be granted. &lt;br/&gt; All the existing organizations&#39; access will be revoked if not in the list. &lt;br/&gt; If the list is empty, all the organizations&#39; access will be revoked. | 

## Example

```python
from py_logto.models.api_applications_id_users_user_id_consent_organizations_put_request import ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest from a JSON string
api_applications_id_users_user_id_consent_organizations_put_request_instance = ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest.to_json())

# convert the object into a dict
api_applications_id_users_user_id_consent_organizations_put_request_dict = api_applications_id_users_user_id_consent_organizations_put_request_instance.to_dict()
# create an instance of ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest from a dict
api_applications_id_users_user_id_consent_organizations_put_request_from_dict = ApiApplicationsIdUsersUserIdConsentOrganizationsPutRequest.from_dict(api_applications_id_users_user_id_consent_organizations_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


