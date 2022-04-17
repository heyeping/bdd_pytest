Feature: 一键执行

  延时为最后一个动作

  Scenario: 一键执行-延时为最后一个动作
    Given 已存在一键执行联动A，联动内存在多个动作
    When 点击一键执行联动A
    Then 延时拖拽为最后一个动作
    Then 点击"完成"按钮
    Then toast提示"延时后必须添加一个设备 类型的动作"