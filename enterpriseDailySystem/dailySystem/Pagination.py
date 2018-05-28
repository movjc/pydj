# -*- coding: utf-8 -*-
class Pagination(object):
    """用于Model字段值的选择"""

    def __init__(self):
        pass

    @classmethod
    def create_pagination(self, from_name='', model_name='',
                          cur_page=1, start_page_omit_symbol='...',
                          end_page_omit_symbol='...', one_page_data_size=10,
                          show_page_item_len=9):
        """通过给的model和分页参数对相关model进行分页
        Args:
            from_name: 导入模块的 from后面的参数
                from {from_name} import model_name
            mode_name: 需要导入的模块名
                from from_name import {model_name}
            cur_page: 当前显示的是第几页
            start_page_omit_symbol: 超出的页数使用怎么样的省略号(前)
                ... 2 3 4
            end_page_omit_symbol: 超出的页数使用怎么样的省略号(后)
                1 2 3 4 ...
            one_page_data_size: 每一页显示几行
            show_page_item_len: 显示几个能点击的页数
        Return:
            pagination: dict
                    pagination = {
                        'objs': objs, # 需要显示model数据
                        'all_obj_counts': all_obj_counts, # 一共多少行数据
                        'start_pos': start_pos, # 数据分页开始的数据
                        'end_pos': end_pos, # 数据分页结束的数据
                        'all_page': all_page, # 一共有多少页
                        'cur_page': cur_page, # 当前的页码
                        'pre_page': pre_page, # 上一页的页码
                        'next_page': next_page, # 下一页的页码
                        'page_items': page_items, 能点击的页数
                        'start_page_omit_symbol': start_page_omit_symbol, # 开始的省略号
                        'end_page_omit_symbol': end_page_omit_symbol, # 结束的省略号
                    }
        Raise: None
        """
        # 如果没有输入导入模块需要的相关信息直接退出
        if not from_name or not model_name:
            return None

        import_str = 'from {from_name} import {model_name}'.format(
            from_name=from_name,
            model_name=model_name)
        # 导入模块
        exec import_str

        start_pos = (cur_page - 1) * one_page_data_size
        end_pos = start_pos + one_page_data_size

        # 查找需要的model数据
        find_objs_str = ('{model_name}.objects.all()'
                         '[{start_pos}:{end_pos}]'.format(
            model_name=model_name,
            start_pos=start_pos,
            end_pos=end_pos))
        objs = eval(find_objs_str)

        # 计算总共的页数
        find_objs_count_str = '{model_name}.objects.count()'.format(
            model_name=model_name)
        all_obj_counts = eval(find_objs_count_str)
        all_page = all_obj_counts / one_page_data_size
        remain_obj = all_obj_counts % one_page_data_size
        if remain_obj > 0:
            all_page += 1

            # 限制当前页不能小于1和并且大于总页数
        cur_page = 1 if cur_page < 1 else cur_page
        cur_page = all_page if cur_page > all_page else cur_page

        # 获得显示页数的最小页
        start_page = cur_page - show_page_item_len / 2
        if start_page > all_page - show_page_item_len:
            start_page = all_page - show_page_item_len + 1
        start_page = 1 if start_page < 1 else start_page

        # 获得显示页数的最大页
        end_page = cur_page + show_page_item_len / 2
        end_page = all_page if end_page > all_page else end_page
        if end_page < show_page_item_len and all_page > show_page_item_len:
            end_page = show_page_item_len

            # 获得上一页
        pre_page = cur_page - 1
        pre_page = 1 if pre_page < 1 else pre_page

        # 获得下一页
        next_page = cur_page + 1
        next_page = all_page if next_page > all_page else next_page

        # 处理省略符，是否显示
        if start_page <= 1:
            start_page_omit_symbol = ''

        if end_page >= all_page:
            end_page_omit_symbol = ''

            # 创建能点击的展示页码
        page_items = range(start_page, end_page + 1)

        pagination = {
            'objs': objs,
            'all_obj_counts': all_obj_counts,
            'start_pos': start_pos,
            'end_pos': end_pos,
            'all_page': all_page,
            'cur_page': cur_page,
            'pre_page': pre_page,
            'next_page': next_page,
            'page_items': page_items,
            'start_page_omit_symbol': start_page_omit_symbol,
            'end_page_omit_symbol': end_page_omit_symbol,
        }

        return pagination
