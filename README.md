![Logo](https://raw.githubusercontent.com/idealista/zanata-role/master/logo.gif)

# Zanata Ansible Role

This Ansible role installs a Zanata server in a Debian environment. Based on the instructions present in [Zanata Platform Documentation](http://docs.zanata.org/en/latest/user-guide/system-admin/configuration/installation/).

- [Getting Started](#getting-started)
    - [Prerequisities](#prerequisities)
    - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)

## Getting Started

These instructions will get you a copy of the role for your Ansible Playbook. Once launched, it will install a [Zanata](http://docs.zanata.org/en/latest/user-guide/system-admin/configuration/installation/) server in a Debian system.

### Prerequisities

Ansible 2.2.1.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista/zanata-role
  version: 1.1.0
  name: zanata
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: zanata }
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

Execute ``` molecule test ``` under zanata-role folder to run the automated tests suite.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.1.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/zanata-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/zanata-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.
