import pytest
from pythoncode.calculator import Calculator


# 课后作业
# 1、补全计算器（加法 除法）的测试用例
# 2、使用参数化完成测试用例的自动生成
# 3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
# 注意：
# 使用等价类，边界值，因果图等设计测试用例
# 测试用例中添加断言，验证结果
# 灵活使用 setup(), teardown() , setup_class(), teardown_class()

class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2]],
                             ids=['int_case', 'bignum_case', 'float_case', 'minus_case'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect
        print("{} + {} = {}".format(a, b, expect))

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 1], [100, 100, 1], [200, 100, 2], [5, 10, 0.5], [4, 0, "error"]])
    def test_div(self, a, b, expect):
        if b == 0:
            print("除数不能为0")
        else:
            result = self.calc.div(a, b)
            assert round(result, 1) == expect
            print("{} / {} = {}".format(a, b, expect))

# def test_add1(self):
#     # calc = Calculator()
#     result = self.calc.add(100, 100)
#     assert result == 200
#
# def test_add2(self):
#     # calc = Calculator()
#     result = self.calc.add(0.1, 0.1)
#     assert result == 0.2
