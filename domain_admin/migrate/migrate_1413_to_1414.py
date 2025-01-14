# -*- coding: utf-8 -*-
"""
@File    : migrate_1413_to_1414.py
@Date    : 2023-06-30

cmd:
$ python domain_admin/migrate/migrate_1413_to_1414.py
"""

from domain_admin.migrate import migrate_common
from domain_admin.model.base_model import db
from domain_admin.model.domain_info_model import DomainInfoModel


def execute_migrate():
    """
    版本升级 1.4.13 => 1.4.14
    :return:
    """
    migrator = migrate_common.get_migrator(db)

    migrate_rows = [
        migrator.add_column(
            DomainInfoModel._meta.table_name,
            DomainInfoModel.domain_registrar.name,
            DomainInfoModel.domain_registrar),

        migrator.add_column(
            DomainInfoModel._meta.table_name,
            DomainInfoModel.domain_registrar_url.name,
            DomainInfoModel.domain_registrar_url),
    ]

    migrate_common.try_execute_migrate(migrate_rows)
