import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/test01.yml")["ansible_facts"]


def test_zanata_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["zanata_user"]).exists
    assert Group(AnsibleDefaults["zanata_group"]).exists


def test_zanata_conf(File, User, Group, AnsibleDefaults):
    conf_path = File(AnsibleDefaults["zanata_conf_path"])
    assert conf_path.exists
    assert conf_path.is_directory
    assert conf_path.user == AnsibleDefaults["zanata_user"]
    assert conf_path.group == AnsibleDefaults["zanata_group"]


def test_zanata_service(File, Service, Socket, AnsibleDefaults):
    port = AnsibleDefaults["zanata_port"]
    assert File("/lib/systemd/system/zanata.service").exists
    assert Service("zanata").is_enabled
    assert Service("zanata").is_running
    assert Socket("tcp://:::" + str(port)).is_listening
