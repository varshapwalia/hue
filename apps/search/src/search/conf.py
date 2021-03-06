#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.utils.translation import ugettext_lazy as _

from desktop.conf import is_hue4
from desktop.lib.conf import Config, coerce_bool


SOLR_URL = Config(
  key="solr_url",
  help=_("URL of the Solr Server."),
  default="http://localhost:8983/solr/")

EMPTY_QUERY = Config(
  key="empty_query",
  help=_("Query sent when no term is entered."),
  default="*:*")

SECURITY_ENABLED = Config(
  key="security_enabled",
  help=_("Whether Solr requires client to perform Kerberos authentication."),
  default=False,
  type=coerce_bool)

LATEST = Config(
  key="latest",
  help=_("Use latest Solr 5.2+ features."),
  default=False,
  type=coerce_bool)

ENABLE_SQL = Config(
  key="enable_sql",
  help=_("Offer to use SQL engines to compute the dashboards."),
  dynamic_default=is_hue4,
  private=True,
  type=coerce_bool)
