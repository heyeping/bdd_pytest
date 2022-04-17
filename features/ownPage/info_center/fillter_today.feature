Feature: # Enter feature name here
  Scenario: 消息中心- 筛选日期-筛选当前日期-有报警消息
    Given 当前在我的页面
    When 点击【消息中心】筛选时间
    And 选择日期是当天
    Then 显示当前的报警消息