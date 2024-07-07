# ListApplicationUserConsentOrganizations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[ListApplicationUserConsentOrganizations200ResponseOrganizationsInner]**](ListApplicationUserConsentOrganizations200ResponseOrganizationsInner.md) | A list of organization entities granted by the user for the application. | 

## Example

```python
from py_logto.models.list_application_user_consent_organizations200_response import ListApplicationUserConsentOrganizations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplicationUserConsentOrganizations200Response from a JSON string
list_application_user_consent_organizations200_response_instance = ListApplicationUserConsentOrganizations200Response.from_json(json)
# print the JSON string representation of the object
print(ListApplicationUserConsentOrganizations200Response.to_json())

# convert the object into a dict
list_application_user_consent_organizations200_response_dict = list_application_user_consent_organizations200_response_instance.to_dict()
# create an instance of ListApplicationUserConsentOrganizations200Response from a dict
list_application_user_consent_organizations200_response_from_dict = ListApplicationUserConsentOrganizations200Response.from_dict(list_application_user_consent_organizations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


