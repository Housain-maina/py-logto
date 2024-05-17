# ApiApplicationsIdPatchRequestOidcClientMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uris** | [**List[ApiApplicationsGet200ResponseInnerOidcClientMetadataRedirectUrisInner]**](ApiApplicationsGet200ResponseInnerOidcClientMetadataRedirectUrisInner.md) |  | [optional] 
**post_logout_redirect_uris** | **List[str]** |  | [optional] 
**logo_uri** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_applications_id_patch_request_oidc_client_metadata import ApiApplicationsIdPatchRequestOidcClientMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsIdPatchRequestOidcClientMetadata from a JSON string
api_applications_id_patch_request_oidc_client_metadata_instance = ApiApplicationsIdPatchRequestOidcClientMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsIdPatchRequestOidcClientMetadata.to_json())

# convert the object into a dict
api_applications_id_patch_request_oidc_client_metadata_dict = api_applications_id_patch_request_oidc_client_metadata_instance.to_dict()
# create an instance of ApiApplicationsIdPatchRequestOidcClientMetadata from a dict
api_applications_id_patch_request_oidc_client_metadata_from_dict = ApiApplicationsIdPatchRequestOidcClientMetadata.from_dict(api_applications_id_patch_request_oidc_client_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


