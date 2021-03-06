# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to set IAM policy for an instance resource."""

from googlecloudsdk.api_lib.compute import iam_base_classes
from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class SetIamPolicy(iam_base_classes.RegionalSetIamPolicy):
  """Set the IAM policy for a Google Compute Engine subnetwork resource."""

  @staticmethod
  def Args(parser):
    iam_base_classes.RegionalSetIamPolicy.Args(parser, 'compute.subnetworks')

  @property
  def service(self):
    return self.compute.subnetworks

  @property
  def resource_type(self):
    return 'subnetworks'

SetIamPolicy.detailed_help = iam_base_classes.SetIamPolicyHelp('subnetwork')
