import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

# Function to clean and process the data

def clean_data(df):
    # Sort by Step to ensure chronological order
    df = df.sort_values('Step')
    
    # For each unique step, keep the maximum value
    # This ensures we don't go back to zero after reaching non-zero values
    max_values = {}
    cleaned_data = []
    
    current_max = 0  # Keep track of maximum value seen so far
    
    for _, row in df.iterrows():
        step = row['Step']
        value = row['Value']
        
        # If we haven't seen this step before
        if step not in max_values:
            # Only update current_max if new value is higher
            current_max = max(current_max, value)
            max_values[step] = current_max
            cleaned_data.append({'Step': step, 'Value': current_max})
    
    return pd.DataFrame(cleaned_data).sort_values('Step')

# Read the CSV files
# push_df = pd.read_csv('D:/Deep Learning/Project/Push_Cube/train_success_once.csv')
# pick_df = pd.read_csv('D:/Deep Learning/Project/Pick_Cube/pick_train_success_once.csv')
# push_transfer_df = pd.read_csv('D:/Deep Learning/Project/Push_Pick_Transfer/push_transfer_train_success_once.csv')

push_df = pd.read_csv('D:/Deep Learning/Project/Push_Cube/policy_loss.csv')
pick_df = pd.read_csv('D:/Deep Learning/Project/Pick_Cube/pick_eval_success_end.csv')
push_transfer_df = pd.read_csv('D:/Deep Learning/Project/Push_Pick_Transfer/push_transfer_losses_value_loss.csv')


 #Clean each dataset
# push_df = clean_data(push_df)
# pick_df = clean_data(pick_df)
# push_transfer_df = clean_data(push_transfer_df)

# Remove duplicates keeping first occurrence for each Step
push_df = push_df.drop_duplicates(subset='Step', keep='first').sort_values('Step')
pick_df = pick_df.drop_duplicates(subset='Step', keep='first').sort_values('Step')
push_transfer_df = push_transfer_df.drop_duplicates(subset='Step', keep='first').sort_values('Step')
# Find the maximum number of steps
max_steps = max(
    push_df['Step'].max(),
    pick_df['Step'].max(),
    push_transfer_df['Step'].max()
)
max_steps = push_transfer_df['Step'].max()
# Create the plot
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Plot each line up to max_steps
# plt.plot(push_df['Step'], push_df['Value'], label='Push from Scratch', linewidth=2)
# plt.plot(pick_df['Step'], pick_df['Value'], label='Pick from Scratch', linewidth=2)
plt.plot(push_transfer_df['Step'], push_transfer_df['Value'], label='Push with Transfer from Pick', linewidth=2, linestyle='--')

# Set x-axis limit to max steps
plt.xlim(0, max_steps)

# Customize the plot
plt.xlabel('Training Steps', fontsize=12)
plt.ylabel('Value Loss', fontsize=12)
plt.title('Value Loss vs Steps (Transfer Learning using PPO)', fontsize=14, pad=15)
plt.legend(fontsize=10)

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Optional: Print max steps and number of points for verification
print(f"Maximum steps: {max_steps}")
print(f"Push data points: {len(push_df)}")
print(f"Pick data points: {len(pick_df)}")
print(f"Push transfer data points: {len(push_transfer_df)}")

# Save the plot
plt.savefig('training_success.png', dpi=300, bbox_inches='tight')
plt.show()