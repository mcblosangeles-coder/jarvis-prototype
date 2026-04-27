import httpx

class AnthropicClient:
    def __init__(self, api_key):
        self.api_key = api_key

    async def request(self, prompt):
        response = await httpx.post(
            'https://api.anthropic.com/v1/complete',
            headers={
                'Authorization': f'Bearer {self.api_key}'
            },
            json={'prompt': prompt}
        )
        return response.json()
