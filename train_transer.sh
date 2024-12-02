#!/bin/bash

NUM_DEMOS=100

python train_transfer.py --env-id PickCube-v1 \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100 \  
    --total_iters 30000 --seed 2

python train_transfer.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 3

python train_transfer.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 4

python train_transfer.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 5

NUM_DEMOS=50

python train.py --env-id PickCube-v1 \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100 \  
    --total_iters 30000 --seed 2

python train.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 3

python train.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 4

python train.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 5

NUM_DEMOS=25

python train.py --env-id PickCube-v1 \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100 \  
    --total_iters 30000 --seed 2

python train.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 3

python train.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 4

python train.py --env-id PickCube-v1   \
    --demo-path ~/.maniskill/demos/PickCube-v1/motionplanning/trajectory.state.pd_ee_delta_pos.cpu.h5   \
    --control-mode "pd_ee_delta_pos" --sim-backend "cpu" \
    --num-demos $NUM_DEMOS --max_episode_steps 100   \
    --total_iters 30000 --seed 5