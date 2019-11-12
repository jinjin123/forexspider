# -*- coding: utf-8 -*- 
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import paddle
import paddle.fluid as fluid
import paddlehub as hub


class AibaseApi:
    def __init__(self):
        self.dataset = hub.dataset.DemoDataset()
        self.module_in = "/root/dataset/module_in"
        self.module = hub.Module(name="ernie")
        self.metrics_choices = ["acc"]

    def load(self):
        inputs, outputs, program = self.module.context(
        trainable=True, max_seq_len=128)

        reader = hub.reader.ClassifyReader(
        dataset=self.dataset,
                vocab_path=self.module.get_vocab_path(),
        	max_seq_len=128,
        	use_task_id=False)

        pooled_output = outputs["pooled_output"]
        feed_list = [
                inputs["input_ids"].name,
                inputs["position_ids"].name,
                inputs["segment_ids"].name,
                inputs["input_mask"].name,
                ]
	
        config = hub.RunConfig(
                use_pyreader=False,
                use_cuda=True,
        	batch_size=30,
        	enable_memory_optim=False,
        	checkpoint_dir=self.module_in,
        	strategy=hub.finetune.strategy.DefaultFinetuneStrategy())

        cls_task = hub.TextClassifierTask(
        	data_reader=reader,
        	feature=pooled_output,
        	feed_list=feed_list,
        	num_classes=self.dataset.num_labels,
        	config=config,
        	metrics_choices=self.metrics_choices)

        return cls_task
