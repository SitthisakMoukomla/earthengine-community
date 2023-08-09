# Copyright 2023 The Google Earth Engine Community Authors
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

# [START earthengine__apidocs__ee_algorithms_objecttype]
print(ee.Algorithms.ObjectType(ee.Number(1)).getInfo())  # The string "Integer"
print(
    ee.Algorithms.ObjectType(ee.String('a string')).getInfo()
)  # The string "String"
print(
    ee.Algorithms.ObjectType(ee.List([1, 'a string'])).getInfo()
)  # The string "List"

# ee.Algorithms.ObjectType can be used to get the type of properties
# of ee.Image or ee.Feature objects.
feature = ee.Feature(
    None,  # No need for geometry in this example.
    {
        'int': 42,
        'int8': ee.Number(-3).int8(),
    }
)

# The string "Integer"
print('int:', ee.Algorithms.ObjectType(feature.get('int')).getInfo())
# The string "Long"
print('int8:', ee.Algorithms.ObjectType(feature.get('int8')).getInfo())
# [END earthengine__apidocs__ee_algorithms_objecttype]
