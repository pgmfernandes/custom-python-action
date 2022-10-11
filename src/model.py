import json


class SastConfig:
    def __init__(self, json_obj):
        self.enabled = json_obj['enabled']


class SecretConfig:
    def __init__(self, json_obj):
        self.enabled = json_obj['enabled']


class ConfigPipeline:
    def __init__(self, json_obj):
        self.org = json_obj['org']
        self.name = json_obj['name']
        self.sast = SastConfig(json_obj['sast'])
        self.secret = SecretConfig(json_obj['secret'])

    def is_sast_enabled(self):
        if self.sast is not None:
            return self.sast.enabled
        return False

    def is_secret_enabled(self):
        if self.secret is not None:
            return self.secret.enabled
        return False

class ConfigPipelineHelper:
    @staticmethod
    def parse_config_pipeline_from_json(json_content) -> ConfigPipeline:
        resultDict = json.loads(json_content)
        obj = ConfigPipeline(resultDict)
        return obj
