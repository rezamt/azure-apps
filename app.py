# https://github.com/microsoftgraph/msgraph-sdk-python#2-getting-started-with-microsoft-graph
import asyncio
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.models.application import Application

# 2. Getting started with Microsoft Graph
# https://github.com/microsoftgraph/msgraph-sdk-python

# 2.1 Register your application
# Register your application by following the steps at Register your app with the Microsoft Identity Platform.
# https://docs.microsoft.com/graph/auth-register-app-v2
# https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-daemon-app-python-acquire-token

if __name__ == '__main__':
    # 2.2 Select and create an authentication provider
    # ClientSecretCredential [ OK ]
    # DeviceCodeCredential
    # InteractiveBrowserCredentials
    # AuthorizationCodeCredentials

    # @ToDo: From Your registration
    tenant_id = "<tenant_id>"
    client_id = "<client_id>"
    client_secret = "<client_secret>"

    # 2.3 Initialize a GraphServiceClient object
    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret,
    )

    scopes = ['https://graph.microsoft.com/.default']

    # 2.3 Initialize a GraphServiceClient object
    graph_client = GraphServiceClient(credentials=credential, scopes=scopes)

    # 3. Make requests against the service
    # GET /users/{id | userPrincipalName}
    async def get_user():
        user = await graph_client.users.by_user_id('userPrincipalName').get()
        if user:
            print(user.display_name)

    asyncio.run(get_user())

    request_body = Application(
        display_name="My App",
        description = "My App Description"
    )

    result = await graph_client.applications.post(body=request_body)