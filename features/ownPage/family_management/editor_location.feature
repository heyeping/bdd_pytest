Feature: editor_location
  【我的-家庭】家庭管理

  Scenario: 家庭-创建家庭-家庭位置修改
    Given  在家庭页面
    When  修改家庭定位为当前
    Then  家庭定位显示为刚刚设置的