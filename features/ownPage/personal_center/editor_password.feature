Feature: editor_info
  【我的-修改密码】设备管理

  Scenario: 修改密码-入口
    Given 当前在我的页面
    When 点击【设置】-【密码】
    Then 点击后跳转到修改密码页面

  Scenario: 修改密码-修改密码-密码修改成功
    Given 当前在设置新密码页面
    When 输入确认密码和新密码-数据一致
    Then 点击完成
    Then  修改完成弹窗提示用户变更完成

