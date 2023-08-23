# coding=utf-8
# Copyright 2020 The Google Research Authors.
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

"""Returns task instances given the task name."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import configure_finetuning
from finetune.classification import classification_tasks
from finetune.qa import qa_tasks
from finetune.tagging import tagging_tasks
from model import tokenization


def get_tasks(config: configure_finetuning.FinetuningConfig):
  tokenizer = tokenization.FullTokenizer(vocab_file=config.vocab_file,
                                         do_lower_case=config.do_lower_case)
  return [get_task(config, task_name, tokenizer)
          for task_name in config.task_names]


def get_task(config: configure_finetuning.FinetuningConfig, task_name,
             tokenizer):
  """Get an instance of a task based on its name."""
  if task_name == "POS_NEG":
    return classification_tasks.POS_NEG(config, tokenizer)
  elif task_name == "BA":
    return classification_tasks.BA(config, tokenizer)
  elif task_name == "CA":
    return classification_tasks.CA(config, tokenizer)
  elif task_name == "FE2":
    return classification_tasks.FE2(config, tokenizer)
  elif task_name == "FE3":
    return classification_tasks.FE3(config, tokenizer)
  elif task_name == "LI":
    return classification_tasks.LI(config, tokenizer)
  elif task_name == "ZN":
    return classification_tasks.ZN(config, tokenizer)
  elif task_name == "CA":
    return classification_tasks.CA(config, tokenizer)
  elif task_name == "MG":
    return classification_tasks.MG(config, tokenizer)
  elif task_name == "MN":
    return classification_tasks.MN(config, tokenizer)
  elif task_name == "CU":
    return classification_tasks.CU(config, tokenizer)
  elif task_name == "CO":
    return classification_tasks.CO(config, tokenizer)
  elif task_name == "K":
    return classification_tasks.K(config, tokenizer)
  elif task_name == "NA":
    return classification_tasks.NA(config, tokenizer)
  elif task_name == "CD":
    return classification_tasks.CD(config, tokenizer)
  elif task_name == "NI":
    return classification_tasks.NI(config, tokenizer)
  elif task_name == "SO4":
    return classification_tasks.SO4(config, tokenizer)
  elif task_name == "I":
    return classification_tasks.I(config, tokenizer)
  elif task_name == "CL":
    return classification_tasks.CL(config, tokenizer)
  elif task_name == "BR":
    return classification_tasks.BR(config, tokenizer)
  elif task_name == "F":
    return classification_tasks.F(config, tokenizer)
  elif task_name == "SO4":
    return classification_tasks.SO4(config, tokenizer)
  elif task_name == "PO4":
    return classification_tasks.PO4(config, tokenizer)
  elif task_name == "NO2":
    return classification_tasks.NO2(config, tokenizer)
  elif task_name == "CO3":
    return classification_tasks.CO3(config, tokenizer)
  else:
    raise ValueError("Unknown task " + task_name)

