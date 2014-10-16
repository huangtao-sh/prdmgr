#!/usr/bin/python3
# 项目：营运管理平台
# 模块：子窗口加载模块
# 作者：黄涛
# 创建：2014-7-22
# 修订：2014-08-04

#app清单
apps=[
        {
            'group':'report',
            'text':'数据导入(&I)',
            'class':'work.impdata.Import',
            'icon':'open.png',
            'shortcut':'Ctrl+I',
            },
        
        {
            'group':'tools',
            'text':'省直分行序列(&S)',
            'class':'work.fenhang.Fenhang',
            'icon':'branch.png',
            'shortcut':None,
            },
        {
            'group':'help',
            'text':'关于(&A)',
            'class':'work.about.About',
            'icon':'help.png',
            'shortcut':None,
            },
        {
            'group':'tools',
            'text':'利息计算',
            'class':'tools.interest.Interest',
            'icon':'save.png',
            'shortcut':None,
            },
        {
            'text':'测试',
            'class':'tools.test.Test',
            'group':'tools',
            },
        {
            'text':'联系人',
            'class':'work.contact.Contact',
            'group':'tools',
            'icon':'contact.png',
            }, 
        {
            'text':'数据库备份/恢复',
            'class':'tools.databackup.DataBackup',
            'icon':'db.png',
            'group':'tools',
            },
        {
            'group':'tools',
            'text':'计算素数',
            'class':'tools.sushu.SuShu',
            },
         {
            'group':'tools',
            'text':'公约数与公倍数',
            'class':'tools.sushu.GongYue',
            },
         {
            'group':'auth',
            'text':'用户签到',
            'class':'auth.users.Login',
            },
        {
            'group':'auth',
            'text':'修改密码',
            'class':'auth.users.ChangePwd',
            },
        {
            'group':'settings',
            'text':'功能管理',
            'class':'auth.permissions.Permissions',
            },
]
comm_app=[
    'auth.users.Login',
    'work.about.About',
    'tools.test.Test',
    'work.fenhang.Fenhang',
    ]
    
