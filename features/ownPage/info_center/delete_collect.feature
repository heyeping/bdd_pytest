# Created by ayla at 2022/2/28
Feature: delete_collect
  【我的-消息中心】消息中心删除

    Scenario: 消息中心-当前用户删除收藏的消息
    Given 当前收藏了一条消息
    When 删除收藏的消息
    Then 当前用户不会再看见此条消息