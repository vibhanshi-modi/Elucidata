# Elucidata_DataProcessing

This flask server involves basic data processing using pandas. Following are the major 4 APIs implemented-
1) Uploading of the .xlsx file to be processed.
2) In third column “Accepted Compound ID”, filtering out all the data for metabolite ids ending with:
‘PC’, ‘LPC’ and ‘plasmalogen’, and creating 3 child datasets (1 for each compound id) from the data in input file.
3) Adding a new column in the parent dataset with the name “Retention Time Roundoff (in mins)”. This column
contains rounded-off values of the corresponding retention time. Retention time is rounded-off to
the nearest natural number.
4) Finding the mean of all the metabolites which have same "Retention Time Roundoff"
across all the samples. The resultant of above operation is a new data-frame where the "Retention Time Roundoff" column is included for all samples.

All the APIs download the output after the tasks have been completed in a folder called outputs.
