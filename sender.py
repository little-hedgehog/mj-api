import requests
import yaml

from endpoint import endpoint

CONFIG_FILE_NAME = "config.yml"


class Sender:
    def __init__(self):
        with open(CONFIG_FILE_NAME, 'r') as f:
            config = yaml.safe_load(f)
        self.authorization = config['authorization']
        self.guild_id = config['guild_id']
        self.channel_id = config['channel_id']
        self.user_agent = config['user_agent']

    def send(self, prompt: str):
        header = {
            'Authorization': self.authorization,
            'user-agent': self.user_agent
        }

        prompt = prompt.replace('_', ' ')
        print(prompt.split(' '))
        prompt = ' '.join(prompt.split())
        # prompt = re.sub(r'[^a-zA-Z0-9\s]+', '', prompt)
        prompt = prompt.lower()

        # payload = endpoint.gen_interactions_params(guild_id=self.guild_id, channel_id=self.channel_id, prompt=prompt)
        payload = endpoint.gen_send_params(guild_id=self.guild_id, channel_id=self.channel_id, prompt=prompt)

        r = requests.post(endpoint.interactions_api, json=payload, headers=header)
        print(r.content)
        print(f'prompt [{prompt}] successfully sent!')


Sender().send('robot')
