import argparse
import os
import unittest

import mock

from harbinger.base import Base
from harbinger.factory.framework_extractor import \
    FrameworkExtractor


class TestFrameworkExtractor(unittest.TestCase):
    """Unit tests for FrameworkExtractor"""

    description_value = None

    def setUp(self):
        self.args = mock.Mock(spec=argparse.Namespace)

        self.yaml = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                 "data/test_yaml.yaml")

        self.base_object = Base(app=mock.Mock(), app_args=self.args)
        self.yaml_file = self.base_object.load_yaml(self.yaml)

        self.test_object = FrameworkExtractor()

    def test_parse_frameworks(self):
        self.framework_dict = self.test_object.parse_frameworks(self.yaml_file)
        self.assertIn("framework_1", self.framework_dict)
        self.assertIn("framework_2", self.framework_dict)
