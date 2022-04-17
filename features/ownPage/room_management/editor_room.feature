Feature: editor_room_management
  【我的-房间管理】房间管理

  Scenario: 房间管理-默认房间验证_修改数据
    Given 当前刚新建了一个家庭在其房间管理页面
    When 修改房间名称保存
    Then 返回房间管理页面时房间刷新与修改一致