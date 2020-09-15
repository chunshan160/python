#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/23 11:47
# @Author :春衫
# @File :payment_method.py

from TestData.test_data import cbp as yb
from TestData.test_data import xianjin as xj
from decimal import *
from Common.user_log import UserLog
from Common.fengyong.Calculation.ratio import ratio

my_logger = UserLog()

class PaymentMethod:

    def payment_method(self,ip,user_id, member_level, payment_method, price):
        '''

        :param member_level: 会员等级
        :param payment_method: 支付方式
        :param price: 商品价格
        :return:
        '''
        ratio_data=ratio(ip, user_id)
        cbp_ratio=ratio_data[0]
        cash_ratio=ratio_data[1]

        cbp = float(price) * cbp_ratio  # 需要支付的易贝服务费
        cbp = Decimal(str(cbp)).quantize(Decimal('0.00'))

        cash = float(price) * cash_ratio  # 需要支付的现金服务费
        cash = Decimal(str(cash)).quantize(Decimal('0.00'))

        goods_price = Decimal(str(price)).quantize(Decimal('0.00'))

        if payment_method == "易贝":
            my_logger.debug(f"买家需要支付易贝服务费：{cbp}")
            my_logger.debug(f"买家需要支付现金服务费：{cash}")
            return goods_price, cbp, cash
        elif payment_method == "易贝券":
            my_logger.debug(f"买家不需要支付易贝服务费")
            my_logger.debug(f"买家不需要支付现金服务费")
            return goods_price
        elif payment_method == "抵工资":
            my_logger.debug(f"企业需要支付易贝服务费：{cbp}")
            my_logger.debug(f"企业需要支付现金服务费：{cash}")
            return goods_price, cbp, cash
        elif payment_method == "家人购":
            my_logger.debug(f"家人需要支付易贝服务费：{cbp}")
            my_logger.debug(f"家人需要支付现金服务费：{cash}")
            return goods_price, cbp, cash
        else:
            cash = float(price) * (yb[member_level] + xj[member_level])
            cash = Decimal(str(cash)).quantize(Decimal('0.00'))
            my_logger.debug(f"卖家不需要支付易贝服务费")
            my_logger.debug(f"卖家需要支付现金服务费：{cash}")
            return goods_price,cash


if __name__ == '__main__':
    a = PaymentMethod().payment_method("钻石会员", "易贝", 10)
    print(a)
    b = '8.50'
    print(b)
