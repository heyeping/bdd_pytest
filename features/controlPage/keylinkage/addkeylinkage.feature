Feature: 添加一键联动

  正常添加一键执行联动

  Scenario: 验证正常添加一键执行联动
    Given 当前在创建一键执行联动ui且绑定有多个正常设备
    When 点击“+”按钮
    Then 在添加任务选择弹窗内选择“控制设备”
    Then 选择设备A的属性1，点击完成
    Then 在动作选择弹窗内选择“延时”
    Then 在延时设置弹窗内设置延时时间
    Then 点击完成
    Then 点击“+”按钮
    Then 选择设备A的属性2，点击完成
    Then 点击"保存"按钮
    Then 弹窗内输入执行名称
    Then 点击确定
    Then 联动保存成功，返回到联动列表页显示刚刚添加成功的联动
