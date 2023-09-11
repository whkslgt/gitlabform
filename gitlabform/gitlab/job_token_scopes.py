from gitlabform.gitlab.core import GitLabCore

JOB_TOKEN_SCOPE_PATH = "/projects/%s/job_token_scope"


class GitLabJobTokenScope(GitLabCore):
    def get_job_token_scope(self, project_and_group_name):
        return self._make_requests_to_api(
            self,
            JOB_TOKEN_SCOPE_PATH,
            project_and_group_name,
        )

    def patch_job_token_scope(self, project_and_group_name, enabled):
        return self._make_requests_to_api(
            JOB_TOKEN_SCOPE_PATH,
            project_and_group_name,
            "PATCH",
            data='{"enabled": {is_enabled}}'.format(is_enabled=enabled),
            expected_codes=[204],
        )
