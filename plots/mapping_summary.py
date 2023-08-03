# Create basic mapping plots from summary files colored by RL number
# Provide:
#   1 - path to the summary csv file
#   2 - path to the output file directory
#   3 - what to plot?

# Try running: python /home/dmakosa/working_data_04/scifi/plots/mapping_summary.py /home/dmakosa/working_data_02/scifiRNAseq/mapping.summary.csv /home/dmakosa/working_data_02/scifiRNAseq/plots 'Median UMI per Cell'

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

# Format the data
summary['Number of Reads'] = summary['Number of Reads']/1e6
summary['Reads With Valid Barcodes'] = summary['Reads With Valid Barcodes']*100
summary['Sequencing Saturation'] = summary['Sequencing Saturation']*100
summary['Reads Mapped to GeneFull: Unique+Multipe GeneFull'] = summary['Reads Mapped to GeneFull: Unique+Multipe GeneFull']*100
summary['Reads Mapped to GeneFull: Unique GeneFull'] = summary['Reads Mapped to GeneFull: Unique GeneFull']*100


# Actual plotting
sns.set_style("ticks")
sns.scatterplot(data = summary, x = 'Number of Reads', y = sys.argv[3], hue="RL", legend = 'auto')
plt.xlabel('Number of Reads [M]')
plt.ylabel(sys.argv[3])
current_xaxis = plt.gca().get_xticks()
plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in current_xaxis])

plt.savefig(sys.argv[2] + '/vsNoOfReads.' + sys.argv[3].replace(' ','') + '.png')