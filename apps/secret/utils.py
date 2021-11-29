# -*- coding: utf-8 -*-
#
from common.utils import get_logger
from assets.models import BaseUser
from assets.const import StorageType
from .backends import Secret

logger = get_logger(__name__)


def get_secret_data(instance: BaseUser, name=None):
    field = instance.SECRET_FIELD
    backend = instance.storage_type
    if backend != StorageType.db:
        client = Secret(instance, backend)
        secret_data = client.get_secret()
        if name:
            return secret_data.get(name, '')
        else:
            return {i: secret_data.get(i, '') for i in field}
    else:
        if name:
            return getattr(instance, name)
        else:
            return {i: getattr(instance, i) for i in field}


def replace_secret(instance: BaseUser, name=None):
    secret_data = get_secret_data(name)
    if not name:
        for k, v in secret_data.items():
            setattr(instance, k, v)
    else:
        setattr(instance, name, secret_data)
