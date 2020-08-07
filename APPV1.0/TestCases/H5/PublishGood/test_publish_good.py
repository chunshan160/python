#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 17:21
# @Author :春衫
# @File :test_publish_good.py

import time
import pytest
from PageObjects.Comm_Bus import CommBus
from TestData.H5.Publish_Data import *
from PageObjects.H5.PublishGood.Common import PublishGoodCommon
from PageObjects.H5.PublishGood.EntityGood_Page import EntityGoodPage


class TestPublishGood:

    @pytest.mark.usefixtures("open_app")
    @pytest.mark.parametrize("data", EntityGood_data)  # 替代ddt
    def test_1_publish_entity_good(self,open_app,data):
        # 首页点击发布商品
        CommBus(open_app).click_publish_good()
        time.sleep(1)
        # 选择发布实物商品
        PublishGoodCommon(open_app).publish_entity_good()
        time.sleep(1)
        EntityGoodPage(open_app).entity_good_information(data["product_title"], data["product_description"],
                                                            data["property_1"],
                                                            data["property_2"], data["purchase_price"],
                                                            data["sell_price"], data["stock"],
                                                            data["limit_quantity"])
        PublishGoodCommon(open_app).submit()
        # # 断言
        # text = SubmitReviewOKBusiness(self.driver).get_text()
        # self.assertTrue(text)
        # self.fd.find_element(good_audit_btn).click()

    # @ddt.data(*CouponGood_data)
    # def test_2_publish_coupon_good(self, data):
    #     time.sleep(1)
    #     # 选择发布本地生活商品
    #     self.fd.find_element(coupon_good).click()
    #     time.sleep(1)
    #     CouponGoodBusiness(self.driver).publish_coupon_good(data["product_title"], data["product_description"],
    #                                                         data["total_price"], data["stock"],
    #                                                         data["limit_quantity"])
    #     CouponGoodBusiness(self.driver).submit()
    #     # 断言
    #     text = SubmitReviewOKBusiness(self.driver).get_text()
    #     self.assertTrue(text)
    #     self.fd.find_element(good_audit_btn).click()
    #
    # @ddt.data(*ServerGood_data)
    # def test_3_publish_server_good(self, data):
    #     time.sleep(1)
    #     # 选择发布商企服务商品
    #     self.fd.find_element(services_good).click()
    #     time.sleep(1)
    #     ServicesGoodBusiness(self.driver).publish_services_good(data["product_title"], data["product_description"],
    #                                                             data["total_price"], data["subsist"], data["stock"],
    #                                                             data["limit_quantity"])
    #     ServicesGoodBusiness(self.driver).submit()
    #     # 断言
    #     text = SubmitReviewOKBusiness(self.driver).get_text()
    #     self.assertTrue(text)
    #     self.fd.find_element(good_audit_btn).click()
    #
    # def tearDown(cls):
    #     pass


if __name__ == '__main__':
    pytest.main(["-s","test_publish_good.py"])
