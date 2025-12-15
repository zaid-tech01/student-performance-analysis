import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/students.csv')

# Calculate average marks
df['average'] = df[['math', 'science', 'english']].mean(axis=1)

# Print averages
print(df[['name', 'average']])

# Top performer
top_student = df.loc[df['average'].idxmax()]
print("Top Student:", top_student['name'])

# Plot graph
plt.bar(df['name'], df['average'])
plt.xlabel('Students')
plt.ylabel('Average Marks')
plt.title('Student Performance')
plt.show()
