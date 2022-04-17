Feature: 艾拉智家登录
     Feature Description

     Scenario: 用户输入正确的账户和密码进行APP登录
      Given 使用账户:15802824470
      When 点击切换为密码登录
      When  用户点击下一步
      When  密码:123abc
      Then  用户登录成功
      Then  用户进行登出操作

