# CreateOrganizationInvitationRequestMessagePayload

The message payload for the \"OrganizationInvitation\" template to use when sending the invitation via email. If it is `false`, the invitation will not be sent via email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**link** | **str** |  | [optional] 

## Example

```python
from py_logto.models.create_organization_invitation_request_message_payload import CreateOrganizationInvitationRequestMessagePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationInvitationRequestMessagePayload from a JSON string
create_organization_invitation_request_message_payload_instance = CreateOrganizationInvitationRequestMessagePayload.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationInvitationRequestMessagePayload.to_json())

# convert the object into a dict
create_organization_invitation_request_message_payload_dict = create_organization_invitation_request_message_payload_instance.to_dict()
# create an instance of CreateOrganizationInvitationRequestMessagePayload from a dict
create_organization_invitation_request_message_payload_from_dict = CreateOrganizationInvitationRequestMessagePayload.from_dict(create_organization_invitation_request_message_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


