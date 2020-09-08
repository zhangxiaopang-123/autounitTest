
from Service.wbf_signature import Signature
import time
from Service.config import environment
import unittest


class TestOpenApi(unittest.TestCase):

    def setUp(self) -> None:
        self.api_key = environment(0)[0]
        self.secret_key = environment(0)[1]
        self.host = environment(0)[-2]
        self.tie = int(time.time())
        print('测试用例开始执行!')

    def tearDown(self) -> None:
        print('测试用例执行结束!')

    def test_balance(self):
        request_path = '/open/api/user/account'
        result = Signature(self.api_key, self.secret_key, self.tie).get_sign(request_path, self.host)
        print('查询资产成功response:{}'.format(result))
        # assert result['msg'] == 'suc' and result['code'] == '0'
        self.assertEqual(result['msg'], 'suc')

    def test_fail(self):
        request_path = '/open/api/user/account'
        result = Signature(self.api_key, self.secret_key[:1], self.tie).get_sign(request_path, self.host)
        # print(result)
        print('查询资产失败response:{}'.format(result))
        # assert result['msg'] == 'suc' and result['code'] == '0'
        self.assertEqual(result['code'], '100005')


if __name__ == '__main__':
    unittest.main(verbosity=2)