# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Deprecated APIs."""


IMPORTS = {
    '': """\x1f# Deprecated imports are kept for backward compatiblity and to be removed in\x1f# future versions. Please refer to public APIs for replacement:\x1f# https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker\x1f# pylint: disable=g-bad-import-order\x1ffrom tensorflow_examples.lite.model_maker.core.data_util.image_dataloader import ImageClassifierDataLoader\x1ffrom tensorflow_examples.lite.model_maker.core.export_format import ExportFormat\x1ffrom tensorflow_examples.lite.model_maker.core.task import configs\x1f# pylint: enable=g-bad-import-order\x1f"""
}
# pylint: enable=line-too-long
