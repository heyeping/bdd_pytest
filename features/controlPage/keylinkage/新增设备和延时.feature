Feature: 一键执行

  新增设备和延时

  Scenario: 一键执行-新增设备和延时
    Given 已存在一键执行联动A
    When 点击一键执行联动A
    Then 点击动作中的延时
    Then 编辑延时时间
    Then 在设备属性选择页中重新选择设备属性
    Then 点击"完成"按钮
    Then 点击"保存"按钮，联动动作更新成功