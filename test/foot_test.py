#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author  :   chenjiannan
@File    :   DTW_distance_test.py
@Description    :   None
'''

import unittest


class TestDemo(unittest.TestCase):
    def setUp(self):
        pass

    def test_equal(self):
        # self.assertEqual(DTW_raw(self.s1, self.s2), 2)
        # self.assertEqual(DTW_raw(self.ts1, self.ts2), 815.650844020277)

        # # 测试计算的两两之间距离的总和是否一致
        # self.assertEqual(np.nansum(self.distance_results), 1607.2270625532249)
        # # 测试计算的两两之间无法计算距离的部分是否一致
        # self.assertEqual(
        #     all((np.isnan(
        #         self.distance_results) == self.isnan_check).flatten()), True)
        # # 测试大样本下两两之间距离的总和是否一致
        # self.assertEqual(np.nansum(self.distance_results2), 91281416.98594227)

if __name__ == '__main__':
    unittest.main()
