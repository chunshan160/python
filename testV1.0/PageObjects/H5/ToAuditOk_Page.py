#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/13 13:42
#@Author :春衫
#@File :ToAuditOk_Page.py

from PageLocators.H5.toAuditOk import *
from Common.find_element import FindElement


# 发布实物商品
class ToAuditOkPage:

    def __init__(self, driver):
        self.fd=FindElement(driver)

    def good_audit_text(self):
        return self.fd.find_element(good_audit_text)

    def good_audit_tip(self):
        return self.fd.find_element(good_audit_tip)

    def good_audit_btn(self):
        return self.fd.find_element(good_audit_btn)