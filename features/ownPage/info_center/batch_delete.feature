Feature: batch_delete
  【我的-消息中心】批量删除消息

  Scenario: 消息中心-批量删除消息-确认
    Given 当前在消息中心
    When 长按任意一条消息,进入删除页面
    Then 选择普通消息，未读消息，收藏消息进行删除
    Then 返回到进去编辑状态前的页面
    Then 当前用户不会再看见相关消息