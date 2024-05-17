# ApiApplicationsGet200ResponseInnerOidcClientMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uris** | [**List[ApiApplicationsGet200ResponseInnerOidcClientMetadataRedirectUrisInner]**](ApiApplicationsGet200ResponseInnerOidcClientMetadataRedirectUrisInner.md) |  | 
**post_logout_redirect_uris** | **List[str]** |  | 
**logo_uri** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_applications_get200_response_inner_oidc_client_metadata import ApiApplicationsGet200ResponseInnerOidcClientMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsGet200ResponseInnerOidcClientMetadata from a JSON string
api_applications_get200_response_inner_oidc_client_metadata_instance = ApiApplicationsGet200ResponseInnerOidcClientMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsGet200ResponseInnerOidcClientMetadata.to_json())

# convert the object into a dict
api_applications_get200_response_inner_oidc_client_metadata_dict = api_applications_get200_response_inner_oidc_client_metadata_instance.to_dict()
# create an instance of ApiApplicationsGet200ResponseInnerOidcClientMetadata from a dict
api_applications_get200_response_inner_oidc_client_metadata_from_dict = ApiApplicationsGet200ResponseInnerOidcClientMetadata.from_dict(api_applications_get200_response_inner_oidc_client_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


