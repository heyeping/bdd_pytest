Feature: 添加云端联动

  正向流程

  Scenario: 添加云端联动-正向流程
    Given app已登录且房间下有可作为条件和动作的设备
    When 点击"添加条件"按钮
    And 在「选择设备」页面选择某个设备点击
    And 进入「功能选择」页面选择某个功能
    And 点击"完成"按钮
    And 跳转回添加页面，点击"添加动作"按钮
    And 在弹框中点击"设备控制"
    And 在「选择设备」页面选择某个设备点击
    And 进入「功能选择」页面选择某个功能
    And 点击"完成"按钮
    And 点击"保存"按钮
    And 在弹框中设置场景icon和名称
    And 点击"确认"按钮
    Then 保存成功，跳转回联动列表
