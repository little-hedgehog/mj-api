interactions_api = 'https://discord.com/api/v9/interactions'


def gen_send_params(guild_id: str, channel_id: str, prompt: str):
    """
    创建发送参数
    :param guild_id: discord 服务器ID
    :param channel_id: 服务器内频道ID
    :param prompt: 提示词
    :return: interactions接口参数
    """
    return {
        "type": 2,
        "application_id": "936929561302675456",
        "guild_id": guild_id,
        "channel_id": channel_id,
        # 变化的？
        "session_id": "deae3a94e3bc6a6b48f8e163cd862cb6",
        "data": {
            "version": "1077969938624553050",
            "id": "938956540159881230",
            "name": "imagine",
            "type": 1,
            "options": [
                {
                    "type": 3,
                    "name": "prompt",
                    # 变化的
                    "value": prompt
                }
            ],
            "application_command": {
                "id": "938956540159881230",
                "application_id": "936929561302675456",
                "version": "1077969938624553050",
                "default_member_permissions": None,
                "type": 1,
                "nsfw": False,
                "name": "imagine",
                "description": "Create images with Midjourney",
                # ？？
                # "dm_permission": None,
                "dm_permission": True,
                "contexts": None,
                "options": [
                    {
                        "type": 3,
                        "name": "prompt",
                        "description": "The prompt to imagine",
                        "required": True
                    }
                ]
            },
            "attachments": [

            ]
        },
        # "nonce": "1105550648591515648"
    }
