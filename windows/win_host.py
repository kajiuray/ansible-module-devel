#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2014, Phil Schwartz <schwartzmx@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_host
version_added: ""
short_description: Hostname setting, Timezone setting, and domain unjoining/joining module.
description:
     - Change the host's timezone, hostname, and domain.  Allows domain joining/unjoining, along with workgroup joining/unjoining.
options:
  hostname:
    description:
      - Hostname to change to
    required: false
    default: current nodes hostname
    aliases: []
  state:
    description:
      - Specify whether to join or unjoin
    required: true
    choices:
      - present
      - absent
    default: none
    aliases: []
  domain:
    description:
      - Domain name to join/unjoin
    required: false
    default: none
    aliases: []
  workgroup:
    description:
      - Workgroup name to join/unjoin
    required: no
    default: none
    aliases: []
  server:
    description:
      - Name of a domain controller
    required: no
    default: none
    aliases: []
  user:
    description:
      - User with permission to join/unjoin
    required: no
    default: none
    aliases: []
  pass:
    description:
      - Password for specified user
    required: no
    default: none
    aliases: []
  timezone:
    description:
      - Timezone to set host to Ex. Central Standard Time
    required: no
    default: none
    aliases: []
  options:
    description:
      - Single or comma separated list of options (AccountCreate, Win9XUpgrade, UnsecuredJoin, PasswordPass, JoinWithNewName, JoinReadOnly, InstallInvoke)
    required: no
    default: none
    aliases: []
  oupath:
    description:
      - Specifies an organizational unit for the domain account
    required: no
    default: none
    aliases: []
  restart:
    description:
      - Restart the host after completion
    required: no
    choices:
      - true
      - yes
      - false
      - no
    default: false
    aliases: []
  unsecure:
    description:
      - Perform an unsecure join, or unjoin.
    required: no
    choices:
      - true
      - yes
      - false
      - no
    default: false
    aliases: []




author: Phil Schwartz
'''

EXAMPLES = '''
# Change Hostname and Timezone
$ ansible -i hosts -m win_host -a "hostname=MyNewComp timezone='Eastern Standard Time'" all
# Add hostnames to domain
$ ansible -i hosts -m win_host -a "hostname=Comp1,Comp2,Comp3 timezone='Central Standard Time' domain=host.com state=present server=xyz.host.com user=Admin pass=Secret restart=true" all

# Playbook example
# Configure a new machine
---
- name: config machine
  hosts: all
  gather_facts: false
  roles:
    - initRole
    - anotherRole

  tasks:
    - name: Rename host, change timezone, and add to domain
      win_host:
        hostname: "NewComputerName"
        domain: "domainName.com"
        workgroup: "WORKGROUP"
        restart: "yes"
        state: "present"
        user: "domainName\Administrator"
        pass: "SecretPassword"
        timezone: "Central Standard Time"
        server: "domaincontroller.domainName.com"
    - name: Wait for reboot
      local_action:
        module: wait_for
        host: "{{ inventory_hostname }}"
        port: "{{ansible_ssh_port|default(5986)}}"
        delay: "15"
        timeout: "10000"
        state: "started"
      sudo: yes
'''
