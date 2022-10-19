from repository import *
from src.model import ConfigPipelineHelper
from src.utility import CyberException, Messages


class ConfigRepositoryController:

    def __init__(self, github_auth, github_reposiroty):
        self.config_manager = CyberConfigRepositoryManager(github_auth=github_auth)
        self.github_repository = github_reposiroty

    def execute_configuration(self, secure_task):
        config_json = self.config_manager.get_config_json(owner_and_repo_name=self.github_repository)
        if config_json is not None:
            print(config_json)
            config_pipeline = ConfigPipelineHelper.parse_config_pipeline_from_json(config_json)
            task = config_pipeline.get_secure_task(secure_task)
            if task is None:
                print(f"::error::Task {secure_task} not found into config file.")
                return
            self.export_output(task)
        else:
            print(f"::error::Repository configuration not found for {self.github_repository}.")

    def export_output(self, task:ConfigPipeline):
        custom_payload = ConfigPipeline.get_custom_payload(task)
        if custom_payload is not None:
            for key in custom_payload:
                value = custom_payload[key]
                print(f"::set-output name={key}::{value}")

class GenericConfigController:

    def __init__(self, custom_payload):
        self.custom_payload = custom_payload

    def execute(self):
        raise CyberException(Messages.ERROR_NOT_IMPLEMENTED)
