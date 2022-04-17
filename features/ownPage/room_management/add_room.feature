Feature: add_room_management
  【我的-房间管理】房间管理

  Scenario: 房间管理-房间管理入口验证_家庭看板处入口
    Given 当前在【我的】页面
    When 点击【xxx的家】下的【房间】
    Then 跳转到【房间管理】

  Scenario: 房间管理-添加房间_成功添加房间
    Given 已进入房间管理页面
    When 点击【添加房间】
    Then 输入房间名称（不存在的房间名称）
    Then 点击【确定】
    Then 返回房间管理页面，提示：房间创建成功，新建房间显示在房间管理页面

