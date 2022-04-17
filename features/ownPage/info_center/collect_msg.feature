Feature: collect_msg
  【我的-消息中心】消息中心

  Scenario: 消息中心-收藏消息-一条
    Given 当前在消息中心
    When 点击收藏
    Then 切换到收藏table
    Then 展现刚收藏的消息

  Scenario: 消息中心-取消收藏
    Given 当前在消息中心
    When 取消收藏的消息
    Then 之前收藏的消息图标变为非收藏的