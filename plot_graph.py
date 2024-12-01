import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
pick_accuracy = pd.read_csv('push_initial.csv')
push_transfer_accuracy = pd.read_csv('push_transfered.csv')

# Extract necessary columns for plotting
steps_pick = pick_accuracy['Step']
values_pick = pick_accuracy['Value']

steps_push_transfer = push_transfer_accuracy['Step']
values_push_transfer = push_transfer_accuracy['Value']

# Plotting
plt.figure(figsize=(10, 6))

# Pick task accuracy
plt.plot(steps_pick, values_pick, label='Trained on Push', linewidth=2.5, linestyle='--', marker='o')

# Push task transferred accuracy
plt.plot(steps_push_transfer, values_push_transfer, label='Transferred from Pick to Push', linewidth=2.5, linestyle='-', marker='s')

# Enhancing visual appeal
plt.title('Model Success Comparison: Pick vs Push Task Transfer (100 demos)', fontsize=16, fontweight='bold')
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
