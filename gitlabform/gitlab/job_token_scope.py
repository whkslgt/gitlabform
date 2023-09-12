from gitlabform.gitlab.core import GitLabCore


class GitLabJobTokenScope(GitLabCore):
    def get_job_token_scope(self, project_and_group_name):
        return self._make_requests_to_api(
            path_as_format_string='/projects/%s/job_token_scope',
            args=project_and_group_name,
        )

    def patch_job_token_scope(self, project_and_group_name, data):
        return self._make_requests_to_api(
            path_as_format_string='/projects/%s/job_token_scope',
            args=project_and_group_name,
            method="PATCH",
            data=data,
            expected_codes=[204],
        )
