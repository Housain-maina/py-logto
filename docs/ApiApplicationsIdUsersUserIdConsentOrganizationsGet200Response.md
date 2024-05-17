# ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner]**](ApiApplicationsIdUsersUserIdConsentOrganizationsGet200ResponseOrganizationsInner.md) | A list of organization entities granted by the user for the application. | 

## Example

```python
from py_logto.models.api_applications_id_users_user_id_consent_organizations_get200_response import ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response from a JSON string
api_applications_id_users_user_id_consent_organizations_get200_response_instance = ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response.to_json())

# convert the object into a dict
api_applications_id_users_user_id_consent_organizations_get200_response_dict = api_applications_id_users_user_id_consent_organizations_get200_response_instance.to_dict()
# create an instance of ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response from a dict
api_applications_id_users_user_id_consent_organizations_get200_response_from_dict = ApiApplicationsIdUsersUserIdConsentOrganizationsGet200Response.from_dict(api_applications_id_users_user_id_consent_organizations_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


