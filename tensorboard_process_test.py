from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
import os
import numpy as np
import matplotlib.pyplot as plt

dataset_size_ = 100

def get_success_data_from_tb_file(file_path):
    event_acc = EventAccumulator(file_path)
    event_acc.Reload()
    tag = "eval/success_at_end"
    scalar_events = event_acc.Scalars(tag)
    successes = [(e.step, e.value) for e in scalar_events]
    return successes

# Directories and data initialization
dptl_pth = "/home/abivishaq/projects/GT_coursework/fall_2024/DL/diffusion_policy"
run_dir = os.path.join(dptl_pth, "runs")
successes_random = {}
successes_transfer = {}

# Collect data across runs
for run_name in os.listdir(run_dir):
    if run_name.startswith("PushCube-v1__train"):
        run_path = os.path.join(run_dir, run_name)
        if "transfer" in run_name:
            dct_to_update = successes_transfer
        else:
            dct_to_update = successes_random

        # Read dataset size from details file
        details_file = os.path.join(run_path, "exp_details.txt")
        with open(details_file, 'r') as f:
            details = f.readlines()
        dataset_size = int(details[0].split(":")[1].strip())
        # if dataset_size != dataset_size_:
        #     continue

        # Get the event file
        fls = os.listdir(run_path)
        for fl in fls:
            if "events" in fl:
                file_path = os.path.join(run_path, fl)
                scalar_data = get_success_data_from_tb_file(file_path)
                break

        if dataset_size in dct_to_update:
            dct_to_update[dataset_size].append(scalar_data)
        else:
            dct_to_update[dataset_size] = [scalar_data]

# Aggregate data
def aggregate_success_data(data_dict):
    mean_dict = {}
    std_dict = {}

    for dataset_size, data_list in data_dict.items():
        # Get all iterations for all runs
        all_steps = [x[0] for x in data_list[0]]
        all_values = np.array([[x[1] for x in data] for data in data_list])

        # Calculate mean and standard deviation
        mean_values = np.mean(all_values, axis=0)
        std_values = np.std(all_values, axis=0)

        mean_dict[dataset_size] = (all_steps, mean_values)
        std_dict[dataset_size] = std_values

    return mean_dict, std_dict

mean_random, std_random = aggregate_success_data(successes_random)
mean_transfer, std_transfer = aggregate_success_data(successes_transfer)

# Plot aggregated data
# number_of_colors = len(mean_random)
# colors = plt.cm.viridis(np.linspace(0, 1, number_of_colors+1))
no_colors = 3
colors = ['r', 'g', 'b']

for i, dataset_size in enumerate(mean_random):
    steps, random_mean = mean_random[dataset_size]
    random_std = std_random[dataset_size]
    _, transfer_mean = mean_transfer[dataset_size]
    transfer_std = std_transfer[dataset_size]
    if dataset_size != dataset_size_:
        alpha_mult = 1
    else:
        alpha_mult = 1

    # Plot random policy success rate
    plt.plot(steps, random_mean, label=f"Push {dataset_size} demos", linestyle="--", color=colors[i], alpha=alpha_mult, linewidth=2)
    plt.fill_between(steps, random_mean - random_std, random_mean + random_std, color=colors[i], alpha=0.2*alpha_mult)

    # Plot transfer policy success rate
    plt.plot(steps, transfer_mean, label=f"Pick to Push {dataset_size} demos", linestyle="-", color=colors[i], alpha=alpha_mult, linewidth=2)
    plt.fill_between(steps, transfer_mean - transfer_std, transfer_mean + transfer_std, color=colors[i], alpha=0.2*alpha_mult)

# Enhancing visual appeal
plt.title('Model Success Comparison: Pick to Push Task Transfer', fontsize=16, fontweight='bold')
plt.xlabel('Training Iterations', fontsize=14)
plt.ylabel('Success Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(alpha=0.3, linestyle='-')

# Adding legend with color-blind safe colors
plt.legend(fontsize=12, loc='lower right', frameon=True, edgecolor='black')

# Show the plot
plt.tight_layout()
# plt.savefig('Success_comparison'+str(dataset_size_)+'.png')
plt.savefig('Success_comparison.png')

plt.show()
