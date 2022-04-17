Feature: 一键执行

  删除所有动作

  Scenario: 一键执行-删除所有动作
    Given 已存在一键执行联动A，联动内存在多个动作
    When 点击一键执行联动A
    Then 删除全部动作
    Then 点击"完成"按钮
    Then toast提示"没有可执行任务"