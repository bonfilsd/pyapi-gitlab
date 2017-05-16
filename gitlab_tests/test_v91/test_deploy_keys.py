import responses

from gitlab.exceptions import HttpError
from gitlab_tests.base import BaseTest
from response_data.deploy_keys import *


class TestGetAllDeployKeys(BaseTest):
    def setUp(self):
        super(TestGetAllDeployKeys, self).setUp()
        self.gitlab.login(user=self.user, password=self.password)

    @responses.activate
    def test_get_all_deploy_keys(self):
        responses.add(
            responses.GET,
            self.gitlab.api_url + '/deploy_keys',
            json=get_deploy_keys,
            status=200,
            content_type='application/json')

        self.assertEqual(get_deploy_keys, self.gitlab.get_all_deploy_keys())

    @responses.activate
    def test_get_all_deploy_keys_empty_list(self):
        responses.add(
            responses.GET,
            self.gitlab.api_url + '/deploy_keys',
            json=[],
            status=200,
            content_type='application/json')

        self.assertEqual([], self.gitlab.get_all_deploy_keys())

    @responses.activate
    def test_get_all_deploy_keys_exception(self):
        responses.add(
            responses.GET,
            self.gitlab.api_url + '/deploy_keys',
            body='{"error":"404 Not Found"}',
            status=404,
            content_type='application/json')

        self.assertRaises(HttpError, self.gitlab.get_all_deploy_keys)