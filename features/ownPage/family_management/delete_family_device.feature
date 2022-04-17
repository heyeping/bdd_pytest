Feature: delete_family_device
  【我的-家庭】家庭管理

  Scenario: 删除家庭——家庭与家庭下设备解除绑定
    Given 该家庭下，绑定有网关、节点设备、WiFi设备（包括红外及其他wifi设备如球泡灯）
    And 家庭主人登录app
    When 在家庭管理页面，删除家庭
    And 二次确认弹窗点击“确定”
    Then 返回上级页面；其他用户可直接绑定该网关；其他用户可直接绑定WiFi-红外设备