# Created by ayla at 2022/2/28
Feature: all_read
  【我的-消息中心】点击全部已读

  Scenario: 消息中心-点击全部已读
    Given 当前在消息中心有未读消息
    When 点击全部已读
    Then 点击后未读消息全部已读，小红点消失