Feature: 修改一键执行

  一键执行-修改

  Scenario: 一键执行-修改
    Given app已登录在一键执行联动列表页面
    When 点击"更多"按钮
    Then 输入新的联动名称
    Then 切换新的icon
    Then 点击"保存"按钮
    Then 联动名称更新成功，一键联动列表页显示新的名称icon
