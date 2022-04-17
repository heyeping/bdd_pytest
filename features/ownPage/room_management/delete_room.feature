Feature: delete_room_management
  【我的-房间管理】房间管理

  Scenario: 房间管理-删除房间_确认删除
    Given 已进入房间管理页面
    When 任选一个房间列向左滑动
    Then 点击【删除】按钮
    Then 弹窗消失，提示：删除成功。
