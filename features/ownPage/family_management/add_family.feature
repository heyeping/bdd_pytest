Feature: add_family
  【我的-家庭】家庭管理

  Scenario: 家庭-创建家庭
    Given 在创建家庭页面
    When 编辑家庭名称
    Then 点击保存
    Then 成功创建家庭