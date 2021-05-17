# from unittest import TestCase

from laxleague.guardian import Guardian


# class TestGuardian(TestCase):
#     def test_guardian(self):
#         assert True
#
#     pass
def test_construction():
        g =  Guardian('Mary', 'Jones')
        assert 'Mary' == g.first_name
        assert 'Jones' == g.last_name

