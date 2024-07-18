#!/bin/bash
# -*- coding: utf-8 -*-
#
# Module implementing.
# author: Reinering
# email: nbxlhc@hotmail.com
#

PYTHON=python3

# 生成项目的requirements.txt，只扫描依赖库
# pipqreqs.py 修改 line:121 忽略 "/model"目录
# print("file_name", file_name)
# if "/model" in file_name:
#     continue
#
# 安装项目的依赖库
# pip install -r requriements.txt



set -e

project_dir=$(cd $(dirname $0); cd ..; pwd)
file=$project_dir/requirements.txt

cd $(dirname $0)

if [[ $1 = "install" ]]; then
  if [ $2 ]; then
    file=$2
  fi

  $PYTHON -m pip install -r $file
else
  rm -f $file
  pipreqs $project_dir --encoding=utf8 --clean $file --force
fi


