#!/bin/sh

python test.py --dataroot ./datasets/evol_pairs_mini_rgb --name poke_evol_mini_reduced_aug --model pix2pix --direction BtoA  --num_test 130 --gpu_ids -1

python test.py --dataroot ./datasets/evol_pairs_mini_rgb --name poke_evol_mini_reduced_aug --model pix2pix --direction BtoA  --num_test 130 --epoch 50 --gpu_ids -1

python test.py --dataroot ./datasets/evol_pairs_mini_rgb --name poke_evol_mini_reduced_aug --model pix2pix --direction BtoA  --num_test 130 --epoch 55 --gpu_ids -1
