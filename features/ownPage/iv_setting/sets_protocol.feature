Feature: sets_protocol
  【设置-用户协议/隐私协议】两个页面的简单交互，如滑动、返回等

  Scenario: 设置-操作路由
    Given 用户已登录
    When 点击元素我的
    And 点击元素设置按钮
    Then 跳转页面text内容包含 用户协议 隐私协议

  Scenario: 设置-隐私协议
    Given 当前页面text内容包含 用户协议 隐私协议
    When   点击元素 隐私协议
    When  跳转进入title为 隐私政策 页面
    Then swip_down无误

  Scenario: 设置-用户协议
    Given 当前页面text内容包含 用户协议 隐私协议
    When  点击元素 用户协议
    And 跳转进入title为 用户政策 页面
    Then swip_down无误


