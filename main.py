
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output directory exists
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# Load datasets
calls_df = pd.read_csv('callsf0d4f5a.csv')
reason_df = pd.read_csv('reason18315ff.csv')
sentiment_statistics_df = pd.read_csv('sentiment_statisticscc1e57a.csv')

# Convert datetime columns to appropriate formats
calls_df['call_start_datetime'] = pd.to_datetime(calls_df['call_start_datetime'])
calls_df['call_end_datetime'] = pd.to_datetime(calls_df['call_end_datetime'])
calls_df['agent_assigned_datetime'] = pd.to_datetime(calls_df['agent_assigned_datetime'])

# Calculate Handle Time (AHT) and Waiting Time (AST)
calls_df['handle_time'] = (calls_df['call_end_datetime'] - calls_df['call_start_datetime']).dt.total_seconds()
calls_df['waiting_time'] = (calls_df['agent_assigned_datetime'] - calls_df['call_start_datetime']).dt.total_seconds()

# Merging datasets: calls_df with reason_df and sentiment_statistics_df
merged_df = pd.merge(calls_df, reason_df, on='call_id')
merged_df = pd.merge(merged_df, sentiment_statistics_df, on='call_id')

# Call Reason Analysis: AHT and AST by Call Reason
aht_by_reason = merged_df.groupby('primary_call_reason')['handle_time'].mean()
ast_by_reason = merged_df.groupby('primary_call_reason')['waiting_time'].mean()

# Visualization 1: Average Handle Time by Call Reason
plt.figure(figsize=(10, 6))
sns.barplot(x=aht_by_reason.index, y=aht_by_reason.values)
plt.title('Average Handle Time by Call Reason')
plt.ylabel('Handle Time (seconds)')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Show plot before saving to ensure it's generated
plt.show()

# Save the plot
aht_img_path = f'{output_dir}/aht_by_call_reason.png'
print(f"Saving AHT plot to {aht_img_path}")
plt.savefig(aht_img_path)
plt.close()

# Visualization 2: Average Speed to Answer by Call Reason
plt.figure(figsize=(10, 6))
sns.barplot(x=ast_by_reason.index, y=ast_by_reason.values)
plt.title('Average Speed to Answer by Call Reason')
plt.ylabel('Speed to Answer (seconds)')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Show plot before saving
plt.show()

# Save the plot
ast_img_path = f'{output_dir}/ast_by_call_reason.png'
print(f"Saving AST plot to {ast_img_path}")
plt.savefig(ast_img_path)
plt.close()

# Confirm completion
print("Plots generated and saved successfully.")
