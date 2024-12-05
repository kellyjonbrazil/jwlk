#!/usr/bin/env python3

import os
import sys
import io
import contextlib
import copy
import unittest
from unittest.mock import patch
import jello.cli
from jello.lib import opts


THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTests(unittest.TestCase):

    def setUp(self):
        # initialize options
        opts.initialize = None
        opts.version_info = None
        opts.helpme = None
        opts.compact = None
        opts.nulls = None
        opts.empty = None
        opts.raw = None
        opts.lines = None
        opts.force_color = None
        opts.mono = None
        opts.schema = None
        opts.types = None
        opts.keyname_color = None
        opts.keyword_color = None
        opts.number_color = None
        opts.string_color = None
        opts.flatten = None
        opts.stream_input = None

        self.jc_a_output = '''{"name": "jc", "version": "1.9.3", "description": "jc cli output JSON conversion tool", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "parser_count": 50, "parsers": [{"name": "airport", "argument": "--airport", "version": "1.0", "description": "airport -I command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["darwin"], "magic_commands": ["airport -I"]}, {"name": "airport_s", "argument": "--airport-s", "version": "1.0", "description": "airport -s command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["darwin"], "magic_commands": ["airport -s"]}, {"name": "arp", "argument": "--arp", "version": "1.2", "description": "arp command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["arp"]}, {"name": "blkid", "argument": "--blkid", "version": "1.0", "description": "blkid command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["blkid"]}, {"name": "crontab", "argument": "--crontab", "version": "1.1", "description": "crontab command and file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["crontab"]}, {"name": "crontab_u", "argument": "--crontab-u", "version": "1.0", "description": "crontab file parser with user support", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "csv", "argument": "--csv", "version": "1.0", "description": "CSV file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using the python standard csv library", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "df", "argument": "--df", "version": "1.1", "description": "df command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin"], "magic_commands": ["df"]}, {"name": "dig", "argument": "--dig", "version": "1.1", "description": "dig command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["dig"]}, {"name": "du", "argument": "--du", "version": "1.1", "description": "du command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["du"]}, {"name": "env", "argument": "--env", "version": "1.1", "description": "env command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"], "magic_commands": ["env"]}, {"name": "file", "argument": "--file", "version": "1.1", "description": "file command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["file"]}, {"name": "free", "argument": "--free", "version": "1.0", "description": "free command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["free"]}, {"name": "fstab", "argument": "--fstab", "version": "1.0", "description": "fstab file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"]}, {"name": "group", "argument": "--group", "version": "1.0", "description": "/etc/group file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "gshadow", "argument": "--gshadow", "version": "1.0", "description": "/etc/gshadow file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd"]}, {"name": "history", "argument": "--history", "version": "1.2", "description": "history command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Optimizations by https://github.com/philippeitis", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"]}, {"name": "hosts", "argument": "--hosts", "version": "1.0", "description": "/etc/hosts file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "id", "argument": "--id", "version": "1.0", "description": "id command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["id"]}, {"name": "ifconfig", "argument": "--ifconfig", "version": "1.5", "description": "ifconfig command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["ifconfig"]}, {"name": "ini", "argument": "--ini", "version": "1.0", "description": "INI file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using configparser from the standard library", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "iptables", "argument": "--iptables", "version": "1.1", "description": "iptables command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["iptables"]}, {"name": "jobs", "argument": "--jobs", "version": "1.0", "description": "jobs command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["jobs"]}, {"name": "last", "argument": "--last", "version": "1.0", "description": "last and lastb command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["last", "lastb"]}, {"name": "ls", "argument": "--ls", "version": "1.3", "description": "ls command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["ls"]}, {"name": "lsblk", "argument": "--lsblk", "version": "1.3", "description": "lsblk command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["lsblk"]}, {"name": "lsmod", "argument": "--lsmod", "version": "1.1", "description": "lsmod command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["lsmod"]}, {"name": "lsof", "argument": "--lsof", "version": "1.0", "description": "lsof command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["lsof"]}, {"name": "mount", "argument": "--mount", "version": "1.1", "description": "mount command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin"], "magic_commands": ["mount"]}, {"name": "netstat", "argument": "--netstat", "version": "1.2", "description": "netstat command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["netstat"]}, {"name": "ntpq", "argument": "--ntpq", "version": "1.0", "description": "ntpq -p command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["ntpq"]}, {"name": "passwd", "argument": "--passwd", "version": "1.0", "description": "/etc/passwd file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "pip_list", "argument": "--pip-list", "version": "1.0", "description": "pip list command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"], "magic_commands": ["pip list", "pip3 list"]}, {"name": "pip_show", "argument": "--pip-show", "version": "1.0", "description": "pip show command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"], "magic_commands": ["pip show", "pip3 show"]}, {"name": "ps", "argument": "--ps", "version": "1.1", "description": "ps command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["ps"]}, {"name": "route", "argument": "--route", "version": "1.0", "description": "route command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["route"]}, {"name": "shadow", "argument": "--shadow", "version": "1.0", "description": "/etc/shadow file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "ss", "argument": "--ss", "version": "1.0", "description": "ss command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["ss"]}, {"name": "stat", "argument": "--stat", "version": "1.0", "description": "stat command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["stat"]}, {"name": "systemctl", "argument": "--systemctl", "version": "1.0", "description": "systemctl command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl"]}, {"name": "systemctl_lj", "argument": "--systemctl-lj", "version": "1.0", "description": "systemctl list-jobs command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl list-jobs"]}, {"name": "systemctl_ls", "argument": "--systemctl-ls", "version": "1.0", "description": "systemctl list-sockets command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl list-sockets"]}, {"name": "systemctl_luf", "argument": "--systemctl-luf", "version": "1.0", "description": "systemctl list-unit-files command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl list-unit-files"]}, {"name": "timedatectl", "argument": "--timedatectl", "version": "1.0", "description": "timedatectl status command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["timedatectl", "timedatectl status"]}, {"name": "uname", "argument": "--uname", "version": "1.1", "description": "uname -a command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin"], "magic_commands": ["uname"]}, {"name": "uptime", "argument": "--uptime", "version": "1.0", "description": "uptime command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["uptime"]}, {"name": "w", "argument": "--w", "version": "1.0", "description": "w command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["w"]}, {"name": "who", "argument": "--who", "version": "1.0", "description": "who command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["who"]}, {"name": "xml", "argument": "--xml", "version": "1.0", "description": "XML file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using the xmltodict library at https://github.com/martinblech/xmltodict", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "yaml", "argument": "--yaml", "version": "1.0", "description": "YAML file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}]}'''

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/twitterdata.jlines'), 'r', encoding='utf-8') as f:
            self.twitterdata = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/twitterdata.json'), 'r', encoding='utf-8') as f:
            self.twitterdata_output = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/twitter-table-output.jlines'), 'r', encoding='utf-8') as f:
            self.twitter_table_output = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/twitter-table-output.schema'), 'r', encoding='utf-8') as f:
            self.twitter_table_output_schema = f.read()

    def test_jc_a(self):
        """
        Test jc -a | jello
        """
        expected = '''\
{
  "name": "jc",
  "version": "1.9.3",
  "description": "jc cli output JSON conversion tool",
  "author": "Kelly Brazil",
  "author_email": "kellyjonbrazil@gmail.com",
  "parser_count": 50,
  "parsers": [
    {
      "name": "airport",
      "argument": "--airport",
      "version": "1.0",
      "description": "airport -I command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "darwin"
      ],
      "magic_commands": [
        "airport -I"
      ]
    },
    {
      "name": "airport_s",
      "argument": "--airport-s",
      "version": "1.0",
      "description": "airport -s command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "darwin"
      ],
      "magic_commands": [
        "airport -s"
      ]
    },
    {
      "name": "arp",
      "argument": "--arp",
      "version": "1.2",
      "description": "arp command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "arp"
      ]
    },
    {
      "name": "blkid",
      "argument": "--blkid",
      "version": "1.0",
      "description": "blkid command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "blkid"
      ]
    },
    {
      "name": "crontab",
      "argument": "--crontab",
      "version": "1.1",
      "description": "crontab command and file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "crontab"
      ]
    },
    {
      "name": "crontab_u",
      "argument": "--crontab-u",
      "version": "1.0",
      "description": "crontab file parser with user support",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "csv",
      "argument": "--csv",
      "version": "1.0",
      "description": "CSV file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using the python standard csv library",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "df",
      "argument": "--df",
      "version": "1.1",
      "description": "df command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin"
      ],
      "magic_commands": [
        "df"
      ]
    },
    {
      "name": "dig",
      "argument": "--dig",
      "version": "1.1",
      "description": "dig command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "dig"
      ]
    },
    {
      "name": "du",
      "argument": "--du",
      "version": "1.1",
      "description": "du command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "du"
      ]
    },
    {
      "name": "env",
      "argument": "--env",
      "version": "1.1",
      "description": "env command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "env"
      ]
    },
    {
      "name": "file",
      "argument": "--file",
      "version": "1.1",
      "description": "file command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "file"
      ]
    },
    {
      "name": "free",
      "argument": "--free",
      "version": "1.0",
      "description": "free command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "free"
      ]
    },
    {
      "name": "fstab",
      "argument": "--fstab",
      "version": "1.0",
      "description": "fstab file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ]
    },
    {
      "name": "group",
      "argument": "--group",
      "version": "1.0",
      "description": "/etc/group file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "gshadow",
      "argument": "--gshadow",
      "version": "1.0",
      "description": "/etc/gshadow file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "history",
      "argument": "--history",
      "version": "1.2",
      "description": "history command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Optimizations by https://github.com/philippeitis",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "hosts",
      "argument": "--hosts",
      "version": "1.0",
      "description": "/etc/hosts file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "id",
      "argument": "--id",
      "version": "1.0",
      "description": "id command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "id"
      ]
    },
    {
      "name": "ifconfig",
      "argument": "--ifconfig",
      "version": "1.5",
      "description": "ifconfig command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "ifconfig"
      ]
    },
    {
      "name": "ini",
      "argument": "--ini",
      "version": "1.0",
      "description": "INI file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using configparser from the standard library",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "iptables",
      "argument": "--iptables",
      "version": "1.1",
      "description": "iptables command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "iptables"
      ]
    },
    {
      "name": "jobs",
      "argument": "--jobs",
      "version": "1.0",
      "description": "jobs command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "jobs"
      ]
    },
    {
      "name": "last",
      "argument": "--last",
      "version": "1.0",
      "description": "last and lastb command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "last",
        "lastb"
      ]
    },
    {
      "name": "ls",
      "argument": "--ls",
      "version": "1.3",
      "description": "ls command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "ls"
      ]
    },
    {
      "name": "lsblk",
      "argument": "--lsblk",
      "version": "1.3",
      "description": "lsblk command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "lsblk"
      ]
    },
    {
      "name": "lsmod",
      "argument": "--lsmod",
      "version": "1.1",
      "description": "lsmod command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "lsmod"
      ]
    },
    {
      "name": "lsof",
      "argument": "--lsof",
      "version": "1.0",
      "description": "lsof command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "lsof"
      ]
    },
    {
      "name": "mount",
      "argument": "--mount",
      "version": "1.1",
      "description": "mount command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin"
      ],
      "magic_commands": [
        "mount"
      ]
    },
    {
      "name": "netstat",
      "argument": "--netstat",
      "version": "1.2",
      "description": "netstat command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "netstat"
      ]
    },
    {
      "name": "ntpq",
      "argument": "--ntpq",
      "version": "1.0",
      "description": "ntpq -p command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "ntpq"
      ]
    },
    {
      "name": "passwd",
      "argument": "--passwd",
      "version": "1.0",
      "description": "/etc/passwd file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "pip_list",
      "argument": "--pip-list",
      "version": "1.0",
      "description": "pip list command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "pip list",
        "pip3 list"
      ]
    },
    {
      "name": "pip_show",
      "argument": "--pip-show",
      "version": "1.0",
      "description": "pip show command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "pip show",
        "pip3 show"
      ]
    },
    {
      "name": "ps",
      "argument": "--ps",
      "version": "1.1",
      "description": "ps command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "ps"
      ]
    },
    {
      "name": "route",
      "argument": "--route",
      "version": "1.0",
      "description": "route command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "route"
      ]
    },
    {
      "name": "shadow",
      "argument": "--shadow",
      "version": "1.0",
      "description": "/etc/shadow file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "ss",
      "argument": "--ss",
      "version": "1.0",
      "description": "ss command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "ss"
      ]
    },
    {
      "name": "stat",
      "argument": "--stat",
      "version": "1.0",
      "description": "stat command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "stat"
      ]
    },
    {
      "name": "systemctl",
      "argument": "--systemctl",
      "version": "1.0",
      "description": "systemctl command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl"
      ]
    },
    {
      "name": "systemctl_lj",
      "argument": "--systemctl-lj",
      "version": "1.0",
      "description": "systemctl list-jobs command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl list-jobs"
      ]
    },
    {
      "name": "systemctl_ls",
      "argument": "--systemctl-ls",
      "version": "1.0",
      "description": "systemctl list-sockets command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl list-sockets"
      ]
    },
    {
      "name": "systemctl_luf",
      "argument": "--systemctl-luf",
      "version": "1.0",
      "description": "systemctl list-unit-files command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl list-unit-files"
      ]
    },
    {
      "name": "timedatectl",
      "argument": "--timedatectl",
      "version": "1.0",
      "description": "timedatectl status command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "timedatectl",
        "timedatectl status"
      ]
    },
    {
      "name": "uname",
      "argument": "--uname",
      "version": "1.1",
      "description": "uname -a command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin"
      ],
      "magic_commands": [
        "uname"
      ]
    },
    {
      "name": "uptime",
      "argument": "--uptime",
      "version": "1.0",
      "description": "uptime command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "uptime"
      ]
    },
    {
      "name": "w",
      "argument": "--w",
      "version": "1.0",
      "description": "w command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "w"
      ]
    },
    {
      "name": "who",
      "argument": "--who",
      "version": "1.0",
      "description": "who command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "who"
      ]
    },
    {
      "name": "xml",
      "argument": "--xml",
      "version": "1.0",
      "description": "XML file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using the xmltodict library at https://github.com/martinblech/xmltodict",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "yaml",
      "argument": "--yaml",
      "version": "1.0",
      "description": "YAML file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    }
  ]
}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_s(self):
        """
        Test jc -a | jello -s
        """
        expected = '''\
_ = {};
_.name = "jc";
_.version = "1.9.3";
_.description = "jc cli output JSON conversion tool";
_.author = "Kelly Brazil";
_.author_email = "kellyjonbrazil@gmail.com";
_.parser_count = 50;
_.parsers = [];
_.parsers[0] = {};
_.parsers[0].name = "airport";
_.parsers[0].argument = "--airport";
_.parsers[0].version = "1.0";
_.parsers[0].description = "airport -I command parser";
_.parsers[0].author = "Kelly Brazil";
_.parsers[0].author_email = "kellyjonbrazil@gmail.com";
_.parsers[0].compatible = [];
_.parsers[0].compatible[0] = "darwin";
_.parsers[0].magic_commands = [];
_.parsers[0].magic_commands[0] = "airport -I";
_.parsers[1] = {};
_.parsers[1].name = "airport_s";
_.parsers[1].argument = "--airport-s";
_.parsers[1].version = "1.0";
_.parsers[1].description = "airport -s command parser";
_.parsers[1].author = "Kelly Brazil";
_.parsers[1].author_email = "kellyjonbrazil@gmail.com";
_.parsers[1].compatible = [];
_.parsers[1].compatible[0] = "darwin";
_.parsers[1].magic_commands = [];
_.parsers[1].magic_commands[0] = "airport -s";
_.parsers[2] = {};
_.parsers[2].name = "arp";
_.parsers[2].argument = "--arp";
_.parsers[2].version = "1.2";
_.parsers[2].description = "arp command parser";
_.parsers[2].author = "Kelly Brazil";
_.parsers[2].author_email = "kellyjonbrazil@gmail.com";
_.parsers[2].compatible = [];
_.parsers[2].compatible[0] = "linux";
_.parsers[2].compatible[1] = "aix";
_.parsers[2].compatible[2] = "freebsd";
_.parsers[2].compatible[3] = "darwin";
_.parsers[2].magic_commands = [];
_.parsers[2].magic_commands[0] = "arp";
_.parsers[3] = {};
_.parsers[3].name = "blkid";
_.parsers[3].argument = "--blkid";
_.parsers[3].version = "1.0";
_.parsers[3].description = "blkid command parser";
_.parsers[3].author = "Kelly Brazil";
_.parsers[3].author_email = "kellyjonbrazil@gmail.com";
_.parsers[3].compatible = [];
_.parsers[3].compatible[0] = "linux";
_.parsers[3].magic_commands = [];
_.parsers[3].magic_commands[0] = "blkid";
_.parsers[4] = {};
_.parsers[4].name = "crontab";
_.parsers[4].argument = "--crontab";
_.parsers[4].version = "1.1";
_.parsers[4].description = "crontab command and file parser";
_.parsers[4].author = "Kelly Brazil";
_.parsers[4].author_email = "kellyjonbrazil@gmail.com";
_.parsers[4].compatible = [];
_.parsers[4].compatible[0] = "linux";
_.parsers[4].compatible[1] = "darwin";
_.parsers[4].compatible[2] = "aix";
_.parsers[4].compatible[3] = "freebsd";
_.parsers[4].magic_commands = [];
_.parsers[4].magic_commands[0] = "crontab";
_.parsers[5] = {};
_.parsers[5].name = "crontab_u";
_.parsers[5].argument = "--crontab-u";
_.parsers[5].version = "1.0";
_.parsers[5].description = "crontab file parser with user support";
_.parsers[5].author = "Kelly Brazil";
_.parsers[5].author_email = "kellyjonbrazil@gmail.com";
_.parsers[5].compatible = [];
_.parsers[5].compatible[0] = "linux";
_.parsers[5].compatible[1] = "darwin";
_.parsers[5].compatible[2] = "aix";
_.parsers[5].compatible[3] = "freebsd";
_.parsers[6] = {};
_.parsers[6].name = "csv";
_.parsers[6].argument = "--csv";
_.parsers[6].version = "1.0";
_.parsers[6].description = "CSV file parser";
_.parsers[6].author = "Kelly Brazil";
_.parsers[6].author_email = "kellyjonbrazil@gmail.com";
_.parsers[6].details = "Using the python standard csv library";
_.parsers[6].compatible = [];
_.parsers[6].compatible[0] = "linux";
_.parsers[6].compatible[1] = "darwin";
_.parsers[6].compatible[2] = "cygwin";
_.parsers[6].compatible[3] = "win32";
_.parsers[6].compatible[4] = "aix";
_.parsers[6].compatible[5] = "freebsd";
_.parsers[7] = {};
_.parsers[7].name = "df";
_.parsers[7].argument = "--df";
_.parsers[7].version = "1.1";
_.parsers[7].description = "df command parser";
_.parsers[7].author = "Kelly Brazil";
_.parsers[7].author_email = "kellyjonbrazil@gmail.com";
_.parsers[7].compatible = [];
_.parsers[7].compatible[0] = "linux";
_.parsers[7].compatible[1] = "darwin";
_.parsers[7].magic_commands = [];
_.parsers[7].magic_commands[0] = "df";
_.parsers[8] = {};
_.parsers[8].name = "dig";
_.parsers[8].argument = "--dig";
_.parsers[8].version = "1.1";
_.parsers[8].description = "dig command parser";
_.parsers[8].author = "Kelly Brazil";
_.parsers[8].author_email = "kellyjonbrazil@gmail.com";
_.parsers[8].compatible = [];
_.parsers[8].compatible[0] = "linux";
_.parsers[8].compatible[1] = "aix";
_.parsers[8].compatible[2] = "freebsd";
_.parsers[8].compatible[3] = "darwin";
_.parsers[8].magic_commands = [];
_.parsers[8].magic_commands[0] = "dig";
_.parsers[9] = {};
_.parsers[9].name = "du";
_.parsers[9].argument = "--du";
_.parsers[9].version = "1.1";
_.parsers[9].description = "du command parser";
_.parsers[9].author = "Kelly Brazil";
_.parsers[9].author_email = "kellyjonbrazil@gmail.com";
_.parsers[9].compatible = [];
_.parsers[9].compatible[0] = "linux";
_.parsers[9].compatible[1] = "darwin";
_.parsers[9].compatible[2] = "aix";
_.parsers[9].compatible[3] = "freebsd";
_.parsers[9].magic_commands = [];
_.parsers[9].magic_commands[0] = "du";
_.parsers[10] = {};
_.parsers[10].name = "env";
_.parsers[10].argument = "--env";
_.parsers[10].version = "1.1";
_.parsers[10].description = "env command parser";
_.parsers[10].author = "Kelly Brazil";
_.parsers[10].author_email = "kellyjonbrazil@gmail.com";
_.parsers[10].compatible = [];
_.parsers[10].compatible[0] = "linux";
_.parsers[10].compatible[1] = "darwin";
_.parsers[10].compatible[2] = "cygwin";
_.parsers[10].compatible[3] = "win32";
_.parsers[10].compatible[4] = "aix";
_.parsers[10].compatible[5] = "freebsd";
_.parsers[10].magic_commands = [];
_.parsers[10].magic_commands[0] = "env";
_.parsers[11] = {};
_.parsers[11].name = "file";
_.parsers[11].argument = "--file";
_.parsers[11].version = "1.1";
_.parsers[11].description = "file command parser";
_.parsers[11].author = "Kelly Brazil";
_.parsers[11].author_email = "kellyjonbrazil@gmail.com";
_.parsers[11].compatible = [];
_.parsers[11].compatible[0] = "linux";
_.parsers[11].compatible[1] = "aix";
_.parsers[11].compatible[2] = "freebsd";
_.parsers[11].compatible[3] = "darwin";
_.parsers[11].magic_commands = [];
_.parsers[11].magic_commands[0] = "file";
_.parsers[12] = {};
_.parsers[12].name = "free";
_.parsers[12].argument = "--free";
_.parsers[12].version = "1.0";
_.parsers[12].description = "free command parser";
_.parsers[12].author = "Kelly Brazil";
_.parsers[12].author_email = "kellyjonbrazil@gmail.com";
_.parsers[12].compatible = [];
_.parsers[12].compatible[0] = "linux";
_.parsers[12].magic_commands = [];
_.parsers[12].magic_commands[0] = "free";
_.parsers[13] = {};
_.parsers[13].name = "fstab";
_.parsers[13].argument = "--fstab";
_.parsers[13].version = "1.0";
_.parsers[13].description = "fstab file parser";
_.parsers[13].author = "Kelly Brazil";
_.parsers[13].author_email = "kellyjonbrazil@gmail.com";
_.parsers[13].compatible = [];
_.parsers[13].compatible[0] = "linux";
_.parsers[14] = {};
_.parsers[14].name = "group";
_.parsers[14].argument = "--group";
_.parsers[14].version = "1.0";
_.parsers[14].description = "/etc/group file parser";
_.parsers[14].author = "Kelly Brazil";
_.parsers[14].author_email = "kellyjonbrazil@gmail.com";
_.parsers[14].compatible = [];
_.parsers[14].compatible[0] = "linux";
_.parsers[14].compatible[1] = "darwin";
_.parsers[14].compatible[2] = "aix";
_.parsers[14].compatible[3] = "freebsd";
_.parsers[15] = {};
_.parsers[15].name = "gshadow";
_.parsers[15].argument = "--gshadow";
_.parsers[15].version = "1.0";
_.parsers[15].description = "/etc/gshadow file parser";
_.parsers[15].author = "Kelly Brazil";
_.parsers[15].author_email = "kellyjonbrazil@gmail.com";
_.parsers[15].compatible = [];
_.parsers[15].compatible[0] = "linux";
_.parsers[15].compatible[1] = "aix";
_.parsers[15].compatible[2] = "freebsd";
_.parsers[16] = {};
_.parsers[16].name = "history";
_.parsers[16].argument = "--history";
_.parsers[16].version = "1.2";
_.parsers[16].description = "history command parser";
_.parsers[16].author = "Kelly Brazil";
_.parsers[16].author_email = "kellyjonbrazil@gmail.com";
_.parsers[16].details = "Optimizations by https://github.com/philippeitis";
_.parsers[16].compatible = [];
_.parsers[16].compatible[0] = "linux";
_.parsers[16].compatible[1] = "darwin";
_.parsers[16].compatible[2] = "cygwin";
_.parsers[16].compatible[3] = "aix";
_.parsers[16].compatible[4] = "freebsd";
_.parsers[17] = {};
_.parsers[17].name = "hosts";
_.parsers[17].argument = "--hosts";
_.parsers[17].version = "1.0";
_.parsers[17].description = "/etc/hosts file parser";
_.parsers[17].author = "Kelly Brazil";
_.parsers[17].author_email = "kellyjonbrazil@gmail.com";
_.parsers[17].compatible = [];
_.parsers[17].compatible[0] = "linux";
_.parsers[17].compatible[1] = "darwin";
_.parsers[17].compatible[2] = "cygwin";
_.parsers[17].compatible[3] = "win32";
_.parsers[17].compatible[4] = "aix";
_.parsers[17].compatible[5] = "freebsd";
_.parsers[18] = {};
_.parsers[18].name = "id";
_.parsers[18].argument = "--id";
_.parsers[18].version = "1.0";
_.parsers[18].description = "id command parser";
_.parsers[18].author = "Kelly Brazil";
_.parsers[18].author_email = "kellyjonbrazil@gmail.com";
_.parsers[18].compatible = [];
_.parsers[18].compatible[0] = "linux";
_.parsers[18].compatible[1] = "darwin";
_.parsers[18].compatible[2] = "aix";
_.parsers[18].compatible[3] = "freebsd";
_.parsers[18].magic_commands = [];
_.parsers[18].magic_commands[0] = "id";
_.parsers[19] = {};
_.parsers[19].name = "ifconfig";
_.parsers[19].argument = "--ifconfig";
_.parsers[19].version = "1.5";
_.parsers[19].description = "ifconfig command parser";
_.parsers[19].author = "Kelly Brazil";
_.parsers[19].author_email = "kellyjonbrazil@gmail.com";
_.parsers[19].details = "Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser";
_.parsers[19].compatible = [];
_.parsers[19].compatible[0] = "linux";
_.parsers[19].compatible[1] = "aix";
_.parsers[19].compatible[2] = "freebsd";
_.parsers[19].compatible[3] = "darwin";
_.parsers[19].magic_commands = [];
_.parsers[19].magic_commands[0] = "ifconfig";
_.parsers[20] = {};
_.parsers[20].name = "ini";
_.parsers[20].argument = "--ini";
_.parsers[20].version = "1.0";
_.parsers[20].description = "INI file parser";
_.parsers[20].author = "Kelly Brazil";
_.parsers[20].author_email = "kellyjonbrazil@gmail.com";
_.parsers[20].details = "Using configparser from the standard library";
_.parsers[20].compatible = [];
_.parsers[20].compatible[0] = "linux";
_.parsers[20].compatible[1] = "darwin";
_.parsers[20].compatible[2] = "cygwin";
_.parsers[20].compatible[3] = "win32";
_.parsers[20].compatible[4] = "aix";
_.parsers[20].compatible[5] = "freebsd";
_.parsers[21] = {};
_.parsers[21].name = "iptables";
_.parsers[21].argument = "--iptables";
_.parsers[21].version = "1.1";
_.parsers[21].description = "iptables command parser";
_.parsers[21].author = "Kelly Brazil";
_.parsers[21].author_email = "kellyjonbrazil@gmail.com";
_.parsers[21].compatible = [];
_.parsers[21].compatible[0] = "linux";
_.parsers[21].magic_commands = [];
_.parsers[21].magic_commands[0] = "iptables";
_.parsers[22] = {};
_.parsers[22].name = "jobs";
_.parsers[22].argument = "--jobs";
_.parsers[22].version = "1.0";
_.parsers[22].description = "jobs command parser";
_.parsers[22].author = "Kelly Brazil";
_.parsers[22].author_email = "kellyjonbrazil@gmail.com";
_.parsers[22].compatible = [];
_.parsers[22].compatible[0] = "linux";
_.parsers[22].compatible[1] = "darwin";
_.parsers[22].compatible[2] = "cygwin";
_.parsers[22].compatible[3] = "aix";
_.parsers[22].compatible[4] = "freebsd";
_.parsers[22].magic_commands = [];
_.parsers[22].magic_commands[0] = "jobs";
_.parsers[23] = {};
_.parsers[23].name = "last";
_.parsers[23].argument = "--last";
_.parsers[23].version = "1.0";
_.parsers[23].description = "last and lastb command parser";
_.parsers[23].author = "Kelly Brazil";
_.parsers[23].author_email = "kellyjonbrazil@gmail.com";
_.parsers[23].compatible = [];
_.parsers[23].compatible[0] = "linux";
_.parsers[23].compatible[1] = "darwin";
_.parsers[23].compatible[2] = "aix";
_.parsers[23].compatible[3] = "freebsd";
_.parsers[23].magic_commands = [];
_.parsers[23].magic_commands[0] = "last";
_.parsers[23].magic_commands[1] = "lastb";
_.parsers[24] = {};
_.parsers[24].name = "ls";
_.parsers[24].argument = "--ls";
_.parsers[24].version = "1.3";
_.parsers[24].description = "ls command parser";
_.parsers[24].author = "Kelly Brazil";
_.parsers[24].author_email = "kellyjonbrazil@gmail.com";
_.parsers[24].compatible = [];
_.parsers[24].compatible[0] = "linux";
_.parsers[24].compatible[1] = "darwin";
_.parsers[24].compatible[2] = "cygwin";
_.parsers[24].compatible[3] = "aix";
_.parsers[24].compatible[4] = "freebsd";
_.parsers[24].magic_commands = [];
_.parsers[24].magic_commands[0] = "ls";
_.parsers[25] = {};
_.parsers[25].name = "lsblk";
_.parsers[25].argument = "--lsblk";
_.parsers[25].version = "1.3";
_.parsers[25].description = "lsblk command parser";
_.parsers[25].author = "Kelly Brazil";
_.parsers[25].author_email = "kellyjonbrazil@gmail.com";
_.parsers[25].compatible = [];
_.parsers[25].compatible[0] = "linux";
_.parsers[25].magic_commands = [];
_.parsers[25].magic_commands[0] = "lsblk";
_.parsers[26] = {};
_.parsers[26].name = "lsmod";
_.parsers[26].argument = "--lsmod";
_.parsers[26].version = "1.1";
_.parsers[26].description = "lsmod command parser";
_.parsers[26].author = "Kelly Brazil";
_.parsers[26].author_email = "kellyjonbrazil@gmail.com";
_.parsers[26].compatible = [];
_.parsers[26].compatible[0] = "linux";
_.parsers[26].magic_commands = [];
_.parsers[26].magic_commands[0] = "lsmod";
_.parsers[27] = {};
_.parsers[27].name = "lsof";
_.parsers[27].argument = "--lsof";
_.parsers[27].version = "1.0";
_.parsers[27].description = "lsof command parser";
_.parsers[27].author = "Kelly Brazil";
_.parsers[27].author_email = "kellyjonbrazil@gmail.com";
_.parsers[27].compatible = [];
_.parsers[27].compatible[0] = "linux";
_.parsers[27].magic_commands = [];
_.parsers[27].magic_commands[0] = "lsof";
_.parsers[28] = {};
_.parsers[28].name = "mount";
_.parsers[28].argument = "--mount";
_.parsers[28].version = "1.1";
_.parsers[28].description = "mount command parser";
_.parsers[28].author = "Kelly Brazil";
_.parsers[28].author_email = "kellyjonbrazil@gmail.com";
_.parsers[28].compatible = [];
_.parsers[28].compatible[0] = "linux";
_.parsers[28].compatible[1] = "darwin";
_.parsers[28].magic_commands = [];
_.parsers[28].magic_commands[0] = "mount";
_.parsers[29] = {};
_.parsers[29].name = "netstat";
_.parsers[29].argument = "--netstat";
_.parsers[29].version = "1.2";
_.parsers[29].description = "netstat command parser";
_.parsers[29].author = "Kelly Brazil";
_.parsers[29].author_email = "kellyjonbrazil@gmail.com";
_.parsers[29].compatible = [];
_.parsers[29].compatible[0] = "linux";
_.parsers[29].magic_commands = [];
_.parsers[29].magic_commands[0] = "netstat";
_.parsers[30] = {};
_.parsers[30].name = "ntpq";
_.parsers[30].argument = "--ntpq";
_.parsers[30].version = "1.0";
_.parsers[30].description = "ntpq -p command parser";
_.parsers[30].author = "Kelly Brazil";
_.parsers[30].author_email = "kellyjonbrazil@gmail.com";
_.parsers[30].compatible = [];
_.parsers[30].compatible[0] = "linux";
_.parsers[30].magic_commands = [];
_.parsers[30].magic_commands[0] = "ntpq";
_.parsers[31] = {};
_.parsers[31].name = "passwd";
_.parsers[31].argument = "--passwd";
_.parsers[31].version = "1.0";
_.parsers[31].description = "/etc/passwd file parser";
_.parsers[31].author = "Kelly Brazil";
_.parsers[31].author_email = "kellyjonbrazil@gmail.com";
_.parsers[31].compatible = [];
_.parsers[31].compatible[0] = "linux";
_.parsers[31].compatible[1] = "darwin";
_.parsers[31].compatible[2] = "aix";
_.parsers[31].compatible[3] = "freebsd";
_.parsers[32] = {};
_.parsers[32].name = "pip_list";
_.parsers[32].argument = "--pip-list";
_.parsers[32].version = "1.0";
_.parsers[32].description = "pip list command parser";
_.parsers[32].author = "Kelly Brazil";
_.parsers[32].author_email = "kellyjonbrazil@gmail.com";
_.parsers[32].compatible = [];
_.parsers[32].compatible[0] = "linux";
_.parsers[32].compatible[1] = "darwin";
_.parsers[32].compatible[2] = "cygwin";
_.parsers[32].compatible[3] = "win32";
_.parsers[32].compatible[4] = "aix";
_.parsers[32].compatible[5] = "freebsd";
_.parsers[32].magic_commands = [];
_.parsers[32].magic_commands[0] = "pip list";
_.parsers[32].magic_commands[1] = "pip3 list";
_.parsers[33] = {};
_.parsers[33].name = "pip_show";
_.parsers[33].argument = "--pip-show";
_.parsers[33].version = "1.0";
_.parsers[33].description = "pip show command parser";
_.parsers[33].author = "Kelly Brazil";
_.parsers[33].author_email = "kellyjonbrazil@gmail.com";
_.parsers[33].compatible = [];
_.parsers[33].compatible[0] = "linux";
_.parsers[33].compatible[1] = "darwin";
_.parsers[33].compatible[2] = "cygwin";
_.parsers[33].compatible[3] = "win32";
_.parsers[33].compatible[4] = "aix";
_.parsers[33].compatible[5] = "freebsd";
_.parsers[33].magic_commands = [];
_.parsers[33].magic_commands[0] = "pip show";
_.parsers[33].magic_commands[1] = "pip3 show";
_.parsers[34] = {};
_.parsers[34].name = "ps";
_.parsers[34].argument = "--ps";
_.parsers[34].version = "1.1";
_.parsers[34].description = "ps command parser";
_.parsers[34].author = "Kelly Brazil";
_.parsers[34].author_email = "kellyjonbrazil@gmail.com";
_.parsers[34].compatible = [];
_.parsers[34].compatible[0] = "linux";
_.parsers[34].compatible[1] = "darwin";
_.parsers[34].compatible[2] = "cygwin";
_.parsers[34].compatible[3] = "aix";
_.parsers[34].compatible[4] = "freebsd";
_.parsers[34].magic_commands = [];
_.parsers[34].magic_commands[0] = "ps";
_.parsers[35] = {};
_.parsers[35].name = "route";
_.parsers[35].argument = "--route";
_.parsers[35].version = "1.0";
_.parsers[35].description = "route command parser";
_.parsers[35].author = "Kelly Brazil";
_.parsers[35].author_email = "kellyjonbrazil@gmail.com";
_.parsers[35].compatible = [];
_.parsers[35].compatible[0] = "linux";
_.parsers[35].magic_commands = [];
_.parsers[35].magic_commands[0] = "route";
_.parsers[36] = {};
_.parsers[36].name = "shadow";
_.parsers[36].argument = "--shadow";
_.parsers[36].version = "1.0";
_.parsers[36].description = "/etc/shadow file parser";
_.parsers[36].author = "Kelly Brazil";
_.parsers[36].author_email = "kellyjonbrazil@gmail.com";
_.parsers[36].compatible = [];
_.parsers[36].compatible[0] = "linux";
_.parsers[36].compatible[1] = "darwin";
_.parsers[36].compatible[2] = "aix";
_.parsers[36].compatible[3] = "freebsd";
_.parsers[37] = {};
_.parsers[37].name = "ss";
_.parsers[37].argument = "--ss";
_.parsers[37].version = "1.0";
_.parsers[37].description = "ss command parser";
_.parsers[37].author = "Kelly Brazil";
_.parsers[37].author_email = "kellyjonbrazil@gmail.com";
_.parsers[37].compatible = [];
_.parsers[37].compatible[0] = "linux";
_.parsers[37].magic_commands = [];
_.parsers[37].magic_commands[0] = "ss";
_.parsers[38] = {};
_.parsers[38].name = "stat";
_.parsers[38].argument = "--stat";
_.parsers[38].version = "1.0";
_.parsers[38].description = "stat command parser";
_.parsers[38].author = "Kelly Brazil";
_.parsers[38].author_email = "kellyjonbrazil@gmail.com";
_.parsers[38].compatible = [];
_.parsers[38].compatible[0] = "linux";
_.parsers[38].magic_commands = [];
_.parsers[38].magic_commands[0] = "stat";
_.parsers[39] = {};
_.parsers[39].name = "systemctl";
_.parsers[39].argument = "--systemctl";
_.parsers[39].version = "1.0";
_.parsers[39].description = "systemctl command parser";
_.parsers[39].author = "Kelly Brazil";
_.parsers[39].author_email = "kellyjonbrazil@gmail.com";
_.parsers[39].compatible = [];
_.parsers[39].compatible[0] = "linux";
_.parsers[39].magic_commands = [];
_.parsers[39].magic_commands[0] = "systemctl";
_.parsers[40] = {};
_.parsers[40].name = "systemctl_lj";
_.parsers[40].argument = "--systemctl-lj";
_.parsers[40].version = "1.0";
_.parsers[40].description = "systemctl list-jobs command parser";
_.parsers[40].author = "Kelly Brazil";
_.parsers[40].author_email = "kellyjonbrazil@gmail.com";
_.parsers[40].compatible = [];
_.parsers[40].compatible[0] = "linux";
_.parsers[40].magic_commands = [];
_.parsers[40].magic_commands[0] = "systemctl list-jobs";
_.parsers[41] = {};
_.parsers[41].name = "systemctl_ls";
_.parsers[41].argument = "--systemctl-ls";
_.parsers[41].version = "1.0";
_.parsers[41].description = "systemctl list-sockets command parser";
_.parsers[41].author = "Kelly Brazil";
_.parsers[41].author_email = "kellyjonbrazil@gmail.com";
_.parsers[41].compatible = [];
_.parsers[41].compatible[0] = "linux";
_.parsers[41].magic_commands = [];
_.parsers[41].magic_commands[0] = "systemctl list-sockets";
_.parsers[42] = {};
_.parsers[42].name = "systemctl_luf";
_.parsers[42].argument = "--systemctl-luf";
_.parsers[42].version = "1.0";
_.parsers[42].description = "systemctl list-unit-files command parser";
_.parsers[42].author = "Kelly Brazil";
_.parsers[42].author_email = "kellyjonbrazil@gmail.com";
_.parsers[42].compatible = [];
_.parsers[42].compatible[0] = "linux";
_.parsers[42].magic_commands = [];
_.parsers[42].magic_commands[0] = "systemctl list-unit-files";
_.parsers[43] = {};
_.parsers[43].name = "timedatectl";
_.parsers[43].argument = "--timedatectl";
_.parsers[43].version = "1.0";
_.parsers[43].description = "timedatectl status command parser";
_.parsers[43].author = "Kelly Brazil";
_.parsers[43].author_email = "kellyjonbrazil@gmail.com";
_.parsers[43].compatible = [];
_.parsers[43].compatible[0] = "linux";
_.parsers[43].magic_commands = [];
_.parsers[43].magic_commands[0] = "timedatectl";
_.parsers[43].magic_commands[1] = "timedatectl status";
_.parsers[44] = {};
_.parsers[44].name = "uname";
_.parsers[44].argument = "--uname";
_.parsers[44].version = "1.1";
_.parsers[44].description = "uname -a command parser";
_.parsers[44].author = "Kelly Brazil";
_.parsers[44].author_email = "kellyjonbrazil@gmail.com";
_.parsers[44].compatible = [];
_.parsers[44].compatible[0] = "linux";
_.parsers[44].compatible[1] = "darwin";
_.parsers[44].magic_commands = [];
_.parsers[44].magic_commands[0] = "uname";
_.parsers[45] = {};
_.parsers[45].name = "uptime";
_.parsers[45].argument = "--uptime";
_.parsers[45].version = "1.0";
_.parsers[45].description = "uptime command parser";
_.parsers[45].author = "Kelly Brazil";
_.parsers[45].author_email = "kellyjonbrazil@gmail.com";
_.parsers[45].compatible = [];
_.parsers[45].compatible[0] = "linux";
_.parsers[45].compatible[1] = "darwin";
_.parsers[45].compatible[2] = "cygwin";
_.parsers[45].compatible[3] = "aix";
_.parsers[45].compatible[4] = "freebsd";
_.parsers[45].magic_commands = [];
_.parsers[45].magic_commands[0] = "uptime";
_.parsers[46] = {};
_.parsers[46].name = "w";
_.parsers[46].argument = "--w";
_.parsers[46].version = "1.0";
_.parsers[46].description = "w command parser";
_.parsers[46].author = "Kelly Brazil";
_.parsers[46].author_email = "kellyjonbrazil@gmail.com";
_.parsers[46].compatible = [];
_.parsers[46].compatible[0] = "linux";
_.parsers[46].compatible[1] = "darwin";
_.parsers[46].compatible[2] = "cygwin";
_.parsers[46].compatible[3] = "aix";
_.parsers[46].compatible[4] = "freebsd";
_.parsers[46].magic_commands = [];
_.parsers[46].magic_commands[0] = "w";
_.parsers[47] = {};
_.parsers[47].name = "who";
_.parsers[47].argument = "--who";
_.parsers[47].version = "1.0";
_.parsers[47].description = "who command parser";
_.parsers[47].author = "Kelly Brazil";
_.parsers[47].author_email = "kellyjonbrazil@gmail.com";
_.parsers[47].compatible = [];
_.parsers[47].compatible[0] = "linux";
_.parsers[47].compatible[1] = "darwin";
_.parsers[47].compatible[2] = "cygwin";
_.parsers[47].compatible[3] = "aix";
_.parsers[47].compatible[4] = "freebsd";
_.parsers[47].magic_commands = [];
_.parsers[47].magic_commands[0] = "who";
_.parsers[48] = {};
_.parsers[48].name = "xml";
_.parsers[48].argument = "--xml";
_.parsers[48].version = "1.0";
_.parsers[48].description = "XML file parser";
_.parsers[48].author = "Kelly Brazil";
_.parsers[48].author_email = "kellyjonbrazil@gmail.com";
_.parsers[48].details = "Using the xmltodict library at https://github.com/martinblech/xmltodict";
_.parsers[48].compatible = [];
_.parsers[48].compatible[0] = "linux";
_.parsers[48].compatible[1] = "darwin";
_.parsers[48].compatible[2] = "cygwin";
_.parsers[48].compatible[3] = "win32";
_.parsers[48].compatible[4] = "aix";
_.parsers[48].compatible[5] = "freebsd";
_.parsers[49] = {};
_.parsers[49].name = "yaml";
_.parsers[49].argument = "--yaml";
_.parsers[49].version = "1.0";
_.parsers[49].description = "YAML file parser";
_.parsers[49].author = "Kelly Brazil";
_.parsers[49].author_email = "kellyjonbrazil@gmail.com";
_.parsers[49].details = "Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml";
_.parsers[49].compatible = [];
_.parsers[49].compatible[0] = "linux";
_.parsers[49].compatible[1] = "darwin";
_.parsers[49].compatible[2] = "cygwin";
_.parsers[49].compatible[3] = "win32";
_.parsers[49].compatible[4] = "aix";
_.parsers[49].compatible[5] = "freebsd";
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-s']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_parsers(self):
        """
        Test jc -a | jello '_["parsers"]'
        """
        expected = '''\
[
  {
    "name": "airport",
    "argument": "--airport",
    "version": "1.0",
    "description": "airport -I command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "darwin"
    ],
    "magic_commands": [
      "airport -I"
    ]
  },
  {
    "name": "airport_s",
    "argument": "--airport-s",
    "version": "1.0",
    "description": "airport -s command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "darwin"
    ],
    "magic_commands": [
      "airport -s"
    ]
  },
  {
    "name": "arp",
    "argument": "--arp",
    "version": "1.2",
    "description": "arp command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "aix",
      "freebsd",
      "darwin"
    ],
    "magic_commands": [
      "arp"
    ]
  },
  {
    "name": "blkid",
    "argument": "--blkid",
    "version": "1.0",
    "description": "blkid command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "blkid"
    ]
  },
  {
    "name": "crontab",
    "argument": "--crontab",
    "version": "1.1",
    "description": "crontab command and file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "crontab"
    ]
  },
  {
    "name": "crontab_u",
    "argument": "--crontab-u",
    "version": "1.0",
    "description": "crontab file parser with user support",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "csv",
    "argument": "--csv",
    "version": "1.0",
    "description": "CSV file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "details": "Using the python standard csv library",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "df",
    "argument": "--df",
    "version": "1.1",
    "description": "df command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin"
    ],
    "magic_commands": [
      "df"
    ]
  },
  {
    "name": "dig",
    "argument": "--dig",
    "version": "1.1",
    "description": "dig command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "aix",
      "freebsd",
      "darwin"
    ],
    "magic_commands": [
      "dig"
    ]
  },
  {
    "name": "du",
    "argument": "--du",
    "version": "1.1",
    "description": "du command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "du"
    ]
  },
  {
    "name": "env",
    "argument": "--env",
    "version": "1.1",
    "description": "env command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "env"
    ]
  },
  {
    "name": "file",
    "argument": "--file",
    "version": "1.1",
    "description": "file command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "aix",
      "freebsd",
      "darwin"
    ],
    "magic_commands": [
      "file"
    ]
  },
  {
    "name": "free",
    "argument": "--free",
    "version": "1.0",
    "description": "free command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "free"
    ]
  },
  {
    "name": "fstab",
    "argument": "--fstab",
    "version": "1.0",
    "description": "fstab file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ]
  },
  {
    "name": "group",
    "argument": "--group",
    "version": "1.0",
    "description": "/etc/group file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "gshadow",
    "argument": "--gshadow",
    "version": "1.0",
    "description": "/etc/gshadow file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "history",
    "argument": "--history",
    "version": "1.2",
    "description": "history command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "details": "Optimizations by https://github.com/philippeitis",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "hosts",
    "argument": "--hosts",
    "version": "1.0",
    "description": "/etc/hosts file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "id",
    "argument": "--id",
    "version": "1.0",
    "description": "id command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "id"
    ]
  },
  {
    "name": "ifconfig",
    "argument": "--ifconfig",
    "version": "1.5",
    "description": "ifconfig command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "details": "Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser",
    "compatible": [
      "linux",
      "aix",
      "freebsd",
      "darwin"
    ],
    "magic_commands": [
      "ifconfig"
    ]
  },
  {
    "name": "ini",
    "argument": "--ini",
    "version": "1.0",
    "description": "INI file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "details": "Using configparser from the standard library",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "iptables",
    "argument": "--iptables",
    "version": "1.1",
    "description": "iptables command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "iptables"
    ]
  },
  {
    "name": "jobs",
    "argument": "--jobs",
    "version": "1.0",
    "description": "jobs command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "jobs"
    ]
  },
  {
    "name": "last",
    "argument": "--last",
    "version": "1.0",
    "description": "last and lastb command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "last",
      "lastb"
    ]
  },
  {
    "name": "ls",
    "argument": "--ls",
    "version": "1.3",
    "description": "ls command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "ls"
    ]
  },
  {
    "name": "lsblk",
    "argument": "--lsblk",
    "version": "1.3",
    "description": "lsblk command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "lsblk"
    ]
  },
  {
    "name": "lsmod",
    "argument": "--lsmod",
    "version": "1.1",
    "description": "lsmod command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "lsmod"
    ]
  },
  {
    "name": "lsof",
    "argument": "--lsof",
    "version": "1.0",
    "description": "lsof command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "lsof"
    ]
  },
  {
    "name": "mount",
    "argument": "--mount",
    "version": "1.1",
    "description": "mount command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin"
    ],
    "magic_commands": [
      "mount"
    ]
  },
  {
    "name": "netstat",
    "argument": "--netstat",
    "version": "1.2",
    "description": "netstat command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "netstat"
    ]
  },
  {
    "name": "ntpq",
    "argument": "--ntpq",
    "version": "1.0",
    "description": "ntpq -p command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "ntpq"
    ]
  },
  {
    "name": "passwd",
    "argument": "--passwd",
    "version": "1.0",
    "description": "/etc/passwd file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "pip_list",
    "argument": "--pip-list",
    "version": "1.0",
    "description": "pip list command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "pip list",
      "pip3 list"
    ]
  },
  {
    "name": "pip_show",
    "argument": "--pip-show",
    "version": "1.0",
    "description": "pip show command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "pip show",
      "pip3 show"
    ]
  },
  {
    "name": "ps",
    "argument": "--ps",
    "version": "1.1",
    "description": "ps command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "ps"
    ]
  },
  {
    "name": "route",
    "argument": "--route",
    "version": "1.0",
    "description": "route command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "route"
    ]
  },
  {
    "name": "shadow",
    "argument": "--shadow",
    "version": "1.0",
    "description": "/etc/shadow file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "ss",
    "argument": "--ss",
    "version": "1.0",
    "description": "ss command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "ss"
    ]
  },
  {
    "name": "stat",
    "argument": "--stat",
    "version": "1.0",
    "description": "stat command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "stat"
    ]
  },
  {
    "name": "systemctl",
    "argument": "--systemctl",
    "version": "1.0",
    "description": "systemctl command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "systemctl"
    ]
  },
  {
    "name": "systemctl_lj",
    "argument": "--systemctl-lj",
    "version": "1.0",
    "description": "systemctl list-jobs command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "systemctl list-jobs"
    ]
  },
  {
    "name": "systemctl_ls",
    "argument": "--systemctl-ls",
    "version": "1.0",
    "description": "systemctl list-sockets command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "systemctl list-sockets"
    ]
  },
  {
    "name": "systemctl_luf",
    "argument": "--systemctl-luf",
    "version": "1.0",
    "description": "systemctl list-unit-files command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "systemctl list-unit-files"
    ]
  },
  {
    "name": "timedatectl",
    "argument": "--timedatectl",
    "version": "1.0",
    "description": "timedatectl status command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux"
    ],
    "magic_commands": [
      "timedatectl",
      "timedatectl status"
    ]
  },
  {
    "name": "uname",
    "argument": "--uname",
    "version": "1.1",
    "description": "uname -a command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin"
    ],
    "magic_commands": [
      "uname"
    ]
  },
  {
    "name": "uptime",
    "argument": "--uptime",
    "version": "1.0",
    "description": "uptime command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "uptime"
    ]
  },
  {
    "name": "w",
    "argument": "--w",
    "version": "1.0",
    "description": "w command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "w"
    ]
  },
  {
    "name": "who",
    "argument": "--who",
    "version": "1.0",
    "description": "who command parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "aix",
      "freebsd"
    ],
    "magic_commands": [
      "who"
    ]
  },
  {
    "name": "xml",
    "argument": "--xml",
    "version": "1.0",
    "description": "XML file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "details": "Using the xmltodict library at https://github.com/martinblech/xmltodict",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ]
  },
  {
    "name": "yaml",
    "argument": "--yaml",
    "version": "1.0",
    "description": "YAML file parser",
    "author": "Kelly Brazil",
    "author_email": "kellyjonbrazil@gmail.com",
    "details": "Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml",
    "compatible": [
      "linux",
      "darwin",
      "cygwin",
      "win32",
      "aix",
      "freebsd"
    ]
  }
]
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_["parsers"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_s_parsers_dot(self):
        """
        Test jc -a | jello -s '_.parsers'
        """
        expected = '''\
_ = [];
_[0] = {};
_[0].name = "airport";
_[0].argument = "--airport";
_[0].version = "1.0";
_[0].description = "airport -I command parser";
_[0].author = "Kelly Brazil";
_[0].author_email = "kellyjonbrazil@gmail.com";
_[0].compatible = [];
_[0].compatible[0] = "darwin";
_[0].magic_commands = [];
_[0].magic_commands[0] = "airport -I";
_[1] = {};
_[1].name = "airport_s";
_[1].argument = "--airport-s";
_[1].version = "1.0";
_[1].description = "airport -s command parser";
_[1].author = "Kelly Brazil";
_[1].author_email = "kellyjonbrazil@gmail.com";
_[1].compatible = [];
_[1].compatible[0] = "darwin";
_[1].magic_commands = [];
_[1].magic_commands[0] = "airport -s";
_[2] = {};
_[2].name = "arp";
_[2].argument = "--arp";
_[2].version = "1.2";
_[2].description = "arp command parser";
_[2].author = "Kelly Brazil";
_[2].author_email = "kellyjonbrazil@gmail.com";
_[2].compatible = [];
_[2].compatible[0] = "linux";
_[2].compatible[1] = "aix";
_[2].compatible[2] = "freebsd";
_[2].compatible[3] = "darwin";
_[2].magic_commands = [];
_[2].magic_commands[0] = "arp";
_[3] = {};
_[3].name = "blkid";
_[3].argument = "--blkid";
_[3].version = "1.0";
_[3].description = "blkid command parser";
_[3].author = "Kelly Brazil";
_[3].author_email = "kellyjonbrazil@gmail.com";
_[3].compatible = [];
_[3].compatible[0] = "linux";
_[3].magic_commands = [];
_[3].magic_commands[0] = "blkid";
_[4] = {};
_[4].name = "crontab";
_[4].argument = "--crontab";
_[4].version = "1.1";
_[4].description = "crontab command and file parser";
_[4].author = "Kelly Brazil";
_[4].author_email = "kellyjonbrazil@gmail.com";
_[4].compatible = [];
_[4].compatible[0] = "linux";
_[4].compatible[1] = "darwin";
_[4].compatible[2] = "aix";
_[4].compatible[3] = "freebsd";
_[4].magic_commands = [];
_[4].magic_commands[0] = "crontab";
_[5] = {};
_[5].name = "crontab_u";
_[5].argument = "--crontab-u";
_[5].version = "1.0";
_[5].description = "crontab file parser with user support";
_[5].author = "Kelly Brazil";
_[5].author_email = "kellyjonbrazil@gmail.com";
_[5].compatible = [];
_[5].compatible[0] = "linux";
_[5].compatible[1] = "darwin";
_[5].compatible[2] = "aix";
_[5].compatible[3] = "freebsd";
_[6] = {};
_[6].name = "csv";
_[6].argument = "--csv";
_[6].version = "1.0";
_[6].description = "CSV file parser";
_[6].author = "Kelly Brazil";
_[6].author_email = "kellyjonbrazil@gmail.com";
_[6].details = "Using the python standard csv library";
_[6].compatible = [];
_[6].compatible[0] = "linux";
_[6].compatible[1] = "darwin";
_[6].compatible[2] = "cygwin";
_[6].compatible[3] = "win32";
_[6].compatible[4] = "aix";
_[6].compatible[5] = "freebsd";
_[7] = {};
_[7].name = "df";
_[7].argument = "--df";
_[7].version = "1.1";
_[7].description = "df command parser";
_[7].author = "Kelly Brazil";
_[7].author_email = "kellyjonbrazil@gmail.com";
_[7].compatible = [];
_[7].compatible[0] = "linux";
_[7].compatible[1] = "darwin";
_[7].magic_commands = [];
_[7].magic_commands[0] = "df";
_[8] = {};
_[8].name = "dig";
_[8].argument = "--dig";
_[8].version = "1.1";
_[8].description = "dig command parser";
_[8].author = "Kelly Brazil";
_[8].author_email = "kellyjonbrazil@gmail.com";
_[8].compatible = [];
_[8].compatible[0] = "linux";
_[8].compatible[1] = "aix";
_[8].compatible[2] = "freebsd";
_[8].compatible[3] = "darwin";
_[8].magic_commands = [];
_[8].magic_commands[0] = "dig";
_[9] = {};
_[9].name = "du";
_[9].argument = "--du";
_[9].version = "1.1";
_[9].description = "du command parser";
_[9].author = "Kelly Brazil";
_[9].author_email = "kellyjonbrazil@gmail.com";
_[9].compatible = [];
_[9].compatible[0] = "linux";
_[9].compatible[1] = "darwin";
_[9].compatible[2] = "aix";
_[9].compatible[3] = "freebsd";
_[9].magic_commands = [];
_[9].magic_commands[0] = "du";
_[10] = {};
_[10].name = "env";
_[10].argument = "--env";
_[10].version = "1.1";
_[10].description = "env command parser";
_[10].author = "Kelly Brazil";
_[10].author_email = "kellyjonbrazil@gmail.com";
_[10].compatible = [];
_[10].compatible[0] = "linux";
_[10].compatible[1] = "darwin";
_[10].compatible[2] = "cygwin";
_[10].compatible[3] = "win32";
_[10].compatible[4] = "aix";
_[10].compatible[5] = "freebsd";
_[10].magic_commands = [];
_[10].magic_commands[0] = "env";
_[11] = {};
_[11].name = "file";
_[11].argument = "--file";
_[11].version = "1.1";
_[11].description = "file command parser";
_[11].author = "Kelly Brazil";
_[11].author_email = "kellyjonbrazil@gmail.com";
_[11].compatible = [];
_[11].compatible[0] = "linux";
_[11].compatible[1] = "aix";
_[11].compatible[2] = "freebsd";
_[11].compatible[3] = "darwin";
_[11].magic_commands = [];
_[11].magic_commands[0] = "file";
_[12] = {};
_[12].name = "free";
_[12].argument = "--free";
_[12].version = "1.0";
_[12].description = "free command parser";
_[12].author = "Kelly Brazil";
_[12].author_email = "kellyjonbrazil@gmail.com";
_[12].compatible = [];
_[12].compatible[0] = "linux";
_[12].magic_commands = [];
_[12].magic_commands[0] = "free";
_[13] = {};
_[13].name = "fstab";
_[13].argument = "--fstab";
_[13].version = "1.0";
_[13].description = "fstab file parser";
_[13].author = "Kelly Brazil";
_[13].author_email = "kellyjonbrazil@gmail.com";
_[13].compatible = [];
_[13].compatible[0] = "linux";
_[14] = {};
_[14].name = "group";
_[14].argument = "--group";
_[14].version = "1.0";
_[14].description = "/etc/group file parser";
_[14].author = "Kelly Brazil";
_[14].author_email = "kellyjonbrazil@gmail.com";
_[14].compatible = [];
_[14].compatible[0] = "linux";
_[14].compatible[1] = "darwin";
_[14].compatible[2] = "aix";
_[14].compatible[3] = "freebsd";
_[15] = {};
_[15].name = "gshadow";
_[15].argument = "--gshadow";
_[15].version = "1.0";
_[15].description = "/etc/gshadow file parser";
_[15].author = "Kelly Brazil";
_[15].author_email = "kellyjonbrazil@gmail.com";
_[15].compatible = [];
_[15].compatible[0] = "linux";
_[15].compatible[1] = "aix";
_[15].compatible[2] = "freebsd";
_[16] = {};
_[16].name = "history";
_[16].argument = "--history";
_[16].version = "1.2";
_[16].description = "history command parser";
_[16].author = "Kelly Brazil";
_[16].author_email = "kellyjonbrazil@gmail.com";
_[16].details = "Optimizations by https://github.com/philippeitis";
_[16].compatible = [];
_[16].compatible[0] = "linux";
_[16].compatible[1] = "darwin";
_[16].compatible[2] = "cygwin";
_[16].compatible[3] = "aix";
_[16].compatible[4] = "freebsd";
_[17] = {};
_[17].name = "hosts";
_[17].argument = "--hosts";
_[17].version = "1.0";
_[17].description = "/etc/hosts file parser";
_[17].author = "Kelly Brazil";
_[17].author_email = "kellyjonbrazil@gmail.com";
_[17].compatible = [];
_[17].compatible[0] = "linux";
_[17].compatible[1] = "darwin";
_[17].compatible[2] = "cygwin";
_[17].compatible[3] = "win32";
_[17].compatible[4] = "aix";
_[17].compatible[5] = "freebsd";
_[18] = {};
_[18].name = "id";
_[18].argument = "--id";
_[18].version = "1.0";
_[18].description = "id command parser";
_[18].author = "Kelly Brazil";
_[18].author_email = "kellyjonbrazil@gmail.com";
_[18].compatible = [];
_[18].compatible[0] = "linux";
_[18].compatible[1] = "darwin";
_[18].compatible[2] = "aix";
_[18].compatible[3] = "freebsd";
_[18].magic_commands = [];
_[18].magic_commands[0] = "id";
_[19] = {};
_[19].name = "ifconfig";
_[19].argument = "--ifconfig";
_[19].version = "1.5";
_[19].description = "ifconfig command parser";
_[19].author = "Kelly Brazil";
_[19].author_email = "kellyjonbrazil@gmail.com";
_[19].details = "Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser";
_[19].compatible = [];
_[19].compatible[0] = "linux";
_[19].compatible[1] = "aix";
_[19].compatible[2] = "freebsd";
_[19].compatible[3] = "darwin";
_[19].magic_commands = [];
_[19].magic_commands[0] = "ifconfig";
_[20] = {};
_[20].name = "ini";
_[20].argument = "--ini";
_[20].version = "1.0";
_[20].description = "INI file parser";
_[20].author = "Kelly Brazil";
_[20].author_email = "kellyjonbrazil@gmail.com";
_[20].details = "Using configparser from the standard library";
_[20].compatible = [];
_[20].compatible[0] = "linux";
_[20].compatible[1] = "darwin";
_[20].compatible[2] = "cygwin";
_[20].compatible[3] = "win32";
_[20].compatible[4] = "aix";
_[20].compatible[5] = "freebsd";
_[21] = {};
_[21].name = "iptables";
_[21].argument = "--iptables";
_[21].version = "1.1";
_[21].description = "iptables command parser";
_[21].author = "Kelly Brazil";
_[21].author_email = "kellyjonbrazil@gmail.com";
_[21].compatible = [];
_[21].compatible[0] = "linux";
_[21].magic_commands = [];
_[21].magic_commands[0] = "iptables";
_[22] = {};
_[22].name = "jobs";
_[22].argument = "--jobs";
_[22].version = "1.0";
_[22].description = "jobs command parser";
_[22].author = "Kelly Brazil";
_[22].author_email = "kellyjonbrazil@gmail.com";
_[22].compatible = [];
_[22].compatible[0] = "linux";
_[22].compatible[1] = "darwin";
_[22].compatible[2] = "cygwin";
_[22].compatible[3] = "aix";
_[22].compatible[4] = "freebsd";
_[22].magic_commands = [];
_[22].magic_commands[0] = "jobs";
_[23] = {};
_[23].name = "last";
_[23].argument = "--last";
_[23].version = "1.0";
_[23].description = "last and lastb command parser";
_[23].author = "Kelly Brazil";
_[23].author_email = "kellyjonbrazil@gmail.com";
_[23].compatible = [];
_[23].compatible[0] = "linux";
_[23].compatible[1] = "darwin";
_[23].compatible[2] = "aix";
_[23].compatible[3] = "freebsd";
_[23].magic_commands = [];
_[23].magic_commands[0] = "last";
_[23].magic_commands[1] = "lastb";
_[24] = {};
_[24].name = "ls";
_[24].argument = "--ls";
_[24].version = "1.3";
_[24].description = "ls command parser";
_[24].author = "Kelly Brazil";
_[24].author_email = "kellyjonbrazil@gmail.com";
_[24].compatible = [];
_[24].compatible[0] = "linux";
_[24].compatible[1] = "darwin";
_[24].compatible[2] = "cygwin";
_[24].compatible[3] = "aix";
_[24].compatible[4] = "freebsd";
_[24].magic_commands = [];
_[24].magic_commands[0] = "ls";
_[25] = {};
_[25].name = "lsblk";
_[25].argument = "--lsblk";
_[25].version = "1.3";
_[25].description = "lsblk command parser";
_[25].author = "Kelly Brazil";
_[25].author_email = "kellyjonbrazil@gmail.com";
_[25].compatible = [];
_[25].compatible[0] = "linux";
_[25].magic_commands = [];
_[25].magic_commands[0] = "lsblk";
_[26] = {};
_[26].name = "lsmod";
_[26].argument = "--lsmod";
_[26].version = "1.1";
_[26].description = "lsmod command parser";
_[26].author = "Kelly Brazil";
_[26].author_email = "kellyjonbrazil@gmail.com";
_[26].compatible = [];
_[26].compatible[0] = "linux";
_[26].magic_commands = [];
_[26].magic_commands[0] = "lsmod";
_[27] = {};
_[27].name = "lsof";
_[27].argument = "--lsof";
_[27].version = "1.0";
_[27].description = "lsof command parser";
_[27].author = "Kelly Brazil";
_[27].author_email = "kellyjonbrazil@gmail.com";
_[27].compatible = [];
_[27].compatible[0] = "linux";
_[27].magic_commands = [];
_[27].magic_commands[0] = "lsof";
_[28] = {};
_[28].name = "mount";
_[28].argument = "--mount";
_[28].version = "1.1";
_[28].description = "mount command parser";
_[28].author = "Kelly Brazil";
_[28].author_email = "kellyjonbrazil@gmail.com";
_[28].compatible = [];
_[28].compatible[0] = "linux";
_[28].compatible[1] = "darwin";
_[28].magic_commands = [];
_[28].magic_commands[0] = "mount";
_[29] = {};
_[29].name = "netstat";
_[29].argument = "--netstat";
_[29].version = "1.2";
_[29].description = "netstat command parser";
_[29].author = "Kelly Brazil";
_[29].author_email = "kellyjonbrazil@gmail.com";
_[29].compatible = [];
_[29].compatible[0] = "linux";
_[29].magic_commands = [];
_[29].magic_commands[0] = "netstat";
_[30] = {};
_[30].name = "ntpq";
_[30].argument = "--ntpq";
_[30].version = "1.0";
_[30].description = "ntpq -p command parser";
_[30].author = "Kelly Brazil";
_[30].author_email = "kellyjonbrazil@gmail.com";
_[30].compatible = [];
_[30].compatible[0] = "linux";
_[30].magic_commands = [];
_[30].magic_commands[0] = "ntpq";
_[31] = {};
_[31].name = "passwd";
_[31].argument = "--passwd";
_[31].version = "1.0";
_[31].description = "/etc/passwd file parser";
_[31].author = "Kelly Brazil";
_[31].author_email = "kellyjonbrazil@gmail.com";
_[31].compatible = [];
_[31].compatible[0] = "linux";
_[31].compatible[1] = "darwin";
_[31].compatible[2] = "aix";
_[31].compatible[3] = "freebsd";
_[32] = {};
_[32].name = "pip_list";
_[32].argument = "--pip-list";
_[32].version = "1.0";
_[32].description = "pip list command parser";
_[32].author = "Kelly Brazil";
_[32].author_email = "kellyjonbrazil@gmail.com";
_[32].compatible = [];
_[32].compatible[0] = "linux";
_[32].compatible[1] = "darwin";
_[32].compatible[2] = "cygwin";
_[32].compatible[3] = "win32";
_[32].compatible[4] = "aix";
_[32].compatible[5] = "freebsd";
_[32].magic_commands = [];
_[32].magic_commands[0] = "pip list";
_[32].magic_commands[1] = "pip3 list";
_[33] = {};
_[33].name = "pip_show";
_[33].argument = "--pip-show";
_[33].version = "1.0";
_[33].description = "pip show command parser";
_[33].author = "Kelly Brazil";
_[33].author_email = "kellyjonbrazil@gmail.com";
_[33].compatible = [];
_[33].compatible[0] = "linux";
_[33].compatible[1] = "darwin";
_[33].compatible[2] = "cygwin";
_[33].compatible[3] = "win32";
_[33].compatible[4] = "aix";
_[33].compatible[5] = "freebsd";
_[33].magic_commands = [];
_[33].magic_commands[0] = "pip show";
_[33].magic_commands[1] = "pip3 show";
_[34] = {};
_[34].name = "ps";
_[34].argument = "--ps";
_[34].version = "1.1";
_[34].description = "ps command parser";
_[34].author = "Kelly Brazil";
_[34].author_email = "kellyjonbrazil@gmail.com";
_[34].compatible = [];
_[34].compatible[0] = "linux";
_[34].compatible[1] = "darwin";
_[34].compatible[2] = "cygwin";
_[34].compatible[3] = "aix";
_[34].compatible[4] = "freebsd";
_[34].magic_commands = [];
_[34].magic_commands[0] = "ps";
_[35] = {};
_[35].name = "route";
_[35].argument = "--route";
_[35].version = "1.0";
_[35].description = "route command parser";
_[35].author = "Kelly Brazil";
_[35].author_email = "kellyjonbrazil@gmail.com";
_[35].compatible = [];
_[35].compatible[0] = "linux";
_[35].magic_commands = [];
_[35].magic_commands[0] = "route";
_[36] = {};
_[36].name = "shadow";
_[36].argument = "--shadow";
_[36].version = "1.0";
_[36].description = "/etc/shadow file parser";
_[36].author = "Kelly Brazil";
_[36].author_email = "kellyjonbrazil@gmail.com";
_[36].compatible = [];
_[36].compatible[0] = "linux";
_[36].compatible[1] = "darwin";
_[36].compatible[2] = "aix";
_[36].compatible[3] = "freebsd";
_[37] = {};
_[37].name = "ss";
_[37].argument = "--ss";
_[37].version = "1.0";
_[37].description = "ss command parser";
_[37].author = "Kelly Brazil";
_[37].author_email = "kellyjonbrazil@gmail.com";
_[37].compatible = [];
_[37].compatible[0] = "linux";
_[37].magic_commands = [];
_[37].magic_commands[0] = "ss";
_[38] = {};
_[38].name = "stat";
_[38].argument = "--stat";
_[38].version = "1.0";
_[38].description = "stat command parser";
_[38].author = "Kelly Brazil";
_[38].author_email = "kellyjonbrazil@gmail.com";
_[38].compatible = [];
_[38].compatible[0] = "linux";
_[38].magic_commands = [];
_[38].magic_commands[0] = "stat";
_[39] = {};
_[39].name = "systemctl";
_[39].argument = "--systemctl";
_[39].version = "1.0";
_[39].description = "systemctl command parser";
_[39].author = "Kelly Brazil";
_[39].author_email = "kellyjonbrazil@gmail.com";
_[39].compatible = [];
_[39].compatible[0] = "linux";
_[39].magic_commands = [];
_[39].magic_commands[0] = "systemctl";
_[40] = {};
_[40].name = "systemctl_lj";
_[40].argument = "--systemctl-lj";
_[40].version = "1.0";
_[40].description = "systemctl list-jobs command parser";
_[40].author = "Kelly Brazil";
_[40].author_email = "kellyjonbrazil@gmail.com";
_[40].compatible = [];
_[40].compatible[0] = "linux";
_[40].magic_commands = [];
_[40].magic_commands[0] = "systemctl list-jobs";
_[41] = {};
_[41].name = "systemctl_ls";
_[41].argument = "--systemctl-ls";
_[41].version = "1.0";
_[41].description = "systemctl list-sockets command parser";
_[41].author = "Kelly Brazil";
_[41].author_email = "kellyjonbrazil@gmail.com";
_[41].compatible = [];
_[41].compatible[0] = "linux";
_[41].magic_commands = [];
_[41].magic_commands[0] = "systemctl list-sockets";
_[42] = {};
_[42].name = "systemctl_luf";
_[42].argument = "--systemctl-luf";
_[42].version = "1.0";
_[42].description = "systemctl list-unit-files command parser";
_[42].author = "Kelly Brazil";
_[42].author_email = "kellyjonbrazil@gmail.com";
_[42].compatible = [];
_[42].compatible[0] = "linux";
_[42].magic_commands = [];
_[42].magic_commands[0] = "systemctl list-unit-files";
_[43] = {};
_[43].name = "timedatectl";
_[43].argument = "--timedatectl";
_[43].version = "1.0";
_[43].description = "timedatectl status command parser";
_[43].author = "Kelly Brazil";
_[43].author_email = "kellyjonbrazil@gmail.com";
_[43].compatible = [];
_[43].compatible[0] = "linux";
_[43].magic_commands = [];
_[43].magic_commands[0] = "timedatectl";
_[43].magic_commands[1] = "timedatectl status";
_[44] = {};
_[44].name = "uname";
_[44].argument = "--uname";
_[44].version = "1.1";
_[44].description = "uname -a command parser";
_[44].author = "Kelly Brazil";
_[44].author_email = "kellyjonbrazil@gmail.com";
_[44].compatible = [];
_[44].compatible[0] = "linux";
_[44].compatible[1] = "darwin";
_[44].magic_commands = [];
_[44].magic_commands[0] = "uname";
_[45] = {};
_[45].name = "uptime";
_[45].argument = "--uptime";
_[45].version = "1.0";
_[45].description = "uptime command parser";
_[45].author = "Kelly Brazil";
_[45].author_email = "kellyjonbrazil@gmail.com";
_[45].compatible = [];
_[45].compatible[0] = "linux";
_[45].compatible[1] = "darwin";
_[45].compatible[2] = "cygwin";
_[45].compatible[3] = "aix";
_[45].compatible[4] = "freebsd";
_[45].magic_commands = [];
_[45].magic_commands[0] = "uptime";
_[46] = {};
_[46].name = "w";
_[46].argument = "--w";
_[46].version = "1.0";
_[46].description = "w command parser";
_[46].author = "Kelly Brazil";
_[46].author_email = "kellyjonbrazil@gmail.com";
_[46].compatible = [];
_[46].compatible[0] = "linux";
_[46].compatible[1] = "darwin";
_[46].compatible[2] = "cygwin";
_[46].compatible[3] = "aix";
_[46].compatible[4] = "freebsd";
_[46].magic_commands = [];
_[46].magic_commands[0] = "w";
_[47] = {};
_[47].name = "who";
_[47].argument = "--who";
_[47].version = "1.0";
_[47].description = "who command parser";
_[47].author = "Kelly Brazil";
_[47].author_email = "kellyjonbrazil@gmail.com";
_[47].compatible = [];
_[47].compatible[0] = "linux";
_[47].compatible[1] = "darwin";
_[47].compatible[2] = "cygwin";
_[47].compatible[3] = "aix";
_[47].compatible[4] = "freebsd";
_[47].magic_commands = [];
_[47].magic_commands[0] = "who";
_[48] = {};
_[48].name = "xml";
_[48].argument = "--xml";
_[48].version = "1.0";
_[48].description = "XML file parser";
_[48].author = "Kelly Brazil";
_[48].author_email = "kellyjonbrazil@gmail.com";
_[48].details = "Using the xmltodict library at https://github.com/martinblech/xmltodict";
_[48].compatible = [];
_[48].compatible[0] = "linux";
_[48].compatible[1] = "darwin";
_[48].compatible[2] = "cygwin";
_[48].compatible[3] = "win32";
_[48].compatible[4] = "aix";
_[48].compatible[5] = "freebsd";
_[49] = {};
_[49].name = "yaml";
_[49].argument = "--yaml";
_[49].version = "1.0";
_[49].description = "YAML file parser";
_[49].author = "Kelly Brazil";
_[49].author_email = "kellyjonbrazil@gmail.com";
_[49].details = "Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml";
_[49].compatible = [];
_[49].compatible[0] = "linux";
_[49].compatible[1] = "darwin";
_[49].compatible[2] = "cygwin";
_[49].compatible[3] = "win32";
_[49].compatible[4] = "aix";
_[49].compatible[5] = "freebsd";
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-s', '_.parsers']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_c_parsers(self):
        """
        Test jc -a | jello -c '_["parsers"]'
        """
        expected = '''[{"name":"airport","argument":"--airport","version":"1.0","description":"airport -I command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -I"]},{"name":"airport_s","argument":"--airport-s","version":"1.0","description":"airport -s command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -s"]},{"name":"arp","argument":"--arp","version":"1.2","description":"arp command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["arp"]},{"name":"blkid","argument":"--blkid","version":"1.0","description":"blkid command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["blkid"]},{"name":"crontab","argument":"--crontab","version":"1.1","description":"crontab command and file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["crontab"]},{"name":"crontab_u","argument":"--crontab-u","version":"1.0","description":"crontab file parser with user support","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"csv","argument":"--csv","version":"1.0","description":"CSV file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the python standard csv library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"df","argument":"--df","version":"1.1","description":"df command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["df"]},{"name":"dig","argument":"--dig","version":"1.1","description":"dig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["dig"]},{"name":"du","argument":"--du","version":"1.1","description":"du command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["du"]},{"name":"env","argument":"--env","version":"1.1","description":"env command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["env"]},{"name":"file","argument":"--file","version":"1.1","description":"file command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["file"]},{"name":"free","argument":"--free","version":"1.0","description":"free command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["free"]},{"name":"fstab","argument":"--fstab","version":"1.0","description":"fstab file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"]},{"name":"group","argument":"--group","version":"1.0","description":"/etc/group file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"gshadow","argument":"--gshadow","version":"1.0","description":"/etc/gshadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd"]},{"name":"history","argument":"--history","version":"1.2","description":"history command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Optimizations by https://github.com/philippeitis","compatible":["linux","darwin","cygwin","aix","freebsd"]},{"name":"hosts","argument":"--hosts","version":"1.0","description":"/etc/hosts file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"id","argument":"--id","version":"1.0","description":"id command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["id"]},{"name":"ifconfig","argument":"--ifconfig","version":"1.5","description":"ifconfig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["ifconfig"]},{"name":"ini","argument":"--ini","version":"1.0","description":"INI file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using configparser from the standard library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"iptables","argument":"--iptables","version":"1.1","description":"iptables command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["iptables"]},{"name":"jobs","argument":"--jobs","version":"1.0","description":"jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["jobs"]},{"name":"last","argument":"--last","version":"1.0","description":"last and lastb command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["last","lastb"]},{"name":"ls","argument":"--ls","version":"1.3","description":"ls command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ls"]},{"name":"lsblk","argument":"--lsblk","version":"1.3","description":"lsblk command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsblk"]},{"name":"lsmod","argument":"--lsmod","version":"1.1","description":"lsmod command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsmod"]},{"name":"lsof","argument":"--lsof","version":"1.0","description":"lsof command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsof"]},{"name":"mount","argument":"--mount","version":"1.1","description":"mount command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["mount"]},{"name":"netstat","argument":"--netstat","version":"1.2","description":"netstat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["netstat"]},{"name":"ntpq","argument":"--ntpq","version":"1.0","description":"ntpq -p command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ntpq"]},{"name":"passwd","argument":"--passwd","version":"1.0","description":"/etc/passwd file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"pip_list","argument":"--pip-list","version":"1.0","description":"pip list command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip list","pip3 list"]},{"name":"pip_show","argument":"--pip-show","version":"1.0","description":"pip show command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip show","pip3 show"]},{"name":"ps","argument":"--ps","version":"1.1","description":"ps command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ps"]},{"name":"route","argument":"--route","version":"1.0","description":"route command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["route"]},{"name":"shadow","argument":"--shadow","version":"1.0","description":"/etc/shadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"ss","argument":"--ss","version":"1.0","description":"ss command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ss"]},{"name":"stat","argument":"--stat","version":"1.0","description":"stat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["stat"]},{"name":"systemctl","argument":"--systemctl","version":"1.0","description":"systemctl command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl"]},{"name":"systemctl_lj","argument":"--systemctl-lj","version":"1.0","description":"systemctl list-jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-jobs"]},{"name":"systemctl_ls","argument":"--systemctl-ls","version":"1.0","description":"systemctl list-sockets command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-sockets"]},{"name":"systemctl_luf","argument":"--systemctl-luf","version":"1.0","description":"systemctl list-unit-files command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-unit-files"]},{"name":"timedatectl","argument":"--timedatectl","version":"1.0","description":"timedatectl status command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["timedatectl","timedatectl status"]},{"name":"uname","argument":"--uname","version":"1.1","description":"uname -a command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["uname"]},{"name":"uptime","argument":"--uptime","version":"1.0","description":"uptime command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["uptime"]},{"name":"w","argument":"--w","version":"1.0","description":"w command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["w"]},{"name":"who","argument":"--who","version":"1.0","description":"who command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["who"]},{"name":"xml","argument":"--xml","version":"1.0","description":"XML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the xmltodict library at https://github.com/martinblech/xmltodict","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"yaml","argument":"--yaml","version":"1.0","description":"YAML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}]
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-c', '_["parsers"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_c_parsers_dot(self):
        """
        Test jc -a | jello -c _.parsers
        """
        expected = '''[{"name":"airport","argument":"--airport","version":"1.0","description":"airport -I command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -I"]},{"name":"airport_s","argument":"--airport-s","version":"1.0","description":"airport -s command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -s"]},{"name":"arp","argument":"--arp","version":"1.2","description":"arp command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["arp"]},{"name":"blkid","argument":"--blkid","version":"1.0","description":"blkid command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["blkid"]},{"name":"crontab","argument":"--crontab","version":"1.1","description":"crontab command and file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["crontab"]},{"name":"crontab_u","argument":"--crontab-u","version":"1.0","description":"crontab file parser with user support","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"csv","argument":"--csv","version":"1.0","description":"CSV file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the python standard csv library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"df","argument":"--df","version":"1.1","description":"df command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["df"]},{"name":"dig","argument":"--dig","version":"1.1","description":"dig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["dig"]},{"name":"du","argument":"--du","version":"1.1","description":"du command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["du"]},{"name":"env","argument":"--env","version":"1.1","description":"env command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["env"]},{"name":"file","argument":"--file","version":"1.1","description":"file command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["file"]},{"name":"free","argument":"--free","version":"1.0","description":"free command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["free"]},{"name":"fstab","argument":"--fstab","version":"1.0","description":"fstab file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"]},{"name":"group","argument":"--group","version":"1.0","description":"/etc/group file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"gshadow","argument":"--gshadow","version":"1.0","description":"/etc/gshadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd"]},{"name":"history","argument":"--history","version":"1.2","description":"history command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Optimizations by https://github.com/philippeitis","compatible":["linux","darwin","cygwin","aix","freebsd"]},{"name":"hosts","argument":"--hosts","version":"1.0","description":"/etc/hosts file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"id","argument":"--id","version":"1.0","description":"id command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["id"]},{"name":"ifconfig","argument":"--ifconfig","version":"1.5","description":"ifconfig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["ifconfig"]},{"name":"ini","argument":"--ini","version":"1.0","description":"INI file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using configparser from the standard library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"iptables","argument":"--iptables","version":"1.1","description":"iptables command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["iptables"]},{"name":"jobs","argument":"--jobs","version":"1.0","description":"jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["jobs"]},{"name":"last","argument":"--last","version":"1.0","description":"last and lastb command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["last","lastb"]},{"name":"ls","argument":"--ls","version":"1.3","description":"ls command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ls"]},{"name":"lsblk","argument":"--lsblk","version":"1.3","description":"lsblk command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsblk"]},{"name":"lsmod","argument":"--lsmod","version":"1.1","description":"lsmod command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsmod"]},{"name":"lsof","argument":"--lsof","version":"1.0","description":"lsof command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsof"]},{"name":"mount","argument":"--mount","version":"1.1","description":"mount command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["mount"]},{"name":"netstat","argument":"--netstat","version":"1.2","description":"netstat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["netstat"]},{"name":"ntpq","argument":"--ntpq","version":"1.0","description":"ntpq -p command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ntpq"]},{"name":"passwd","argument":"--passwd","version":"1.0","description":"/etc/passwd file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"pip_list","argument":"--pip-list","version":"1.0","description":"pip list command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip list","pip3 list"]},{"name":"pip_show","argument":"--pip-show","version":"1.0","description":"pip show command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip show","pip3 show"]},{"name":"ps","argument":"--ps","version":"1.1","description":"ps command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ps"]},{"name":"route","argument":"--route","version":"1.0","description":"route command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["route"]},{"name":"shadow","argument":"--shadow","version":"1.0","description":"/etc/shadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]},{"name":"ss","argument":"--ss","version":"1.0","description":"ss command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ss"]},{"name":"stat","argument":"--stat","version":"1.0","description":"stat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["stat"]},{"name":"systemctl","argument":"--systemctl","version":"1.0","description":"systemctl command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl"]},{"name":"systemctl_lj","argument":"--systemctl-lj","version":"1.0","description":"systemctl list-jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-jobs"]},{"name":"systemctl_ls","argument":"--systemctl-ls","version":"1.0","description":"systemctl list-sockets command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-sockets"]},{"name":"systemctl_luf","argument":"--systemctl-luf","version":"1.0","description":"systemctl list-unit-files command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-unit-files"]},{"name":"timedatectl","argument":"--timedatectl","version":"1.0","description":"timedatectl status command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["timedatectl","timedatectl status"]},{"name":"uname","argument":"--uname","version":"1.1","description":"uname -a command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["uname"]},{"name":"uptime","argument":"--uptime","version":"1.0","description":"uptime command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["uptime"]},{"name":"w","argument":"--w","version":"1.0","description":"w command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["w"]},{"name":"who","argument":"--who","version":"1.0","description":"who command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["who"]},{"name":"xml","argument":"--xml","version":"1.0","description":"XML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the xmltodict library at https://github.com/martinblech/xmltodict","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]},{"name":"yaml","argument":"--yaml","version":"1.0","description":"YAML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}]
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-c', '_.parsers']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_l_parsers(self):
        """
        Test jc -a | jello -l '_["parsers"]'
        """
        expected = '''\
{"name":"airport","argument":"--airport","version":"1.0","description":"airport -I command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -I"]}
{"name":"airport_s","argument":"--airport-s","version":"1.0","description":"airport -s command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -s"]}
{"name":"arp","argument":"--arp","version":"1.2","description":"arp command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["arp"]}
{"name":"blkid","argument":"--blkid","version":"1.0","description":"blkid command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["blkid"]}
{"name":"crontab","argument":"--crontab","version":"1.1","description":"crontab command and file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["crontab"]}
{"name":"crontab_u","argument":"--crontab-u","version":"1.0","description":"crontab file parser with user support","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"csv","argument":"--csv","version":"1.0","description":"CSV file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the python standard csv library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"df","argument":"--df","version":"1.1","description":"df command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["df"]}
{"name":"dig","argument":"--dig","version":"1.1","description":"dig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["dig"]}
{"name":"du","argument":"--du","version":"1.1","description":"du command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["du"]}
{"name":"env","argument":"--env","version":"1.1","description":"env command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["env"]}
{"name":"file","argument":"--file","version":"1.1","description":"file command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["file"]}
{"name":"free","argument":"--free","version":"1.0","description":"free command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["free"]}
{"name":"fstab","argument":"--fstab","version":"1.0","description":"fstab file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"]}
{"name":"group","argument":"--group","version":"1.0","description":"/etc/group file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"gshadow","argument":"--gshadow","version":"1.0","description":"/etc/gshadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd"]}
{"name":"history","argument":"--history","version":"1.2","description":"history command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Optimizations by https://github.com/philippeitis","compatible":["linux","darwin","cygwin","aix","freebsd"]}
{"name":"hosts","argument":"--hosts","version":"1.0","description":"/etc/hosts file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"id","argument":"--id","version":"1.0","description":"id command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["id"]}
{"name":"ifconfig","argument":"--ifconfig","version":"1.5","description":"ifconfig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["ifconfig"]}
{"name":"ini","argument":"--ini","version":"1.0","description":"INI file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using configparser from the standard library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"iptables","argument":"--iptables","version":"1.1","description":"iptables command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["iptables"]}
{"name":"jobs","argument":"--jobs","version":"1.0","description":"jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["jobs"]}
{"name":"last","argument":"--last","version":"1.0","description":"last and lastb command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["last","lastb"]}
{"name":"ls","argument":"--ls","version":"1.3","description":"ls command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ls"]}
{"name":"lsblk","argument":"--lsblk","version":"1.3","description":"lsblk command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsblk"]}
{"name":"lsmod","argument":"--lsmod","version":"1.1","description":"lsmod command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsmod"]}
{"name":"lsof","argument":"--lsof","version":"1.0","description":"lsof command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsof"]}
{"name":"mount","argument":"--mount","version":"1.1","description":"mount command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["mount"]}
{"name":"netstat","argument":"--netstat","version":"1.2","description":"netstat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["netstat"]}
{"name":"ntpq","argument":"--ntpq","version":"1.0","description":"ntpq -p command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ntpq"]}
{"name":"passwd","argument":"--passwd","version":"1.0","description":"/etc/passwd file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"pip_list","argument":"--pip-list","version":"1.0","description":"pip list command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip list","pip3 list"]}
{"name":"pip_show","argument":"--pip-show","version":"1.0","description":"pip show command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip show","pip3 show"]}
{"name":"ps","argument":"--ps","version":"1.1","description":"ps command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ps"]}
{"name":"route","argument":"--route","version":"1.0","description":"route command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["route"]}
{"name":"shadow","argument":"--shadow","version":"1.0","description":"/etc/shadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"ss","argument":"--ss","version":"1.0","description":"ss command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ss"]}
{"name":"stat","argument":"--stat","version":"1.0","description":"stat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["stat"]}
{"name":"systemctl","argument":"--systemctl","version":"1.0","description":"systemctl command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl"]}
{"name":"systemctl_lj","argument":"--systemctl-lj","version":"1.0","description":"systemctl list-jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-jobs"]}
{"name":"systemctl_ls","argument":"--systemctl-ls","version":"1.0","description":"systemctl list-sockets command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-sockets"]}
{"name":"systemctl_luf","argument":"--systemctl-luf","version":"1.0","description":"systemctl list-unit-files command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-unit-files"]}
{"name":"timedatectl","argument":"--timedatectl","version":"1.0","description":"timedatectl status command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["timedatectl","timedatectl status"]}
{"name":"uname","argument":"--uname","version":"1.1","description":"uname -a command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["uname"]}
{"name":"uptime","argument":"--uptime","version":"1.0","description":"uptime command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["uptime"]}
{"name":"w","argument":"--w","version":"1.0","description":"w command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["w"]}
{"name":"who","argument":"--who","version":"1.0","description":"who command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["who"]}
{"name":"xml","argument":"--xml","version":"1.0","description":"XML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the xmltodict library at https://github.com/martinblech/xmltodict","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"yaml","argument":"--yaml","version":"1.0","description":"YAML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', '_["parsers"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_l_parsers_dot(self):
        """
        Test jc -a | jello -l _.parsers
        """
        expected = '''\
{"name":"airport","argument":"--airport","version":"1.0","description":"airport -I command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -I"]}
{"name":"airport_s","argument":"--airport-s","version":"1.0","description":"airport -s command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["darwin"],"magic_commands":["airport -s"]}
{"name":"arp","argument":"--arp","version":"1.2","description":"arp command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["arp"]}
{"name":"blkid","argument":"--blkid","version":"1.0","description":"blkid command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["blkid"]}
{"name":"crontab","argument":"--crontab","version":"1.1","description":"crontab command and file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["crontab"]}
{"name":"crontab_u","argument":"--crontab-u","version":"1.0","description":"crontab file parser with user support","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"csv","argument":"--csv","version":"1.0","description":"CSV file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the python standard csv library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"df","argument":"--df","version":"1.1","description":"df command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["df"]}
{"name":"dig","argument":"--dig","version":"1.1","description":"dig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["dig"]}
{"name":"du","argument":"--du","version":"1.1","description":"du command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["du"]}
{"name":"env","argument":"--env","version":"1.1","description":"env command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["env"]}
{"name":"file","argument":"--file","version":"1.1","description":"file command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["file"]}
{"name":"free","argument":"--free","version":"1.0","description":"free command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["free"]}
{"name":"fstab","argument":"--fstab","version":"1.0","description":"fstab file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"]}
{"name":"group","argument":"--group","version":"1.0","description":"/etc/group file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"gshadow","argument":"--gshadow","version":"1.0","description":"/etc/gshadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","aix","freebsd"]}
{"name":"history","argument":"--history","version":"1.2","description":"history command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Optimizations by https://github.com/philippeitis","compatible":["linux","darwin","cygwin","aix","freebsd"]}
{"name":"hosts","argument":"--hosts","version":"1.0","description":"/etc/hosts file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"id","argument":"--id","version":"1.0","description":"id command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["id"]}
{"name":"ifconfig","argument":"--ifconfig","version":"1.5","description":"ifconfig command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser","compatible":["linux","aix","freebsd","darwin"],"magic_commands":["ifconfig"]}
{"name":"ini","argument":"--ini","version":"1.0","description":"INI file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using configparser from the standard library","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"iptables","argument":"--iptables","version":"1.1","description":"iptables command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["iptables"]}
{"name":"jobs","argument":"--jobs","version":"1.0","description":"jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["jobs"]}
{"name":"last","argument":"--last","version":"1.0","description":"last and lastb command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"],"magic_commands":["last","lastb"]}
{"name":"ls","argument":"--ls","version":"1.3","description":"ls command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ls"]}
{"name":"lsblk","argument":"--lsblk","version":"1.3","description":"lsblk command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsblk"]}
{"name":"lsmod","argument":"--lsmod","version":"1.1","description":"lsmod command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsmod"]}
{"name":"lsof","argument":"--lsof","version":"1.0","description":"lsof command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["lsof"]}
{"name":"mount","argument":"--mount","version":"1.1","description":"mount command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["mount"]}
{"name":"netstat","argument":"--netstat","version":"1.2","description":"netstat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["netstat"]}
{"name":"ntpq","argument":"--ntpq","version":"1.0","description":"ntpq -p command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ntpq"]}
{"name":"passwd","argument":"--passwd","version":"1.0","description":"/etc/passwd file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"pip_list","argument":"--pip-list","version":"1.0","description":"pip list command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip list","pip3 list"]}
{"name":"pip_show","argument":"--pip-show","version":"1.0","description":"pip show command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","win32","aix","freebsd"],"magic_commands":["pip show","pip3 show"]}
{"name":"ps","argument":"--ps","version":"1.1","description":"ps command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["ps"]}
{"name":"route","argument":"--route","version":"1.0","description":"route command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["route"]}
{"name":"shadow","argument":"--shadow","version":"1.0","description":"/etc/shadow file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","aix","freebsd"]}
{"name":"ss","argument":"--ss","version":"1.0","description":"ss command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["ss"]}
{"name":"stat","argument":"--stat","version":"1.0","description":"stat command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["stat"]}
{"name":"systemctl","argument":"--systemctl","version":"1.0","description":"systemctl command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl"]}
{"name":"systemctl_lj","argument":"--systemctl-lj","version":"1.0","description":"systemctl list-jobs command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-jobs"]}
{"name":"systemctl_ls","argument":"--systemctl-ls","version":"1.0","description":"systemctl list-sockets command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-sockets"]}
{"name":"systemctl_luf","argument":"--systemctl-luf","version":"1.0","description":"systemctl list-unit-files command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["systemctl list-unit-files"]}
{"name":"timedatectl","argument":"--timedatectl","version":"1.0","description":"timedatectl status command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux"],"magic_commands":["timedatectl","timedatectl status"]}
{"name":"uname","argument":"--uname","version":"1.1","description":"uname -a command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin"],"magic_commands":["uname"]}
{"name":"uptime","argument":"--uptime","version":"1.0","description":"uptime command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["uptime"]}
{"name":"w","argument":"--w","version":"1.0","description":"w command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["w"]}
{"name":"who","argument":"--who","version":"1.0","description":"who command parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","compatible":["linux","darwin","cygwin","aix","freebsd"],"magic_commands":["who"]}
{"name":"xml","argument":"--xml","version":"1.0","description":"XML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the xmltodict library at https://github.com/martinblech/xmltodict","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
{"name":"yaml","argument":"--yaml","version":"1.0","description":"YAML file parser","author":"Kelly Brazil","author_email":"kellyjonbrazil@gmail.com","details":"Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml","compatible":["linux","darwin","cygwin","win32","aix","freebsd"]}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', '_.parsers']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_parsers_18(self):
        """
        Test jc -a | jello '_["parsers"][18]'
        """
        expected = '''\
{
  "name": "id",
  "argument": "--id",
  "version": "1.0",
  "description": "id command parser",
  "author": "Kelly Brazil",
  "author_email": "kellyjonbrazil@gmail.com",
  "compatible": [
    "linux",
    "darwin",
    "aix",
    "freebsd"
  ],
  "magic_commands": [
    "id"
  ]
}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_["parsers"][18]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_parsers_18_dot(self):
        """
        Test jc -a | jello _.parsers[18]
        """
        expected = '''\
{
  "name": "id",
  "argument": "--id",
  "version": "1.0",
  "description": "id command parser",
  "author": "Kelly Brazil",
  "author_email": "kellyjonbrazil@gmail.com",
  "compatible": [
    "linux",
    "darwin",
    "aix",
    "freebsd"
  ],
  "magic_commands": [
    "id"
  ]
}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_.parsers[18]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_s_parsers_18_dot(self):
        """
        Test jc -a | jello -s _.parsers[18]
        """
        expected = '''\
_ = {};
_.name = "id";
_.argument = "--id";
_.version = "1.0";
_.description = "id command parser";
_.author = "Kelly Brazil";
_.author_email = "kellyjonbrazil@gmail.com";
_.compatible = [];
_.compatible[0] = "linux";
_.compatible[1] = "darwin";
_.compatible[2] = "aix";
_.compatible[3] = "freebsd";
_.magic_commands = [];
_.magic_commands[0] = "id";
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-s', '_.parsers[18]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_parsers_18_name(self):
        """
        Test jc -a | jello '_["parsers"][18]["name"]'
        """
        expected = '"id"\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_["parsers"][18]["name"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_parsers_18_name_dot(self):
        """
        Test jc -a | jello _.parsers[18].name
        """
        expected = '"id"\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_.parsers[18].name']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_l_parsers_18_name(self):
        """
        Test jc -a | jello -l '_["parsers"][18]["name"]'
        """
        expected = '"id"\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', '_["parsers"][18]["name"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_l_parsers_18_name_dot(self):
        """
        Test jc -a | jello -l _.parsers[18].name
        """
        expected = '"id"\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', '_.parsers[18].name']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_r_parsers_18_name(self):
        """
        Test jc -a | jello -r '_["parsers"][18]["name"]'
        """
        expected = 'id\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-r', '_["parsers"][18]["name"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_r_parsers_18_name_dot(self):
        """
        Test jc -a | jello -r _.parsers[18].name
        """
        expected = 'id\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-r', '_.parsers[18].name']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_parsers_18_compatible(self):
        """
        Test jc -a | jello '_["parsers"][18]["compatible"]'
        """
        expected = '''\
[
  "linux",
  "darwin",
  "aix",
  "freebsd"
]
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_["parsers"][18]["compatible"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_parsers_18_compatible_dot(self):
        """
        Test jc -a | jello _.parsers[18].compatible
        """
        expected = '''\
[
  "linux",
  "darwin",
  "aix",
  "freebsd"
]
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_.parsers[18].compatible']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_s_parsers_18_compatible_dot(self):
        """
        Test jc -a | jello -s _.parsers[18].compatible
        """
        expected = '''\
_ = [];
_[0] = "linux";
_[1] = "darwin";
_[2] = "aix";
_[3] = "freebsd";
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-s', '_.parsers[18].compatible']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_c_parsers_18_compatible(self):
        """
        Test jc -a | jello -c '_["parsers"][18]["compatible"]'
        """
        expected = '["linux","darwin","aix","freebsd"]\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-c', '_["parsers"][18]["compatible"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_c_parsers_18_compatible_dot(self):
        """
        Test jc -a | jello -c _.parsers[18].compatible
        """
        expected = '["linux","darwin","aix","freebsd"]\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-c', '_.parsers[18].compatible']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_l_parsers_18_compatible(self):
        """
        Test jc -a | jello -l '_["parsers"][18]["compatible"]'
        """
        expected = '''\
"linux"
"darwin"
"aix"
"freebsd"
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', '_["parsers"][18]["compatible"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_l_parsers_18_compatible_dot(self):
        """
        Test jc -a | jello -l _.parsers[18].compatible
        """
        expected = '''\
"linux"
"darwin"
"aix"
"freebsd"
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', '_.parsers[18].compatible']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_lr_parsers_18_compatible(self):
        """
        Test jc -a | jello -lr '_["parsers"][18]["compatible"]'
        """
        expected = '''\
linux
darwin
aix
freebsd
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-lr', '_["parsers"][18]["compatible"]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_lr_parsers_18_compatible_dot(self):
        """
        Test jc -a | jello -lr _.parsers[18].compatible
        """
        expected = '''\
linux
darwin
aix
freebsd
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-lr', '_.parsers[18].compatible']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_c_list_comprehension(self):
        """
        Test jc -a | jello -c '[entry["name"] for entry in _["parsers"] if "darwin" in entry["compatible"]]'
        """
        expected = '["airport","airport_s","arp","crontab","crontab_u","csv","df","dig","du","env","file","group","history","hosts","id","ifconfig","ini","jobs","last","ls","mount","passwd","pip_list","pip_show","ps","shadow","uname","uptime","w","who","xml","yaml"]\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-c', '[entry["name"] for entry in _["parsers"] if "darwin" in entry["compatible"]]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_jc_a_c_list_comprehension_dot(self):
        """
        Test jc -a | jello -c '[entry.name for entry in _.parsers if "darwin" in entry.compatible]'
        """
        expected = '["airport","airport_s","arp","crontab","crontab_u","csv","df","dig","du","env","file","group","history","hosts","id","ifconfig","ini","jobs","last","ls","mount","passwd","pip_list","pip_show","ps","shadow","uname","uptime","w","who","xml","yaml"]\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-c', '[entry.name for entry in _.parsers if "darwin" in entry.compatible]']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.jc_a_output)
        self.assertEqual(f.getvalue(), expected)

    def test_twitter_jlines_to_json(self):
        """
        Test cat twitterdata.jlines | jello
        """
        expected = self.twitterdata_output

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.twitterdata)
        self.assertEqual(f.getvalue(), expected)

    def test_twitter_lines_table(self):
        """
        Test cat twitterdata.jlines | jello -l '\
                                      user_ids = set()
                                      result = []
                                      for tweet in _:
                                          user_ids.add(tweet["user"]["id"])
                                      for user in user_ids:
                                          user_profile = {}
                                          tweet_ids = []
                                          for tweet in _:
                                              if tweet["user"]["id"] == user:
                                                  user_profile.update({
                                                      "user_id": user,
                                                      "user_name": tweet["user"]["screen_name"],
                                                      "user_followers": tweet["user"]["followers_count"]})
                                                  tweet_ids.append(str(tweet["id"]))
                                          user_profile["tweet_ids"] = ";".join(tweet_ids)
                                          result.append(user_profile)
                                      result'
        """
        query = '''\
user_ids = set()
result = []
for tweet in _:
    user_ids.add(tweet["user"]["id"])
for user in sorted(user_ids):
    user_profile = {}
    tweet_ids = []
    for tweet in _:
        if tweet["user"]["id"] == user:
            user_profile.update({
                "user_id": user,
                "user_name": tweet["user"]["screen_name"],
                "user_followers": tweet["user"]["followers_count"]})
            tweet_ids.append(str(tweet["id"]))
    user_profile["tweet_ids"] = ";".join(tweet_ids)
    result.append(user_profile)
result
'''
        expected = self.twitter_table_output

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.twitterdata)
        self.assertEqual(f.getvalue(), expected)

    def test_twitter_lines_table_schema(self):
        """
        Test cat twitterdata.jlines | jello -s '\
                                      user_ids = set()
                                      result = []
                                      for tweet in _:
                                          user_ids.add(tweet["user"]["id"])
                                      for user in sorted(user_ids):
                                          user_profile = {}
                                          tweet_ids = []
                                          for tweet in _:
                                              if tweet["user"]["id"] == user:
                                                  user_profile.update({
                                                      "user_id": user,
                                                      "user_name": tweet["user"]["screen_name"],
                                                      "user_followers": tweet["user"]["followers_count"]})
                                                  tweet_ids.append(str(tweet["id"]))
                                          user_profile["tweet_ids"] = ";".join(tweet_ids)
                                          result.append(user_profile)
                                      result'
        """
        query = '''\
user_ids = set()
result = []
for tweet in _:
    user_ids.add(tweet["user"]["id"])
for user in sorted(user_ids):
    user_profile = {}
    tweet_ids = []
    for tweet in _:
        if tweet["user"]["id"] == user:
            user_profile.update({
                "user_id": user,
                "user_name": tweet["user"]["screen_name"],
                "user_followers": tweet["user"]["followers_count"]})
            tweet_ids.append(str(tweet["id"]))
    user_profile["tweet_ids"] = ";".join(tweet_ids)
    result.append(user_profile)
result
'''
        expected = self.twitter_table_output_schema

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-s', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.twitterdata)
        self.assertEqual(f.getvalue(), expected)

    def test_twitter_lines_table_dot(self):
        """
        Test cat twitterdata.jlines | jello -l '\
                                      user_ids = set()
                                      result = []
                                      for tweet in _:
                                          user_ids.add(tweet.user.id)
                                      for user in user_ids:
                                          user_profile = {}
                                          tweet_ids = []
                                          for tweet in _:
                                              if tweet.user.id == user:
                                                  user_profile.update({
                                                      "user_id": user,
                                                      "user_name": tweet.user.screen_name,
                                                      "user_followers": tweet.user.followers_count})
                                                  tweet_ids.append(str(tweet.id))
                                          user_profile.tweet_ids = ";".join(tweet_ids)
                                          result.append(user_profile)
                                      result'
        """
        query = '''\
user_ids = set()
result = []
for tweet in _:
  user_ids.add(tweet.user.id)
for user in sorted(user_ids):
  user_profile = {}
  tweet_ids = []
  for tweet in _:
      if tweet.user.id == user:
          user_profile.update({
              "user_id": user,
              "user_name": tweet.user.screen_name,
              "user_followers": tweet.user.followers_count})
          tweet_ids.append(str(tweet.id))
  user_profile["tweet_ids"] = ";".join(tweet_ids)
  result.append(user_profile)
result
'''
        expected = self.twitter_table_output

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-l', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=self.twitterdata)
        self.assertEqual(f.getvalue(), expected)


    def test_scope_with_comprehension(self):
        """
        fix for https://github.com/kellyjonbrazil/jello/issues/46
        """
        sample = '''\
        {
          "foods": [
            { "name": "carrot" },
            { "name": "banana" }
          ],
          "people": [
            { "name": "alice", "likes": "apples" },
            { "name": "bob", "likes": "banana" },
            { "name": "carrol", "likes": "carrot" },
            { "name": "dave", "likes": "donuts" }
          ]
        }'''
        query = '''\
foods = set(f.name for f in _.foods)
[p.name for p in _.people if p.likes not in foods]'''
        expected = '''[
  "alice",
  "dave"
]
'''

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)
        self.assertEqual(f.getvalue(), expected)

    def test_scope_with_comprehension2(self):
        """
        fix for https://github.com/kellyjonbrazil/jello/issues/46
        """
        sample = '''\
        {
          "foods": [
            { "name": "carrot" },
            { "name": "banana" }
          ],
          "people": [
            { "name": "alice", "likes": "apples" },
            { "name": "bob", "likes": "banana" },
            { "name": "carrol", "likes": "carrot" },
            { "name": "dave", "likes": "donuts" }
          ]
        }'''
        query = '''\
[p.name for p in _.people if p.likes not in (f.name for f in _.foods)]'''
        expected = '''[
  "alice",
  "dave"
]
'''

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)
        self.assertEqual(f.getvalue(), expected)


    def test_yield(self):
        sample = '''[1, 2, 3, 4]'''
        query = '''\
for i in _:
  yield i
'''
        expected = '''[
  1,
  2,
  3,
  4
]
'''

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)
        self.assertEqual(f.getvalue(), expected)


    def test_yield_from(self):
        sample = '''[[1, 2], [3, 4]]'''
        query = '''\
for l in _:
  yield from l
'''
        expected = '''[
  1,
  2,
  3,
  4
]
'''

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)
        self.assertEqual(f.getvalue(), expected)


    def test_initialization_file(self):

        # patch read_file function to mock initialization file
        old_read_file = copy.copy(jello.lib.read_file)
        jello.lib.read_file = lambda x: 'init_var = "test"'

        sample = '''{"a": "hello world"}'''
        expected = '"test"\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-i', 'init_var']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        jello.lib.read_file = old_read_file
        self.assertEqual(f.getvalue(), expected)


    def test_query_file(self):

        # patch read_file function to mock initialization file
        old_read_file = copy.copy(jello.cli.read_file)
        jello.cli.read_file = lambda x: 'init_var = "test"\ninit_var'

        sample = '''{"a": "hello world"}'''
        expected = '"test"\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-q', 'myqueryfile']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        jello.cli.read_file = old_read_file
        self.assertEqual(f.getvalue(), expected)


    def test_data_file(self):

        # patch read_file function to mock initialization file
        old_read_file = copy.copy(jello.cli.read_file)
        jello.lib.read_file = lambda x: '''{"a": "hello world"}'''

        sample = ''
        expected = '"hello world"\n'

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '_.a', '-f', 'mydatafile']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        jello.lib.read_file = old_read_file
        self.assertEqual(f.getvalue(), expected)


    def test_empty_data_option(self):
        sample = ''
        expected = '''\
{
  "a": "test"
}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-e', '{"a": "test"}']
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        self.assertEqual(f.getvalue(), expected)


    def test_flatten_generator(self):
        sample = ''
        query = '''\
yield {"k":1,"v":10}
yield {"k":2,"v":20}
'''
        expected = '''\
{
  "k": 1,
  "v": 10
}
{
  "k": 2,
  "v": 20
}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-F', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        self.assertEqual(f.getvalue(), expected)


    def test_flatten_iterable(self):
        sample = ''
        query = '''\
return [{"k":1,"v":10},{"k":2,"v":20}]
'''
        expected = '''\
{
  "k": 1,
  "v": 10
}
{
  "k": 2,
  "v": 20
}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-F', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        self.assertEqual(f.getvalue(), expected)


    def test_flatten_iterator(self):
        sample = ''
        query = '''\
class MyIterator:
  def __init__(self):
    self.vals = [{"k":1,"v":10},{"k":2,"v":20}]
    self.index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= len(self.vals):
      raise StopIteration
    val = self.vals[self.index]
    self.index += 1
    return val

MyIterator()
'''
        expected = '''\
{
  "k": 1,
  "v": 10
}
{
  "k": 2,
  "v": 20
}
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-F', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        self.assertEqual(f.getvalue(), expected)


    def test_flatten_error_not_iterator(self):
        sample = '{"k":1}'
        err_expected = '''-F/flatten requires the query to return an iterator/generator or list'''
        f = io.StringIO()
        f_err = io.StringIO()
        caught_ex = None
        with contextlib.redirect_stdout(f):
            with contextlib.redirect_stderr(f_err):
                testargs = ['jello', '-F']
                with patch.object(sys, 'argv', testargs):
                    try:
                        _ = jello.cli.main(data=sample)
                    except SystemExit as ex:
                        caught_ex = ex

        self.assertTrue(caught_ex)
        self.assertEqual(type(caught_ex), SystemExit)
        context = caught_ex.__context__
        self.assertTrue(caught_ex.__context__)
        self.assertEqual(type(context), TypeError)
        self.assertEqual(context.args[0], err_expected)


    def test_stream_input(self):
        sample = '''\
{"k":1,"v":10}
{"k":2,"v":20}
'''
        query = '''\
_
'''
        expected = '''\
[
  {
    "k": 1,
    "v": 10
  },
  {
    "k": 2,
    "v": 20
  }
]
'''
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            testargs = ['jello', '-S', query]
            with patch.object(sys, 'argv', testargs):
                _ = jello.cli.main(data=sample)

        self.assertEqual(f.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
