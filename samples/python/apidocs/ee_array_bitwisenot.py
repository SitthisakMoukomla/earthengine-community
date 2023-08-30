# Copyright 2021 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START earthengine__apidocs__ee_array_bitwisenot]
empty = ee.Array([], ee.PixelType.int8())
display(empty.bitwiseNot())  # []

display(ee.Array(0).bitwiseNot())  # -1
display(ee.Array(1).bitwiseNot())  # -2
display(ee.Array(0xFF).bitwiseNot())  # -256

display(ee.Array(-1).bitwiseNot())  # 0
display(ee.Array(-2).bitwiseNot())  # 1
display(ee.Array(-3).bitwiseNot())  # 2

display(ee.Array(0xFF).toInt64().bitwiseNot())  # -256
# [END earthengine__apidocs__ee_array_bitwisenot]
