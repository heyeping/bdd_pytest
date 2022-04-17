Feature: personal_center_nickname
  【我的-个人中心】头像 昵称修改

  Scenario: 我的-个人中心-昵称修改
    Given 跳转页面text内容包含 头像 昵称
    When 点击元素昵称
    Then 昵称修改
    Then 昵称修改成功