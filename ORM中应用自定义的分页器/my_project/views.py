from django.http import HttpResponse
from utils.sqlpage import PageNumError



def page_p_sql(request):
    # 使用自定义sql分页类：
    from utils.sqlpage import SqlPaginator
    try:
        page = int(request.GET.get('page', 1))  # 当前页码，保证是正数
    except:
        return HttpResponse('no valid page')
    sql = (
        ' select `id`, `username`, `nickname` from `weibo_user`'
        ' where `id` > %s'
    )

    sql_params = [20]  # 传入参数实现筛选id>20
    page_size = 10
    try:
        p = SqlPaginator(sql, sql_params, page_size)  # 类的实例化，传入属性
        page_data = p.page(page)  # page就是传给参数now_page的
        for row in page_data:
            print(row)

        count = p.count
        print('总记录数：', count)
        page_count = p.page_count
        print('总页数：', page_count)
    except PageNumError as e:
        return HttpResponse('invalid page number')

    return HttpResponse('ok')
