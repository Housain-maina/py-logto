# ApiApplicationsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**oidc_client_metadata** | [**ApiApplicationsIdPatchRequestOidcClientMetadata**](ApiApplicationsIdPatchRequestOidcClientMetadata.md) |  | [optional] 
**custom_client_metadata** | [**ApiApplicationsGet200ResponseInnerCustomClientMetadata**](ApiApplicationsGet200ResponseInnerCustomClientMetadata.md) |  | [optional] 
**protected_app_metadata** | [**ApiApplicationsIdPatchRequestProtectedAppMetadata**](ApiApplicationsIdPatchRequestProtectedAppMetadata.md) |  | [optional] 
**is_admin** | **bool** | Whether the application has admin access. User can enable the admin access for Machine-to-Machine apps. | [optional] 

## Example

```python
from py_logto.models.api_applications_id_patch_request import ApiApplicationsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsIdPatchRequest from a JSON string
api_applications_id_patch_request_instance = ApiApplicationsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsIdPatchRequest.to_json())

# convert the object into a dict
api_applications_id_patch_request_dict = api_applications_id_patch_request_instance.to_dict()
# create an instance of ApiApplicationsIdPatchRequest from a dict
api_applications_id_patch_request_from_dict = ApiApplicationsIdPatchRequest.from_dict(api_applications_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


