import unittest
from HurricaneAnalysis.src.hurricane_analyzer import aggregate_hurricane_info


class TestAggregationHurricaneInformation(unittest.TestCase):

    def test_should_aggregate_information_about_the_hurricane_name(self):
        names = ["Cuba I"]
        actual_result = aggregate_hurricane_info(names,
                                                 months=[""],
                                                 years=[""],
                                                 winds=[""],
                                                 areas=[""],
                                                 damages=[""],
                                                 deaths=[""]
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "",
                                      "Year": "",
                                      "Max Sustained Wind": "",
                                      "Areas Affected": "",
                                      "Damage": "",
                                      "Deaths": ""
                                      }
                           }

        self.assertEqual(expected_result, actual_result)

        names = ["Cuba I", "San Felipe II Okeechobee"]
        actual_result = aggregate_hurricane_info(names,
                                                 months=["", ""],
                                                 years=["", ""],
                                                 winds=["", ""],
                                                 areas=["", ""],
                                                 damages=["", ""],
                                                 deaths=["", ""]
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "",
                                      "Year": "",
                                      "Max Sustained Wind": "",
                                      "Areas Affected": "",
                                      "Damage": "",
                                      "Deaths": ""
                                      },
                           "San Felipe II Okeechobee": {"Name": "San Felipe II Okeechobee",
                                                        "Month": "",
                                                        "Year": "",
                                                        "Max Sustained Wind": "",
                                                        "Areas Affected": "",
                                                        "Damage": "",
                                                        "Deaths": ""
                                                        }
                           }

        self.assertEqual(expected_result, actual_result)

    def test_should_aggregate_information_about_the_month(self):
        names = ["Cuba I"]
        months = ["October"]
        actual_result = aggregate_hurricane_info(names,
                                                 months,
                                                 years=[""],
                                                 winds=[""],
                                                 areas=[""],
                                                 damages=[""],
                                                 deaths=[""]
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "October",
                                      "Year": "",
                                      "Max Sustained Wind": "",
                                      "Areas Affected": "",
                                      "Damage": "",
                                      "Deaths": ""
                                      }
                           }

        self.assertEqual(expected_result, actual_result)

        names = ["Cuba I", "San Felipe II Okeechobee"]
        months = ["October", "September"]
        actual_result = aggregate_hurricane_info(names,
                                                 months,
                                                 years=["", ""],
                                                 winds=["", ""],
                                                 areas=["", ""],
                                                 damages=["", ""],
                                                 deaths=["", ""]
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "October",
                                      "Year": "",
                                      "Max Sustained Wind": "",
                                      "Areas Affected": "",
                                      "Damage": "",
                                      "Deaths": ""
                                      },
                           "San Felipe II Okeechobee": {"Name": "San Felipe II Okeechobee",
                                                        "Month": "September",
                                                        "Year": "",
                                                        "Max Sustained Wind": "",
                                                        "Areas Affected": "",
                                                        "Damage": "",
                                                        "Deaths": ""
                                                        }
                           }

        self.assertEqual(expected_result, actual_result)

    def test_should_aggregate_information_about_the_year(self):
        names = ["Cuba I"]
        months = ["October"]
        years = [1924]
        actual_result = aggregate_hurricane_info(names,
                                                 months,
                                                 years,
                                                 winds=[""],
                                                 areas=[""],
                                                 damages=[""],
                                                 deaths=[""]
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "October",
                                      "Year": 1924,
                                      "Max Sustained Wind": "",
                                      "Areas Affected": "",
                                      "Damage": "",
                                      "Deaths": ""
                                      }
                           }

        self.assertEqual(expected_result, actual_result)

    def test_should_aggregate_information_about_the_wind(self):
        names = ["Cuba I"]
        months = ["October"]
        years = [1924]
        winds = [165]
        actual_result = aggregate_hurricane_info(names,
                                                 months,
                                                 years,
                                                 winds,
                                                 areas=[""],
                                                 damages=[""],
                                                 deaths=[""]
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "October",
                                      "Year": 1924,
                                      "Max Sustained Wind": 165,
                                      "Areas Affected": "",
                                      "Damage": "",
                                      "Deaths": ""
                                      }
                           }
        self.assertEqual(expected_result, actual_result)

    def test_should_aggregate_information_about_the_affected_areas(self):
        names = ["Cuba I"]
        months = ["October"]
        years = [1924]
        winds = [165]
        areas = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas']]
        actual_result = aggregate_hurricane_info(names,
                                                 months,
                                                 years,
                                                 winds,
                                                 areas,
                                                 damages=[""],
                                                 deaths=[""]
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "October",
                                      "Year": 1924,
                                      "Max Sustained Wind": 165,
                                      "Areas Affected": ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                                      "Damage": "",
                                      "Deaths": ""
                                      }
                           }
        self.assertEqual(expected_result, actual_result)

    def test_should_aggregate_information_about_the_damage(self):
        names = ["Cuba I"]
        months = ["October"]
        years = [1924]
        winds = [165]
        areas = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas']]
        damages = ['Damages not recorded']
        actual_result = aggregate_hurricane_info(names,
                                                 months,
                                                 years,
                                                 winds,
                                                 areas,
                                                 damages,
                                                 deaths=[""])
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "October",
                                      "Year": 1924,
                                      "Max Sustained Wind": 165,
                                      "Areas Affected": ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                                      "Damage": "Damages not recorded",
                                      "Deaths": ""
                                      }
                           }
        self.assertEqual(expected_result, actual_result)

    def test_should_aggregate_information_about_the_number_of_deaths(self):
        names = ["Cuba I"]
        months = ["October"]
        years = [1924]
        winds = [165]
        areas = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas']]
        damages = ['Damages not recorded']
        deaths = [90]
        actual_result = aggregate_hurricane_info(names,
                                                 months,
                                                 years,
                                                 winds,
                                                 areas,
                                                 damages,
                                                 deaths
                                                 )
        expected_result = {"Cuba I": {"Name": "Cuba I",
                                      "Month": "October",
                                      "Year": 1924,
                                      "Max Sustained Wind": 165,
                                      "Areas Affected": ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                                      "Damage": "Damages not recorded",
                                      "Deaths": 90
                                      }
                           }
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
