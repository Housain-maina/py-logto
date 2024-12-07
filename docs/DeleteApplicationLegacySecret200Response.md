# DeleteApplicationLegacySecret200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**secret** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**oidc_client_metadata** | [**ListApplications200ResponseInnerOidcClientMetadata**](ListApplications200ResponseInnerOidcClientMetadata.md) |  | 
**custom_client_metadata** | [**ListApplications200ResponseInnerCustomClientMetadata**](ListApplications200ResponseInnerCustomClientMetadata.md) |  | 
**protected_app_metadata** | [**ListApplications200ResponseInnerProtectedAppMetadata**](ListApplications200ResponseInnerProtectedAppMetadata.md) |  | 
**custom_data** | **object** | arbitrary | 
**is_third_party** | **bool** |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.delete_application_legacy_secret200_response import DeleteApplicationLegacySecret200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteApplicationLegacySecret200Response from a JSON string
delete_application_legacy_secret200_response_instance = DeleteApplicationLegacySecret200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteApplicationLegacySecret200Response.to_json())

# convert the object into a dict
delete_application_legacy_secret200_response_dict = delete_application_legacy_secret200_response_instance.to_dict()
# create an instance of DeleteApplicationLegacySecret200Response from a dict
delete_application_legacy_secret200_response_from_dict = DeleteApplicationLegacySecret200Response.from_dict(delete_application_legacy_secret200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


