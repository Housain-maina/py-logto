# CreateApplicationRequestProtectedAppMetadata

The data for protected app, this feature is not available for open source version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_domain** | **str** | The subdomain prefix, e.g., my-site. | 
**origin** | **str** | The origin of target website, e.g., https://example.com. | 

## Example

```python
from py_logto.models.create_application_request_protected_app_metadata import CreateApplicationRequestProtectedAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationRequestProtectedAppMetadata from a JSON string
create_application_request_protected_app_metadata_instance = CreateApplicationRequestProtectedAppMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationRequestProtectedAppMetadata.to_json())

# convert the object into a dict
create_application_request_protected_app_metadata_dict = create_application_request_protected_app_metadata_instance.to_dict()
# create an instance of CreateApplicationRequestProtectedAppMetadata from a dict
create_application_request_protected_app_metadata_from_dict = CreateApplicationRequestProtectedAppMetadata.from_dict(create_application_request_protected_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


