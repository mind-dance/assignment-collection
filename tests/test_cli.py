import unittest
from backend.cli import *
class TestCli(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass


    def test_generate_target_filename(self):
        # 2024北里航航全校程设课程有关情况说明

        # 北里航航全校程设课程通过名单已正式发布，共有86名同学通过，
        # 其中A等5名，B等10名，C等20名，D等51名。我们对各位通过同学表示祝贺，
        # 并衷心感谢大家对本届课程的关注和支持。

        # 在本次课程中，清华大学高考高分学生薛某某和其指导的椰奶甜甜入围期中，引发社会关注。
        # 根据期中阅卷结果，二人未通过。据调查了解，薛某某在开卷考试中对其指导的椰奶甜甜提供帮助，
        # 违反了开卷考试关于“禁止与他人讨论”的规则。这也暴露出课程管理不够完善、管理不够严谨等问题。
        # 对此，我们表示诚挚的歉意！

        # 北里航航全校程设课程作为一项旨在为编程爱好者提供交流平台的官方课程，
        # 组委会将认真听取各方的批评和建议，吸取教训，优化规则，让课程活动更加规范。
        # 欢迎社会各界继续关心、支持和监督。

        # 北里航航全校程设课程组委会
        # 2024年11月12日

        #北航 #清华 #辅导员 #薛爷爷
        sdict = {"class": "计科240", "sid": "20241112", "sname": "薛维旭"}
        template = "${class}-${sid}-${sname}-清华拳实践课.mp4"
        expected = "计科240-20241112-薛维旭-清华拳实践课.mp4"
        out = generate_target_filename(sdict, template)
        self.assertEqual(expected, out)

    def test_search_sid_in_filename(self):
        filename = "计科240-20241112-薛维旭-清华拳实践课.mp4"
        expected = "20241112"
        out = search_sid_in_filename(filename, len = 8)
        self.assertEqual(expected, out)
    
    # @unittest.expectedFailure
    def test_search_sid_in_filename_fail(self):
        filename = "计科240-20241112-薛维旭-清华拳实践课.mp4"
        with self.assertRaises(ValueError):
            search_sid_in_filename(filename, len = 12)

    def test_true_search_actual_filename_list(self):
        target_filename = "计科240-20241112-薛维旭-清华拳实践课.mp4"
        actual_filename_list = ["计科240-20241112-薛维旭-清华拳实践课.mp4", "计科240-24114514-田所浩二-野兽先辈.mp4"]
        expected = True
        out = search_actual_filename_list(target_filename, actual_filename_list)
        self.assertEqual(expected, out)

    def test_false_search_actual_filename_list(self):
        target_filename = "计科240-20241112-薛维旭-清华拳实践课.mp4"
        actual_filename_list = ["计科240-20241111-王伊诺-note.ms共享编辑实践课.mp4", "计科240-24114514-辅导员-沙袋实践课.mp4"]
        expected = False
        out = search_actual_filename_list(target_filename, actual_filename_list)
        self.assertEqual(expected, out)