# coding=utf-8
#================================================================#
#   Copyright (C) 2019 Freecss All rights reserved.
#   
#   File Name     ：run.py
#   Author        ：freecss
#   Email         ：karlfreecss@gmail.com
#   Created Date  ：2019/12/14
#   Description   ：
#
#================================================================#

import os
import shutil

def rmdir(dir_path):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        shutil.rmtree(dir_path)


'''
pretrain_bert_train_epochs_list = [3,2]
pretrain_sentence_model_times_list = [3]
abl_bert_train_epochs_list = [1,2,3,4]
abl_sentence_model_times_list = [3]
abl_max_change_num_list = [1,2]

pretrain_bert_train_epochs_list = [5,1]
pretrain_sentence_model_times_list = [3]
abl_bert_train_epochs_list = [1,2,3,4]
abl_sentence_model_times_list = [3]
abl_max_change_num_list = [1,2]
'''

pretrain_bert_train_epochs_list = [20] #3
pretrain_sentence_model_times_list = [3]
abl_bert_train_epochs_list = [1,2]
abl_sentence_model_times_list = [3]
abl_max_change_num_list = [2,3]

rule_file_paths = ["rule_test_file.txt"]
test_times = 7
abl_times = 7

#pretrain_bert_train_epochs_list = [1]
#pretrain_sentence_model_times_list = [1]
#abl_bert_train_epochs_list = [1]
#abl_sentence_model_times_list = [1]
#abl_max_change_num_list = [1]
#rule_file_paths = ["rule_test_file.txt"]
#times = 1

os.system("mkdir pk_files")
test_num = 0
for time in range(test_times): # 测试次数
    for pretrain_bert_train_epoch in pretrain_bert_train_epochs_list:
        for pretrain_sentence_model_times in pretrain_sentence_model_times_list:
            for abl_bert_train_epochs in abl_bert_train_epochs_list:
                for abl_sentence_model_times in abl_sentence_model_times_list:
                    for abl_max_change_num in abl_max_change_num_list:
                        for rule_file_path in rule_file_paths:
                            os.system("mkdir tmp")
                            rmdir("./abl_model_0") #Remove model
                            #result_file = "./result/result_"+str(pretrain_bert_train_epoch)+"_"+str(pretrain_sentence_model_times)+"_"+str(abl_bert_train_epochs)+"_"+str(abl_sentence_model_times)+"_"+str(abl_max_change_num)+("_time_%d.out" % time)
                            result_file = f"./result/result_{pretrain_bert_train_epoch}_{pretrain_sentence_model_times}_{abl_bert_train_epochs}_{abl_sentence_model_times}_{abl_max_change_num}_{rule_file_path}_time_{time}.out"
                            # run ss_abl_model.py
                            cmd = "python -u abl_model.py -pretrain_bert_train_epochs=%d -pretrain_sentence_model_times=%d -abl_bert_train_epochs=%d -abl_sentence_model_times=%d -abl_max_change_num=%d -rule_file_path=%s -log_dump_file=%s -abl_times=%d > %s" % (pretrain_bert_train_epoch, pretrain_sentence_model_times, abl_bert_train_epochs, abl_sentence_model_times, abl_max_change_num, rule_file_path, ("pk_files/%05d.pk" % test_num), abl_times, result_file)
                            print("\n\n\nStart training")
                            print(cmd)
                            print("=================================================")
                            os.system(cmd)
                            os.system("mkdir test_id_%d && mv tmp/ log.txt test_id_%d && cp -r data test_id_%d" % (test_num, test_num, test_num))
                            test_num += 1

