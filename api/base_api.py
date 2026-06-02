class BaseApi:

    def __init__(self, request, agent_id, point_id):
        self.request = request
        self.agent_id = agent_id
        self.point_id = point_id

    @property
    def base_path(self):
        return f"v1/agents/{self.agent_id}/points/{self.point_id}"
