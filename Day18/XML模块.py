#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: XML模块.py
@time: 2018/8/17 0017 上午 11:11
"""

"""
XML跟JSON类似,也是常用的数据交换类型. xml常用于数据存储和传输，文件后缀为 .xml
XML设计用来传送及携带数据信息，不用来表现或展示数据，所以XML用途的焦点是它说明数据是什么，以及携带数据信息。
而HTML语言则用来表现数据.
XML使用DTD(document type definition)文档类型定义来组织数据;格式统一，跨平台和语言，早已成为业界公认的标准。

XML格式:是通过 < >  来区别数据结构, 用 </ > 来表示结束,比如：

<data>
    <country name='China'>
        <gdp>13600</gdp>
    <country name='Japan'>    
        <gdp>19900</gdp>
    </countr> 
</data>

JSON格式：是通过JSON字符串来表现,在Python中用dict来搭载
"""

# FIXME 前端概念——“属性” ： 包括名字,日期,排名等各种数据名字

# 在Python中操作XML
# XML是结构化数据形式，在ET中使用ElementTree代表整个XML文档，并视其为一棵树,树上有其他分支,Element代表这个文档树中的单个节点。
# 单个节点就是每个 < > 包含的信息
# element对象都具有以下属性：
#
# 　　1. tag：string对象，表示数据代表的种类。
#
# 　　2. attrib：dictionary对象，表示附有的属性。
#
# 　　3. text：string对象，表示element的内容。
#
# 　　4. tail：string对象，表示element闭合之后的尾迹。
#
# 　　5. 若干子元素（child elements）。
#
#    <tag attrib1=1> text </tag>tail
#      1     2        3         4
#
# 从硬盘的xml文件读取数据 3步：
#
# 1.导入 xml.etree.cElementTree as ET
#
# 2.解析(parse)XML,载入数据
#
# 3.获取根节点

import xml.etree.ElementTree as ET

tree = ET.parse("XML_test")  # 载入数据 tree就是解析出的数据 ：用ET模块来解析XML

root = tree.getroot()  # 获取根节点

print(root.tag)  # data


# 遍历xml文档
for child in root:    # 根目录下有2个子文件，china 和 Japan
    print(child.tag, child.attrib)
    # tag标签名：country {'name': 'China'}
    #          country {'name': 'Japan'}
    for i in child:   # 子文件里面 就1个属性 gdp
        print(i.tag, i.text)
        #  attrib属性： gdp 13600  year 2017
        #              gdp 19900  year 2017


# 修改XML文档
for node in root.iter('year'):  # root.iter('标签') 表示指定 标签
    new_year = node.text    # .text 就是返回 Unicode 类型
    new_year = 2018    # 给 new_year 赋值
    node.text = str(new_year)   # 再把new_year 转回字符串
    print(new_year)

tree.write('year修正后.xml')  # 最后写入 XML文档 2017-->2018


# 把gdp少于 5000 的国家排除
for country in root.findall('country'):
    country_gdp = int(country.find('gdp').text)
    if country_gdp < 5000:
        root.remove(country)

tree.write('gdp修整后.xml')  # 最后写入






