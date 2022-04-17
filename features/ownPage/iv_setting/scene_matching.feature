Feature: Scene_matching
  【设置-场景速配】设备管理

  Scenario: 场景速配-关闭
    Given 当前在实验室功能页面
    When 家庭1下的A用户关闭场景速配
    And A用户切换任意家庭创建联动
    Then A用户都不展现场景速配选项
    Then 和A用户同一个家庭的用户正常显示

  Scenario: 场景速配-开启
    Given 当前在实验室功能页面
    When 家庭1下的A用户开启场景速配
    And A用户切换任意家庭创建联动
    Then A用户都展现场景速配选项
    Then 和A用户同一个家庭的用户正常显示

  Scenario: 家庭主人转移-转移成功
    Given 当前在主人转移页面
    When 输入正确的手机号和验证码
    And 点击完成
    Then 弹窗提示用户当前家庭转移成功到【xxxxxx】名下
    Then 【我知道了】按钮点击后跳转到返回「个人信息」页面