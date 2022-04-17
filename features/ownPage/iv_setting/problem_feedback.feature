Feature: problem_feedback
  【设置-问题反馈】问题反馈

  Scenario: 问题反馈-点击返回-写了数据
    Given 当前在问题反馈页面，输入了数据
    When 点击返回按钮
    Then 弹窗提示用户是否返回

  Scenario: 问题反馈-正常提交
    Given 当前在问题反馈页面
    When 输入文案
    Then 选择一张图片
    Then 输入联系方式
    Then 点击提交按钮，正常提交弹窗提示