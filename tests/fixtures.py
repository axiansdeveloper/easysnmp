from __future__ import unicode_literals

import logging

import pytest
import easysnmp

# Disable logging for the C interface
snmp_logger = logging.getLogger('easysnmp.interface')
snmp_logger.disabled = True


@pytest.fixture
def sess_v1_args():
    return {
        'version': 1,
        'hostname': 'localhost',
        'remote_port': 11161,
        'community': 'public'
    }


@pytest.fixture
def sess_v2_args():
    return {
        'version': 2,
        'hostname': 'localhost',
        'remote_port': 11161,
        'community': 'public'
    }


@pytest.fixture
def sess_v3_args():
    return {
        'version': 3,
        'hostname': 'localhost',
        'remote_port': 11161,
        'security_level': 'authPriv',
        'security_username': 'initial',
        'privacy_password': 'priv_pass',
        'auth_password': 'auth_pass'
    }


@pytest.fixture
def sess_v1():
    return easysnmp.Session(**sess_v1_args())


@pytest.fixture
def sess_v2():
    return easysnmp.Session(**sess_v2_args())


@pytest.fixture
def sess_v3():
    return easysnmp.Session(**sess_v3_args())
