# ApiApplicationsPostRequestProtectedAppMetadata

The data for protected app, this feature is not available for open source version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_domain** | **str** | The subdomain prefix, e.g., my-site. | 
**origin** | **str** | The origin of target website, e.g., https://example.com. | 

## Example

```python
from py_logto.models.api_applications_post_request_protected_app_metadata import ApiApplicationsPostRequestProtectedAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsPostRequestProtectedAppMetadata from a JSON string
api_applications_post_request_protected_app_metadata_instance = ApiApplicationsPostRequestProtectedAppMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsPostRequestProtectedAppMetadata.to_json())

# convert the object into a dict
api_applications_post_request_protected_app_metadata_dict = api_applications_post_request_protected_app_metadata_instance.to_dict()
# create an instance of ApiApplicationsPostRequestProtectedAppMetadata from a dict
api_applications_post_request_protected_app_metadata_from_dict = ApiApplicationsPostRequestProtectedAppMetadata.from_dict(api_applications_post_request_protected_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


