Feature: 一键执行

  不删除异常项点击保存

  Scenario: 一键场景-不删除异常项点击保存
    Given app已登录
    And 房间下有一建执行联动
    When 选择某个一键执行联动，进入其编辑页面
    And 点击"保存"按钮
    Then toast提示"智能场景异常，请删除异常任务"