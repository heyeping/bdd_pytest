Feature: clear_cache
  【设置-清除缓存】点击清除缓存

  Scenario: 清除缓存-显示当前缓存-点击清除缓存
    Given 当前在设置页面
    When 查看清除缓存
    Then 缓存清理完成，重新获取应显示为0.00mb
    Then 会有toaSt提示用户清理完成