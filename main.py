import inmation_api_client

# Replace with your Inmation server URL
server_url = "http://localhost:8080"

# Create an Inmation API client
client = inmation_api_client.InmationClient(server_url)

# Get the server information
server_info = client.get_server_info()
print(server_info)