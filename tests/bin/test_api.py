from unittest import TestCase

from mro.bin.api import MROApi


class TestMROApi(TestCase):

    def setUp(self):
        self.instance = MROApi("test")

    def tearDown(self):
        pass

    def testInstance(self):
        self.assertIsInstance(self.instance, MROApi)
