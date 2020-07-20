#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 22:55
# @Author :春衫
# @File :project_path.py
import datetime
import os

"""专门来读取路径的值"""
# 当前目录的顶级路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试用例的路径
test_case_path = os.path.join(project_path, "TestData", "fenyong_data.xlsx")

# 测试报告的路径
test_report_path = os.path.join(project_path, "Report")

# 配置文件的路径
case_config_path = os.path.join(project_path, "Source", "case.config")

# 日志输出文件的路径
log_path = os.path.join(project_path, "Log")

#上传图片文件地址
image_path=os.path.join(project_path, "Source", "picture.jpg")

#报错截图
error_image=os.path.join(project_path,"Report", "Error_Image", datetime.datetime.now().strftime("%Y-%m-%d")+".png")

