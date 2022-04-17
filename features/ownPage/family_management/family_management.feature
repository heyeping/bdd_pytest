Feature: add_family
  【我的-家庭】家庭管理

  Scenario: 家庭-创建家庭
    Given 在创建家庭页面
    When 编辑家庭名称
    Then 点击保存
    Then 成功创建家庭

  Scenario: 删除家庭—家庭被成功删除
    Given 已存在成功创建家庭
    When 在家庭管理页面，删除家庭
    Then 二次确认弹窗点击“确定”
    Then 家庭被成功删除

  Scenario： 家庭-创建家庭-家庭位置修改
    Given  在创建家庭页面
    And  修改家庭定位为当前
    Then  点击查看家庭信息时，家庭定位显示为刚刚设置的

  Scenario： 家庭-创建家庭-家庭名称修改
    Given  在创建家庭页面
    And  修改家庭名称
    Then  点击查看家庭信息时，家庭名称显示为刚刚修改的