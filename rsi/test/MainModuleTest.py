import unittest

from rsi  import mainmodule

class MainoduleTest(unittest.TestCase):
    def test_log(self):
        self.assertEqual('ok', mainmodule.log("ok"))
