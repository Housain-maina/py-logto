# ApiApplicationsGet200ResponseInnerCustomClientMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cors_allowed_origins** | **List[str]** |  | [optional] 
**id_token_ttl** | **float** |  | [optional] 
**refresh_token_ttl** | **float** |  | [optional] 
**refresh_token_ttl_in_days** | **float** |  | [optional] 
**always_issue_refresh_token** | **bool** |  | [optional] 
**rotate_refresh_token** | **bool** |  | [optional] 

## Example

```python
from py_logto.models.api_applications_get200_response_inner_custom_client_metadata import ApiApplicationsGet200ResponseInnerCustomClientMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsGet200ResponseInnerCustomClientMetadata from a JSON string
api_applications_get200_response_inner_custom_client_metadata_instance = ApiApplicationsGet200ResponseInnerCustomClientMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsGet200ResponseInnerCustomClientMetadata.to_json())

# convert the object into a dict
api_applications_get200_response_inner_custom_client_metadata_dict = api_applications_get200_response_inner_custom_client_metadata_instance.to_dict()
# create an instance of ApiApplicationsGet200ResponseInnerCustomClientMetadata from a dict
api_applications_get200_response_inner_custom_client_metadata_from_dict = ApiApplicationsGet200ResponseInnerCustomClientMetadata.from_dict(api_applications_get200_response_inner_custom_client_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


