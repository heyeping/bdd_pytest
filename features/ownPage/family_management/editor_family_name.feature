Feature: editor_family_name
  【我的-家庭】家庭管理

  Scenario: 家庭-创建家庭-家庭名称修改
    Given  在家庭页面
    When  修改家庭名称
    Then  家庭名称显示为刚刚修改的