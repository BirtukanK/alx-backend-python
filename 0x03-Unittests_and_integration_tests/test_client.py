#!/usr/bin/env python3
""" defines test case for client file
"""


from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """ unittest class for org client"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    @patch('client.get_json', return_value={"login": "mocked"})
    def test_org(self, org_name: str, expected: dict, mock_get_json):
        """ test method for GithubOrgClient"""
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"login": "mocked"})


if __name__ == "__main__":
    unittest.main()
