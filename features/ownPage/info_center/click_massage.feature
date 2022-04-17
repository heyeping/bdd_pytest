# Created by ayla at 2022/2/25
Feature: 消息中心

  Scenario: 消息中心-点击消息
    Given 当前在消息中心
    When 点击消息
    Then 点击单控/高级的返回按钮
    Then 返回到之前的ui