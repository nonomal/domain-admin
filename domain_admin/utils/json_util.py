# -*- coding: utf-8 -*-
"""
@File    : json_util.py
@Date    : 2023-04-16
"""
import json
from datetime import datetime

from peewee import ModelSelect, Model
from playhouse.shortcuts import model_to_dict


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def default_json_encoder(o):
    """
    json 序列化
    :param o:
    :return:
    """

    if isinstance(o, ModelSelect):
        return list(o.dicts())

    if isinstance(o, Model):
        return model_to_dict(o)

    if isinstance(o, datetime):
        return o.strftime(DATETIME_FORMAT)

    return o


def json_encode(data, default=default_json_encoder, **kwargs):
    """
    json序列化
    :param data:
    :param default:
    :param kwargs:
    :return:
    """
    return json.dumps(data, default=default, **kwargs)
