#!/usr/bin/python3
# 项目：用户管理模块
# 名称：QT5库函数
# 作者：黄涛
# 创建：2014-8-8
from work.basefrm import TransFrame
from settings import apps
class Permissions(TransFrame):

    query_sql='select codename from auth_permission where content_type_id=8000'
    insert_sql='insert into auth_permission(name,content_type_id,codename) '\
        'values(%s,8000,%s)'
    delete_sql='delete from auth_permission where codename=%s'
    def init(self):
        self.app_list=[(x['class'],x['text']) for x in apps]
        self['items']=self.app_list
        self['values']=self.query_list(self.query_sql)
    def submit(self):
        deleted,inserted=self['delta']
        if deleted:
            params=[(x,) for x in deleted]
            self.exec_many(self.delete_sql,params)
            self.notify('删除功能成功！')
            self.showinfo(','.join(deleted)+'<br/>已被删除')
        if inserted:
            params=[(b,a) for a,b in self.app_list if a in inserted]
            self.exec_many(self.insert_sql,params)
            self.notify('新增功能成功!')
            self.showinfo(','.join(inserted)+'<br/>添加成功')
