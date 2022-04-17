Feature: editor_info
  【我的-修改密码】设备管理

  Scenario: 修改手机号-入口
    Given 当前在我的页面
    When 点击个人信息-手机号
    Then  跳转到更换手机号页面

  Scenario: 修改手机号-手机号修改成功
    Given 已经在输入变更手机号页面
    And 输入正确的手机号，验证码
    And 点击完成
    Then 弹窗提示”您的手机号已成功变更为 xxx*******xxx“，确认返回上级菜单