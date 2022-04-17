Feature: delete_family
  【我的-家庭】家庭管理

  Scenario: 删除家庭—家庭被成功删除
    Given 已存在成功创建家庭
    When 在家庭管理页面，删除家庭
    Then 二次确认弹窗点击“确定”
    Then 家庭被成功删除