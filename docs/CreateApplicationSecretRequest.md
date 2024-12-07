# CreateApplicationSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The secret name. Must be unique within the application. | 
**expires_at** | **float** | The epoch time in milliseconds when the secret will expire. If not provided, the secret will never expire. | [optional] 

## Example

```python
from py_logto.models.create_application_secret_request import CreateApplicationSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationSecretRequest from a JSON string
create_application_secret_request_instance = CreateApplicationSecretRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationSecretRequest.to_json())

# convert the object into a dict
create_application_secret_request_dict = create_application_secret_request_instance.to_dict()
# create an instance of CreateApplicationSecretRequest from a dict
create_application_secret_request_from_dict = CreateApplicationSecretRequest.from_dict(create_application_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


