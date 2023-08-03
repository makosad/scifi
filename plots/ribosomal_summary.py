# Create basic mapping plots from summary files colored by RL number
# Provide:
#   1 - path to the summary csv file
#   2 - path to the output file directory
#   3 - what to plot?

# Try running: python /home/dmakosa/working_data_04/scifi/plots/ribosomal_summary.py /home/dmakosa/working_data_02/scifiRNAseq/ribosomalMapped.summary.csv /home/dmakosa/working_data_02/scifiRNAseq/plots 'FractionRibosomal'

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

summary_path = sys.argv[1]
# Read in the dependencies
summary = pd.read_csv(summary_path, sep = ',')

summary[['RL','well','sample#']] = summary['Sample'].str.split("_", expand = True)

# Exclude samples from printing
summary = summary.loc[~summary['Sample'].str.contains('undetermined', case=False)]

# Actual plotting
sns.set_style("ticks")
sns.violinplot(data = summary, x = 'RL', y = sys.argv[3])
plt.xlabel('Sample')
plt.ylabel(sys.argv[3])

plt.savefig(sys.argv[2] + '/violin.' + sys.argv[3].replace(' ','') + '.png')