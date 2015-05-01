# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gns3.network_client import getNetworkUrl


def test_getNetworkUrl():
    assert getNetworkUrl("http", "localhost", 8000) == "http://localhost:8000"
    assert getNetworkUrl("http", "localhost", 8000, "root") == "http://root@localhost:8000"


def test_ssh_getNetworkUrl():
    settings = {"ssh_port": 22}
    assert getNetworkUrl("ssh", "localhost", 8000, "root", settings=settings) == "ssh://root@localhost:22:8000"
