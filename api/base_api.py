import os


class BaseApi:

    def __init__(self, request):
        self.request = request

        agent_id = os.getenv("AGENT_ID", "YOUR_AGENT_ID")
        point_id = os.getenv("POINT_ID", "YOUR_POINT_ID")

        self.base_path = f"/v1/agents/{agent_id}/points/{point_id}"