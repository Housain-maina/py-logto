# UpdateApplicationRequestOidcClientMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uris** | [**List[ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner]**](ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner.md) |  | [optional] 
**post_logout_redirect_uris** | **List[str]** |  | [optional] 
**backchannel_logout_uri** | **str** |  | [optional] 
**backchannel_logout_session_required** | **bool** |  | [optional] 
**logo_uri** | **str** |  | [optional] 

## Example

```python
from py_logto.models.update_application_request_oidc_client_metadata import UpdateApplicationRequestOidcClientMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationRequestOidcClientMetadata from a JSON string
update_application_request_oidc_client_metadata_instance = UpdateApplicationRequestOidcClientMetadata.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicationRequestOidcClientMetadata.to_json())

# convert the object into a dict
update_application_request_oidc_client_metadata_dict = update_application_request_oidc_client_metadata_instance.to_dict()
# create an instance of UpdateApplicationRequestOidcClientMetadata from a dict
update_application_request_oidc_client_metadata_from_dict = UpdateApplicationRequestOidcClientMetadata.from_dict(update_application_request_oidc_client_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


