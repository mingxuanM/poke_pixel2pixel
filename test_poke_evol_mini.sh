#!/bin/sh

python test.py --dataroot ./datasets/evol_pairs_mini_rgb --name poke_evol_mini_reduced_aug --model pix2pix --direction BtoA  --num_test 130 --epoch 30 --gpu_ids -1

python test.py --dataroot ./datasets/evol_pairs_mini_rgb --name poke_evol_mini_reduced_aug --model pix2pix --direction BtoA  --num_test 130 --epoch 70 --gpu_ids -1

python test.py --dataroot ./datasets/evol_pairs_mini_rgb --name poke_evol_mini_reduced_aug --model pix2pix --direction BtoA  --num_test 130 --epoch 90 --gpu_ids -1
