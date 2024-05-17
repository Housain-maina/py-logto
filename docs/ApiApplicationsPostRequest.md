# ApiApplicationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 
**oidc_client_metadata** | [**ApiApplicationsGet200ResponseInnerOidcClientMetadata**](ApiApplicationsGet200ResponseInnerOidcClientMetadata.md) |  | [optional] 
**custom_client_metadata** | [**ApiApplicationsGet200ResponseInnerCustomClientMetadata**](ApiApplicationsGet200ResponseInnerCustomClientMetadata.md) |  | [optional] 
**is_third_party** | **bool** |  | [optional] 
**protected_app_metadata** | [**ApiApplicationsPostRequestProtectedAppMetadata**](ApiApplicationsPostRequestProtectedAppMetadata.md) |  | [optional] 

## Example

```python
from py_logto.models.api_applications_post_request import ApiApplicationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsPostRequest from a JSON string
api_applications_post_request_instance = ApiApplicationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsPostRequest.to_json())

# convert the object into a dict
api_applications_post_request_dict = api_applications_post_request_instance.to_dict()
# create an instance of ApiApplicationsPostRequest from a dict
api_applications_post_request_from_dict = ApiApplicationsPostRequest.from_dict(api_applications_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


