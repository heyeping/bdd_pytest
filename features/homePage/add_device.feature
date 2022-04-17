# @File  : add_device.feature
# @Author: yeping.he
# @Time  : 2021/11/29 14:20:12

Feature: 添加设备

    在家庭里添加网关、节点设备

    Scenario Outline: 添加网关
        Given 点击 添加设备+
        When 网关：<equipmentNet> 添加
        And 点击 已确认上述操作
        And 点击 下一步
        And 点击 我已确认上述操作
        And 点击 下一步
        And 点击 手动输入
      # And 点击 请输入设备ID
        And 输入 设备ID ： AC000W021752901
        And 点击 下一步
        And 点击 客厅
        And 点击 下一步
        And 点击 完成
        Then 检查网关：<equipmentNet>
        Examples:
            | equipmentNet |
            | 雅典智能网关   |

  Scenario Outline: 设备入网
    Given 点击 添加设备+
    And 网关：<equipmentNet> 添加
    And 点击 已确认上述操作
    And 点击 下一步
    And 点击 我已确认上述操作
    And 点击 下一步
    And 点击 手动输入
   # And 点击 请输入设备ID
    And 输入 设备ID ： AC000W021752901
    And 点击 下一步
    And 点击 客厅
    And 点击 下一步
    And 点击 完成
    When 网关设备：<equipmentType> 类型设备 <equipmentName> 入网 <equipmentNet>
    And 点击 我已确认上述操作
    And 点击 下一步
    And 开始 <equipmentName> 配网
    Then 检查设备：<equipmentName>
    Examples:
      | equipmentType | equipmentName | equipmentNet |
      | 照明          | 雅典智能射灯    | 雅典智能网关    |