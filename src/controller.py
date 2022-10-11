from repository import *
from src.model import ConfigPipelineHelper


class ConfigRepositoryController:

    def __init__(self, github_auth, github_reposiroty):
        self.config_manager = CyberConfigRepositoryManager(github_auth=github_auth)
        self.github_repository = github_reposiroty

    def execute_configuration(self):
        config_json = self.config_manager.get_config_json(owner_and_repo_name=self.github_repository)
        if config_json is not None:
            print(config_json)
            config_pipeline = ConfigPipelineHelper.parse_config_pipeline_from_json(config_json)
            if config_pipeline.is_sast_enabled():
                print(f"::debug::{config_pipeline.name} - Sast enabled.")
            if config_pipeline.is_secret_enabled():
                print(f"::debug::{config_pipeline.name} - Secret enabled.")
            github_repository = "test-" + self.github_repository
            print(f"::set-output name=dockerfiles::{config_pipeline}")
        else:
            print("::error::Repository configuration not found.")