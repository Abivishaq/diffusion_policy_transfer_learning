from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
import os
def get_success_data_from_tb_file(file_path):
    """
    Reads a single TensorBoard file and extracts scalar data.

    Args:
        file_path (str): Path to the TensorBoard `.tfevents` file.

    Returns:
        dict: A dictionary where keys are tags and values are lists of (step, value) tuples.
    """
    # Load the event file
    event_acc = EventAccumulator(file_path)
    event_acc.Reload()  # Load data from the file

    # Extract scalar data
    # scalars = {}
    # for tag in event_acc.Tags()['scalars']:
    #     scalar_events = event_acc.Scalars(tag)
    #     scalars[tag] = [(e.step, e.value) for e in scalar_events]
    tag = "eval/success_at_end"
    scalar_events = event_acc.Scalars(tag)
    successes = [(e.step, e.value) for e in scalar_events]

    return successes

# Example usage
# file_path = "/home/abivishaq/projects/GT_courseworks/fall24/Deep_learning/project/diffusion_policy_transfer_learning/runs/PickCube-v1__train__1__1732985543/events.out.tfevents.1732985550.rail-desktop-4.31672.0"  # Replace with your file path
# scalar_data = get_success_data_from_tb_file(file_path)

# print(scalar_data)
# Print the extracted data
# for tag, values in scalar_data.items():
#     print(f"Tag: {tag}")
#     print("Data:", values[:5])  # Print the first 5 records for the tag
dptl_pth = "/home/abivishaq/projects/GT_courseworks/fall24/Deep_learning/project/diffusion_policy_transfer_learning"#os.environ['DPTL_PATH']

run_dir = os.path.join(dptl_pth, "runs")

successes_random = {}
successes_transfer = {}

# reading csv 
import pandas as pd

# Load the datasets
pick_accuracy = pd.read_csv('runs/push_initial.csv')
push_transfer_accuracy = pd.read_csv('runs/push_transfered.csv')

# Extract necessary columns for plotting
steps_pick = pick_accuracy['Step']
values_pick = pick_accuracy['Value']
data = [(step,value) for step, value in zip(steps_pick, values_pick)]
successes_random[100] = data

steps_push_transfer = push_transfer_accuracy['Step']
values_push_transfer = push_transfer_accuracy['Value']
data = [(step,value) for step, value in zip(steps_push_transfer, values_push_transfer)]
successes_transfer[100] = data

for run_name in os.listdir(run_dir):
    if run_name.startswith("PushCube-v1__train"):
        run_path = os.path.join(run_dir, run_name)
        if "transfer" in run_name:
            dct_to_update = successes_transfer
        else:
            dct_to_update = successes_random
        print(run_path)
        # gettting the details file
        details_file = os.path.join(run_path, "exp_details.txt")
        with open(details_file, 'r') as f:
            details = f.readlines()
        dataset_size = int(details[0].split(":")[1].strip())
        print("dataset_size", dataset_size)
        # get the event file
        fls = os.listdir(run_path)
        print(fls)
        for fl in fls:
            if "events" in fl:
                file_path = os.path.join(run_path, fl)
                scalar_data = get_success_data_from_tb_file(file_path)
                break        
        dct_to_update[dataset_size] = scalar_data

# plot the data
import matplotlib.pyplot as plt
import numpy as np
number_of_colors = len(successes_random.keys())
colors = plt.cm.viridis(np.linspace(0, 1, number_of_colors))
n=0
for key in successes_random.keys():

    data = successes_random[key]
    print(data)
    x, y = zip(*data)
    plt.plot(x, y, label=f"Push {key} demos", linestyle="--", color=colors[n])

    data = successes_transfer[key]
    x, y = zip(*data)
    plt.plot(x, y, label=f"Pick to Push {key} demos", linestyle="-", color=colors[n])
    n+=1

# plt.xlabel("Steps")
# plt.ylabel("Success Rate")
# # plt.legend()

# Enhancing visual appeal
plt.title('Model Success Comparison: Pick to Push Task Transfer', fontsize=16, fontweight='bold')
plt.xlabel('Training Iterations', fontsize=14)
plt.ylabel('Success_rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(alpha=0.3, linestyle='--')

# Adding legend with color-blind safe colors
plt.legend(fontsize=12, loc='lower right', frameon=True, edgecolor='black')

# Show the plot
plt.tight_layout()
plt.savefig('Success_comparison.png')
plt.show()
