from repository import *


class ConfigRepositoryController:

    def __init__(self, github_auth, github_reposiroty):
        self.config_manager = CyberConfigRepositoryManager(github_auth=github_auth)
        self.github_repository = github_reposiroty

    def execute_configuration(self):
        print(f"[{self.github_repository}] Busca de arquivo específico de configuração")
        obj = self.config_manager.get_config_json(owner_and_repo_name=self.github_repository)
        if obj is not None:
            print(obj)
            github_repository = "test-" + self.github_repository
            print(f"::set-output name=dockerfiles::{github_repository}")