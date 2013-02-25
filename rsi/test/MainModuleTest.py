import unittest

from mypackage import mymodule

class MainoduleTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual('ok', mainmodule.main())
