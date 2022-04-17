  Scenario: 成员管理-删除成员
    Given 处于成员管理页面
    When 选择成员
    Then  删除成员
    Then 对应成员在app刷新后不能再选择该家庭，没有查看入口