# ListApplications200ResponseInnerOidcClientMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uris** | [**List[ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner]**](ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner.md) |  | 
**post_logout_redirect_uris** | **List[str]** |  | 
**backchannel_logout_uri** | **str** |  | [optional] 
**backchannel_logout_session_required** | **bool** |  | [optional] 
**logo_uri** | **str** |  | [optional] 

## Example

```python
from py_logto.models.list_applications200_response_inner_oidc_client_metadata import ListApplications200ResponseInnerOidcClientMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplications200ResponseInnerOidcClientMetadata from a JSON string
list_applications200_response_inner_oidc_client_metadata_instance = ListApplications200ResponseInnerOidcClientMetadata.from_json(json)
# print the JSON string representation of the object
print(ListApplications200ResponseInnerOidcClientMetadata.to_json())

# convert the object into a dict
list_applications200_response_inner_oidc_client_metadata_dict = list_applications200_response_inner_oidc_client_metadata_instance.to_dict()
# create an instance of ListApplications200ResponseInnerOidcClientMetadata from a dict
list_applications200_response_inner_oidc_client_metadata_from_dict = ListApplications200ResponseInnerOidcClientMetadata.from_dict(list_applications200_response_inner_oidc_client_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


