<!--
 Copyright (C) 2020 Yuboona Zhang
 
 PeoplePaper is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 PeoplePaper is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.
 
 You should have received a copy of the GNU Lesser General Public License
 along with PeoplePaper. If not, see <http://www.gnu.org/licenses/>.
-->

# people_paper_2018-2019


> 预处理后的人民日报数据集（2018-2019）  
> 下载地址：
> 1. 处理后的数据集：[百度网盘1](https://pan.baidu.com/s/1qGei8MexfJfodQEutUtuIw)
> 2. 未处理的数据集：[百度网盘2](https://pan.baidu.com/s/142aXMXFK2HkkqyHbf430-w)

## 1. 适用的任务

- 标点恢复，五种标点
- `['、', '，', '。', '？', '！']`

## 2. 处理方法(TextProc.ipynb)

- 去除了奇怪的字符
- 将部分标点转换成了五种标点之一
- 保留了部分无关任务的中文标点，不当做标点，将其当作文本的一部分

> 具体的标点处理方案：[punc.md](./punc.md)
