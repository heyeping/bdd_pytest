Feature: device_management
  【我的-设备管理】设备管理

  Scenario: 设备管理-设备管理入口验证_家庭看板处入口
    Given 在我的页面
    When 点击某一个家庭的设备
    Then 进入设备管理页面，全部下显示设备和对应房间
    Then 点击设备直接跳转高级页面
    Then 有移除权限的成员可移除设备