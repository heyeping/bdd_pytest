Feature: 一键执行

  删除一个动作

  Scenario: 一键执行-删除一个动作
    Given 已存在一键执行联动A，联动内存在多个动作
    When 点击一键执行联动A
    Then 删除动作1
    Then 点击"完成"按钮
    Then 联动延时动作更新成功