true_data.head()
fake_data.head()
merged_data = merged_data.sample(frac=1).reset_index(drop=True)
merged_data.head()
merged_data.dtypes
# Calculate label distribution
label_distribution = merged_data['label'].value_counts()

# Extracting labels and counts for pie chart
labels = [f"{label} ({count})" for label, count in zip(label_distribution.index, label_distribution.values)]

# Plotting the pie chart
plt.figure(figsize=(4, 4))
plt.pie(label_distribution, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Label Distribution')
plt.show()

