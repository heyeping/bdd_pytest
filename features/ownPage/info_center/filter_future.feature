Feature: # Enter feature name here
  Scenario: 消息中心- 筛选日期-筛选未来的日期
    Given 当前在我的页面
    When 点击【消息中心】筛选时间
    And 选择日期是30天前
    Then 显示没有消息报警缺省图