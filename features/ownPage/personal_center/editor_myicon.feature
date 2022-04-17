Feature: personal_center
  【我的-个人中心】头像 昵称修改

  Scenario: 我的-个人中心
    Given 用户已登录
    When 点击元素我的
    And 点击元素个人中心
    Then 跳转页面text内容包含 头像 昵称

  Scenario: 我的-个人中心-头像
    Given 跳转页面text内容包含 头像 昵称
    When 点击元素头像
    And 更换头像
    Then 更换头像成功
