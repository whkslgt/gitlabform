from tests.acceptance import run_gitlabform
from gitlabform.processors.project.job_token_scopes_processor import JobTokenScopesProcessor


class TestJobTokenScope:
    def test__job_token_scope_change(self, project):
        config_job_token_scope = f"""
        projects_and_groups:
          {project.path_with_namespace}:
            inbound_job_token_scope: true
        """

        run_gitlabform(config_job_token_scope, project)

