from gitlabform import Configuration
from gitlabform.gitlab import GitLab
from gitlabform.processors.single_entity_processor import SingleEntityProcessor


class JobTokenScopeProcessor(SingleEntityProcessor):
    def __init__(self, gitlab: GitLab, config: Configuration, strict: bool):
        super().__init__(
            configuration_name="inbound_job_token_scope",
            gitlab=gitlab,
            add_method_name=None,
            edit_method_name="patch_job_token_scope",
            get_method_name="get_job_token_scope",
        )
        self.config = config
        self.strict = strict
