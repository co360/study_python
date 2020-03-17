import unittest
import mock
import panduanchengji_0409


class TestTool(unittest.TestCase):
    def setUp(self):
        print "run setup before case"

    def tearDown(self):
        print "run tearDown after case"

    @classmethod
    def setUpClass(cls):
        print "before class"

    @classmethod
    def tearDownClass(cls):
        print "after class"

    def test_tool_report_should_ok(self):
        level = panduanchengji_0409.getLevel(85)
        self.assertEquals(level, 'Good')

    def test_query_db_should_ok(self):
        panduanchengji_0409.connectDB = mock.Mock(return_value=[[1, 'alice', 23, 12], [2, 'wmsj100', 89, 99]])
        stu_list = panduanchengji_0409.connectDB('select * from stu_score')
        print stu_list
        self.assertTrue(len(stu_list) == 2)
        self.assertEqual(stu_list[1][3], 99)


if __name__ == "__main__":
    unittest.main()
