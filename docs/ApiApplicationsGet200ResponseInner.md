# ApiApplicationsGet200ResponseInner


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

## Example

```python
from py_logto.models.api_applications_get200_response_inner import ApiApplicationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsGet200ResponseInner from a JSON string
api_applications_get200_response_inner_instance = ApiApplicationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsGet200ResponseInner.to_json())

# convert the object into a dict
api_applications_get200_response_inner_dict = api_applications_get200_response_inner_instance.to_dict()
# create an instance of ApiApplicationsGet200ResponseInner from a dict
api_applications_get200_response_inner_from_dict = ApiApplicationsGet200ResponseInner.from_dict(api_applications_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


