# UpdateApplicationSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The secret name to update. Must be unique within the application. | 

## Example

```python
from py_logto.models.update_application_secret_request import UpdateApplicationSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationSecretRequest from a JSON string
update_application_secret_request_instance = UpdateApplicationSecretRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicationSecretRequest.to_json())

# convert the object into a dict
update_application_secret_request_dict = update_application_secret_request_instance.to_dict()
# create an instance of UpdateApplicationSecretRequest from a dict
update_application_secret_request_from_dict = UpdateApplicationSecretRequest.from_dict(update_application_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


