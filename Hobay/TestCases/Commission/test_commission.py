#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_commission.py
import os

import allure
import pytest
from Common.DoExcel import DoExcel
from Common.fengyong.sql.reserve_fund_sql import reserve_fund_sql
from Common.fengyong.sql.wallet_detail import wallet_detail
from Common.fengyong.new_muban.moban2 import MoBan
from Common.fengyong.new_muban.Fan_Hui import fan_hui
from Common.fengyong.shangji.Superior_template import SuperiorTemplate
from Common.fengyong.tools.Calculation_Data import CalculationData
from Common.project_path import test_data_path
from Common.user_log import UserLog
from Common.fengyong.API.BuyEntityGoods import bug_entity_goods
from Common.fengyong.API.BuyCouponGoods import buy_coupon_goods
from Common.fengyong.API.BuyServerGoods import buy_server_goods
from Common.fengyong.tools.boss_setting import BossSetting
from Common.fengyong.tools.bing_relationship_data import BingRelationshipData
from Common.fengyong.tools.TransactionSecondPayagentRatio import TransactionSecondPayagentRatio
from Common.fengyong.API.delete_partner import delete_partner
from Common.fengyong.API.Recharge_behavior import recharge_behavior
from Common.fengyong.tools.get_js import get_js
from Common.project_path import allure_report

my_logger = UserLog()
test_data = DoExcel().get_data(test_data_path)


@allure.feature('测试分佣功能')
class TestCommission:

    @allure.story("测试分佣")
    @pytest.mark.smoke
    @pytest.mark.parametrize("item", test_data)
    def test_commission(self, item):
        my_logger.info(f"---------------------------------------------------")
        my_logger.info(f"----------开始执行用例{item['case_id']}，环境是{item['surroundings']}----------")

        ip = item['ip']
        data = eval(item['data'])
        buyer_phone = data['buyer_phone']
        seller_phone = data['seller_phone']
        buyer_id = data["买家"]
        seller_id=data["卖家"]

        with allure.step("获取绑定关系"):
            superior = SuperiorTemplate().superior_template_main(ip, item['payment_method'], item['data'], buyer_phone)
        # 环境
        surroundings = item['surroundings']
        with allure.step("Boss后台运营设置"):
            operational_setting = eval(item['operational_setting'])

        my_logger.info("----------开始BOSS后台设置运营分佣比例操作----------")

        with allure.step("Boss后台设置运营分佣比例"):
            BossSetting().main(ip, surroundings, item['payment_method'], superior, operational_setting)

        my_logger.info("----------BOSS后台运营分佣比例设置完毕----------")

        my_logger.info("----------开始执行前端操作----------")

        buyer_identity = item['buyer_identity']
        seller_identity = item['seller_identity']
        # 支付密码
        payPassword = get_js('runs', item['payPassword'])
        if buyer_identity == "公海用户":
            if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                my_logger.info("----------开始充值服务费----------")
                with allure.step("充值"):
                    recharge_behavior(surroundings, buyer_phone, payPassword)
                with allure.step("写回储备池和充值金额"):
                    reserve_fund_data = reserve_fund_sql(ip, buyer_id)
                    DoExcel.write_back_reserve_fund(test_data_path, item['sheet_name'], item['case_id'],
                                                    str(reserve_fund_data))

        if item['payment_method'] == "易贝":
            payType = 3
        elif item['payment_method'] == "易贝券":
            payType = 4
        elif item['payment_method'] == "家人购":
            payType = 5
        elif item['payment_method'] == "抵工资":
            payType = 6
        elif item['payment_method'] == "现金":
            payType = 7

        my_logger.info("----------开始购买商品----------")
        # 根据商品名判断流程
        if "实物商品" in item['goodsname']:
            with allure.step("购买实物商品"):
                order = bug_entity_goods(surroundings, buyer_phone, seller_phone, item['goodsname'], payType,
                                         payPassword)

        elif "本地生活" in item['goodsname']:
            with allure.step("购买本地生活"):
                order = buy_coupon_goods(surroundings, buyer_phone, seller_phone, item['goodsname'], payType,
                                         payPassword)

        elif "商企服务" in item['goodsname']:
            with allure.step("购买商企服务"):
                order = buy_server_goods(surroundings, buyer_phone, seller_phone, item['goodsname'], payType,
                                         payPassword)

        with allure.step("写回订单号"):
            # buyerid = data['买家']
            DoExcel.get_order(test_data_path, item['sheet_name'], item['case_id'], order)

        with allure.step("获取绑定关系，写回Excel"):
            superior = SuperiorTemplate().superior_template_main(ip, item['payment_method'], item['data'], buyer_phone)
            DoExcel.superior(test_data_path, item['sheet_name'], item['case_id'], str(superior))

        with allure.step("获取上级分佣比例，写回Excel"):
            proportion = SuperiorTemplate().fenyong_template_main(ip, item['payment_method'], superior)
            DoExcel.fenyong_bili(test_data_path, item['sheet_name'], item['case_id'], str(proportion))

        if buyer_identity == "公海用户":
            if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                my_logger.info("----------开始解除绑定关系----------")
                with allure.step("买家和卖家解绑"):
                    if seller_identity == "个人焕商":
                        delete_partner(surroundings, seller_phone, buyer_id)
                    elif seller_identity == "非焕商且已绑定个人焕商":
                        bangding_phone = data['bangding_phone']
                        delete_partner(surroundings, bangding_phone, buyer_id)

        my_logger.info("----------前端操作执行完毕----------")

        with allure.step("查询买家是否绑定销售/业务焕商/TCO"):
            with allure.step("获取买家绑定的销售/业务焕商/TCO"):
                if item['payment_method'] in ["易贝", "易贝券"]:
                    bind_buyer_relationship_data = BingRelationshipData().bing_relationship_data(ip,
                                                                                                 item['payment_method'],
                                                                                                 data, buyer_id)
                    with allure.step("把买家上级销售/业务焕商的上级写回Excel"):
                        DoExcel().bing_sale_id(test_data_path, item['sheet_name'], item['case_id'],
                                               str(bind_buyer_relationship_data))

                elif item['payment_method'] in ["抵工资", "家人购", "现金"]:
                    bind_relationship_data = BingRelationshipData().bing_relationship_data(ip, item['payment_method'],
                                                                                           data,
                                                                                           buyer_id)
                    bind_buyer_relationship_data = bind_relationship_data[0]
                    bind_payer_relationship_data = bind_relationship_data[1]
                    with allure.step("把买家上级销售/业务焕商的上级写回Excel"):
                        bind_buyer_relationship_id = {"储备金二级分佣对象": bind_buyer_relationship_data,
                                                      "支付服务费二级分佣对象": bind_payer_relationship_data}
                        DoExcel().bing_sale_id(test_data_path, item['sheet_name'], item['case_id'],
                                               str(bind_buyer_relationship_id))

        with allure.step("获取这笔订单应该【使用】的二级分佣比例"):

            transaction_second_payagent_ratio = TransactionSecondPayagentRatio().transaction_second_payagent_ratio(ip,
                                                                                                                   item[
                                                                                                                       'payment_method'],
                                                                                                                   superior,
                                                                                                                   data)
            with allure.step("把这笔订单所使用的二级分佣比例写回Excel"):
                DoExcel().second_payagent_ratio(test_data_path, item['sheet_name'], item['case_id'],
                                                str(transaction_second_payagent_ratio))

        my_logger.info("----------开始进行对比----------")

        buyer_identity = item['buyer_identity']
        seller_identity = item['seller_identity']
        data = eval(item['data'])

        try:
            if buyer_identity == "公海用户":
                if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                    charge_amount = reserve_fund_data['charge_amount']
                    reserve_fund = reserve_fund_data['reserve_fund']
                else:
                    charge_amount = None
                    reserve_fund = None
            else:
                charge_amount = None
                reserve_fund = None

            if item['payment_method'] in ["易贝", "易贝券","抵工资", "家人购"]:
                calculation_data = CalculationData().calculation_data(ip, item['payment_method'], item['member_level'],
                                                                  buyer_identity, seller_identity, proportion,
                                                                  charge_amount, reserve_fund, order,buyer_id)
            else:
                calculation_data = CalculationData().calculation_data(ip, item['payment_method'], item['member_level'],
                                                                      buyer_identity, seller_identity, proportion,
                                                                      charge_amount, reserve_fund, order, seller_id)

            if item['payment_method'] in ["易贝", "易贝券"]:
                bind_buyer_relationship_data = bind_buyer_relationship_data
                expected_moban = MoBan(buyer_identity, seller_identity, item['member_level'], item['payment_method'],
                                       order).expected_moban(ip, data, superior, reserve_fund, calculation_data,
                                                             transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data)

            elif item['payment_method'] in ["抵工资", "家人购", "现金"]:
                bind_buyer_relationship_data = bind_buyer_relationship_id['储备金二级分佣对象']
                bind_payer_relationship_data = bind_buyer_relationship_id['支付服务费二级分佣对象']
                expected_moban = MoBan(buyer_identity, seller_identity, item['member_level'], item['payment_method'],
                                       order).expected_moban(ip, data, superior, reserve_fund, calculation_data,
                                                             transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data, bind_payer_relationship_data)

            # 写回Excel用
            fanhui = fan_hui(ip, order, expected_moban)

            sql_data = wallet_detail(ip, order)

            for i in range(0, len(expected_moban)):
                assert expected_moban[i] == sql_data[i]
            my_logger.info("用例{0}正确！{1}".format(item['case_id'], item['title']))
            TestResult = 'Pass'
            Error = None

        except AssertionError as e:
            my_logger.info("用例错误！错误原因是第{0}行，{1}：".format(i + 1, e))
            TestResult = 'Failed'
            Error = "用例错误！错误原因是：第{0}行，{1}：".format(i + 1, e)
            raise e  # 异常处理完后记得抛出

        finally:  # 不管怎样都得写入Excel
            DoExcel().write_back(test_data_path, item['sheet_name'], item['case_id'] + 1,
                                 str(fanhui[0]), str(fanhui[2]), str(expected_moban),
                                 str(sql_data), TestResult, str(Error))
        my_logger.info("----------对比结束----------")
        my_logger.info(f"----------用例{item['case_id']}执行完毕----------")


if __name__ == '__main__':
    # pytest.main(
    #     ["-v", "-s", "--reruns", "1", "--reruns-delay", "1", "test_commission.py", "--alluredir",
    #      allure_report + "/result", "--clean-alluredir"])
    pytest.main(
        ["-v", "-s", "test_commission.py", "--alluredir", allure_report + "/result", "--clean-alluredir"])
    os.system(f"allure generate {allure_report}/result -o {allure_report}/html --clean")
