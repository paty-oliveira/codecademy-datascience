import unittest
from HurricaneAnalysis.src.huricane_analysis import update_money_damages


class TestHurricaneDamage(unittest.TestCase):

    def test_should_return_damage_spent_in_millions(self):
        damages = ["1M", "10M"]
        actual_result = update_money_damages(damages)
        expected_result = [1000000.0, 10000000.0]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_damage_spent_in_billions(self):
        damages = ["1B", "10B"]
        actual_result = update_money_damages(damages)
        expected_result = [1000000000.0, 10000000000.0]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_damage_spent_in_million_and_billions(self):
        damages = ["40M", "27.9M", "5M", "64.8B", "91.6B", "25.1B"]
        actual_result = update_money_damages(damages)
        expected_result = [40000000.0, 279000000.0, 5000000.0,
                           648000000000.0, 916000000000, 251000000000.0]
        self.assertEqual(expected_result, actual_result)

    def test_should_keep_damages_not_records_in_damage_list(self):
        damages = ["Damages not recorded"]
        actual_result = update_money_damages(damages)
        expected_result = ["Damages not recorded"]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_damage_spent_by_hurricane(self):
        damages = ["Damages not recorded", "100M", "Damages not recorded",
                   "40M", "27.9M", "1.01B", "125B"]
        actual_result = update_money_damages(damages)
        expected_result = ["Damages not recorded", 100000000.0,
                           "Damages not recorded", 40000000.0,
                           279000000.0, 101000000000.0, 125000000000.0]

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
