# ApiApplicationsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**secret** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**oidc_client_metadata** | [**ApiApplicationsGet200ResponseInnerOidcClientMetadata**](ApiApplicationsGet200ResponseInnerOidcClientMetadata.md) |  | 
**custom_client_metadata** | [**ApiApplicationsGet200ResponseInnerCustomClientMetadata**](ApiApplicationsGet200ResponseInnerCustomClientMetadata.md) |  | 
**protected_app_metadata** | [**ApiApplicationsGet200ResponseInnerProtectedAppMetadata**](ApiApplicationsGet200ResponseInnerProtectedAppMetadata.md) |  | 
**is_third_party** | **bool** |  | 
**created_at** | **float** |  | 
**is_admin** | **bool** |  | 

## Example

```python
from py_logto.models.api_applications_id_get200_response import ApiApplicationsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsIdGet200Response from a JSON string
api_applications_id_get200_response_instance = ApiApplicationsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsIdGet200Response.to_json())

# convert the object into a dict
api_applications_id_get200_response_dict = api_applications_id_get200_response_instance.to_dict()
# create an instance of ApiApplicationsIdGet200Response from a dict
api_applications_id_get200_response_from_dict = ApiApplicationsIdGet200Response.from_dict(api_applications_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


