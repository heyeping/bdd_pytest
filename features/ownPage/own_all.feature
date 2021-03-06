Scenario:清除缓存- 显示当前缓存-点击清除缓存
    Given 当前在设置页面
    When 查看清除缓存
    Then 缓存清理完成，重新获取应显示为0.00mb
    Then 会有toaSt提示用户清理完成

Scenario:问题反馈-文案-输入500个文字
    Given 当前在问题反馈页面
    When 输入500字
    Then 文案上的字数动态变化（0-500/500），数据展现正常
Scenario:问题反馈-点击返回-写了数据
    Given 当前在问题反馈页面，输入了数据
    When 点击返回按钮
    Then 弹窗提示用户是否返回
Scenario:问题反馈-图片-上传一张点击提交
    Given 当前在问题反馈页面
    When 输入文案
    And 选择一张图片
    And 点击提交按钮
    Then 正常提交弹窗提示
Scenario:问题反馈-联系电话-输入电话
    Given 当前在问题反馈页面-描述文案已输入
    When 联系电话输入正常
    And 点击提交按钮
    Then 正常提交数据

Scenario:消息中心- 筛选日期-筛选当前日期-有报警消息
    Given 当前在我的页面
    When 点击【消息中心】筛选时间
    And 选择日期是当天
    Then 显示当前的报警消息

Scenario:消息中心- 筛选日期-筛选未来的日期
    Given 当前在我的页面
    When 点击【消息中心】筛选时间
    And 选择日期是30天前
    Then 显示没有消息报警缺省图
Scenario:  消息中心-当前用户删除收藏的消息
   Given 当前收藏了一条消息
   When 删除收藏的消息
   Then 当前用户不会再看见此条消息，但是同一个家庭下的其他用户依然能看见该消息

Scenario:   消息中心-批量删除消息-确认
    Given 当前在消息中心
    When 长按任意一条消息
    And 进入删除页面
    And 选择普通消息，未读消息，收藏消息进行删除
   Then 返回到进去编辑状态前的页面
   And 当前用户不会再看见相关消息，但是同一个家庭下的其他用户依然能看见该消息

Scenario:   消息中心-收藏消息-一条
    Given 当前在消息中心
    When 点击收藏
    And 切换到收藏table
    Then 展现刚收藏的消息
Scenario:   消息中心-取消收藏
    Given 当前在消息中心
    When 取消收藏的消息
    Then toaSt提示取消成功
    Then 之前收藏的消息图标变为非收藏的
Scenario:   消息中心-点击消息
    Given 当前在消息中心
    When 点击消息
    And 点击单控/高级的返回按钮
    Then 返回到之前的ui
Scenario:   消息中心 -点击全部已读
     Given 当前在消息中心有未读消息
     When 点击全部已读
     Then 点击后未读消息全部已读，小红点消失

Scenario:家庭-创建家庭
    Given 在创建家庭页面
    And 点击保存
    Then toast 文案：'请设置家庭名称'

#Scenario: 删除家庭——家庭与家庭下设备解除绑定
#    Given 该家庭下，绑定有网关、节点设备、WiFi设备（包括红外及其他wifi设备如球泡灯）
#    And 家庭主人登录app
#    When 在家庭管理页面，删除家庭
#    And 二次确认弹窗点击“确定”
#    Then 返回上级页面；其他用户可直接绑定该网关；其他用户可直接绑定WiFi-红外设备

Scenario: 删除家庭—家庭被成功删除
    Given 已存在成功创建家庭
    When 在家庭管理页面，删除家庭
    And 二次确认弹窗点击“确定”
    Then 家庭被成功删除

Scenario ：房间管理-添加房间_成功添加房间
    Given 已进入房间管理页面
    When 点击【添加房间】
    And 输入房间名称（不存在的房间名称）
    And 点击【确定】
    Then 返回房间管理页面，提示：房间创建成功，新建房间显示在房间管理页面
Scenario ：房间管理-默认房间验证_修改数据
    Given 当前刚新建了一个家庭在其房间管理页面
    When 修改房间名称保存
    Then 返回房间管理页面时房间刷新与修改一致
Scenario ：房间管理-房间管理入口验证_家庭看板处入口
    Given 当前在【我的】页面
    When 点击【xxx的家】下的【房间】
    Then 跳转到【房间管理】
Scenario ：房间管理-房间管理入口验证_家庭管理中入口
    Given 当前在【我的】页面
    When 点击【xxx的家】右边的【设置】图标
    And 点击【房间管理】
    Then 跳转到【家庭管理】页面，展示各种家庭信息
    Then 跳转到【房间管理】页面，展示各种房间信息
Scenario ：房间管理-默认房间验证_原始数据
    Given 当前刚新建了一个家庭在其房间管理页面
    When 查看ui默认数据
    Then 默认可选房间包含：客厅、主卧、次卧、厨房、餐厅（此处数据拿后端默认房间Tag的数据）
Scenario ：房间管理-删除房间_确认删除
    Given 已进入房间管理页面
    When任选一个房间列向左滑动
    And 点击【删除】按钮
    And 点击【确认】
    Then 弹窗消失，提示：删除成功。选择的房间被删除，该房间下的设备在设备列表首页被迁移到【全部】列下

Scenario ：设备管理-设备管理入口验证_家庭看板处入口
    Given 在我的页面
    When 点击某一个家庭的设备
    Then 进入设备管理页面，全部下显示设备和对应房间
    Then 点击设备直接跳转高级页面
    Then 有移除权限的成员可移除设备

Scenario： 修改密码-入口
    Given 当前在我的页面
    When 点击【设置】-【密码】
    Then 点击后跳转到修改密码页面
Scenario： 修改密码-修改密码-密码修改成功
    Given 当前在设置新密码页面
    When 输入确认密码和新密码-数据一致
    And 点击完成
    Then  修改完成弹窗提示用户变更完成
    Then 程序自动重新登录，不用用户再次手动去登录
Scenario： 修改手机号-入口
    Given 当前在我的页面
    When 点击个人信息-手机号
    Then  跳转到更换手机号页面
Scenario： 修改手机号-手机号修改成功
  Given 已经在输入变更手机号页面
  And 输入正确的手机号，验证码
  And 点击完成
  Then 弹窗提示”您的手机号已成功变更为 xxx*******xxx“，确认返回上级菜单

Scenario：场景速配-关闭
    Given 当前在实验室功能页面
    When 家庭1下的A用户关闭场景速配
    And A用户切换任意家庭创建联动
    Then A用户都不展现场景速配选项
    Then 和A用户同一个家庭的用户正常显示
Scenario：场景速配-开启
    Given 当前在实验室功能页面
    When 家庭1下的A用户开启场景速配
    And A用户切换任意家庭创建联动
    Then A用户都展现场景速配选项
    Then 和A用户同一个家庭的用户正常显示

Scenario： 家庭主人转移-转移成功
     Given 当前在主人转移页面
     When 输入正确的手机号和验证码
     And 点击完成
     Then 弹窗提示用户当前家庭转移成功到【xxxxxx】名下
     Then 【我知道了】按钮点击后跳转到返回「个人信息」页面