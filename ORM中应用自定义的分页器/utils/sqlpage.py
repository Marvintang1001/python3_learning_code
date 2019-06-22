# 1.获取数据库连接
from django.db import connection
import math


class PageNumError(Exception):  #必须继承Exception父类
    #自定义异常：页码超出范围
    pass

class SqlPaginator(object):     #python3可以不写，默认继承
    #实现sql分页类：
    def __init__(self, sql, params, page_size):
        super().__init__()
        self.sql = sql      #要查询的sql
        self.params = params    #sql查询时候传递的参数
        self.page_size = page_size      #每页多少条数据

    @property
    def page_count(self):
        #数据表有多少页 = 总记录数/当前页码大小，向上取整
        return math.ceil(self.count / self.page_size)

    @property       #不需要传入特定的参数，所以把它变成一个属性而不是方法
    def count(self):
        #数据库总共有多少条记录
        count_sql = (
            'select count(1) from(' +self.sql + ') as count_record'
        )
        try:
            # 2。根据连接获取游标
            cursor = connection.cursor()
            # 3。根据游标执行sql
            cursor.execute(count_sql, self.params)
            rest = cursor.fetchone()
            rest = rest[0]
        except:
            rest = 0
        return rest

    def page(self, now_page):
        """
        获取当前页：
        :param now_page: 页码，需要判断是否超出总页数
        """
        if now_page > self.page_count or now_page < 1:
            raise PageNumError  #不符合规定，抛出错误
        offset = (now_page - 1) * self.page_size  # 偏移量：每页的首位置
        sql = self.sql + ' limit %s offset %s'      #不要漏了sql的空格

        # 2。根据连接获取游标
        cursor = connection.cursor()
        # 3。根据游标执行sql
        sql_params = self.params[:]     #这么做是不想一会用self.params时被干扰了，才新建一个列表做备份
        sql_params.extend([self.page_size, offset])     #一开始，self.params=[5]，后来变成[5, self.page_size, offset]
        #extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        cursor.execute(sql, sql_params)
        # 4。获取查询结果
        rows = cursor.fetchall()
        return rows
