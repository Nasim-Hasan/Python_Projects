# @title Load the imports
import keras
import numpy as np
import pandas as pd
import plotly.express as px

# The following lines adjust the granularity of reporting.
pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

# @title Load the dataset
email_dataset = pd.read_excel("E-mail_Data.xlsx")
print ("E-mail Dataset:\n")
print(email_dataset)

year = email_dataset['Year']
true_positive = email_dataset['True_Positive']
false_positive = email_dataset['False_Positive']
true_negative = email_dataset['True_Negative']
false_negative = email_dataset['False_Negative']

print(f"Year Column:\n{year}\n")
print(f"True Positive Column:\n{true_positive}\n")
print(f"False Positive Column:\n{false_positive}\n")
print(f"True Negative Column:\n{true_negative}\n")
print(f"False Negative Column:\n{false_negative}\n")

def determine_accuracy() -> dict[int, float]:
  accuracy_dataframe : dict[int, float] = {}
  for i in range(len(email_dataset)):
       tp = true_positive[i]
       fp = false_positive[i]
       tn = true_negative[i]
       fn = false_negative[i]
       # Calculating Accuracy for Each Year
       print(f"Calculating accuracy for Year {year[i]}:")
       print(f"True Positives: {tp}")
       print(f"False Positives: {fp}")
       print(f"True Negatives: {tn}")
       print(f"False Negatives: {fn}")
       # Accuracy formula: (TP + TN) / (TP + FP + TN + FN)
       total_predictions = tp + fp + tn + fn
       if total_predictions > 0:
           accuracy = (tp + tn) / total_predictions
           accuracy = accuracy * 100  # Convert to percentage
           accuracy_dataframe[year[i]] = accuracy
       else:
           print(f"No predictions for Year {year[i]}, cannot calculate accuracy.\n")
  return accuracy_dataframe

def determine_tpr() -> dict[int, float]:
    tpr_dataframe : dict[int, float] = {}
    for i in range(len(email_dataset)):
         tp = true_positive[i]
         fn = false_negative[i]
         # Calculating TPR for Each Year
         print(f"Calculating TPR for Year {year[i]}:")
         print(f"True Positives: {tp}")
         print(f"False Negatives: {fn}")
         # TPR formula: TP / (TP + FN)
         total_actual_positives = tp + fn
         if total_actual_positives > 0:
             tpr = tp / total_actual_positives
             tpr = tpr * 100  # Convert to percentage
             tpr_dataframe[year[i]] = tpr
         else:
             print(f"No actual positives for Year {year[i]}, cannot calculate TPR.\n")
    return tpr_dataframe

def determine_fpr() -> dict[int, float]:
    fpr_dataframe : dict[int, float] = {}
    for i in range(len(email_dataset)):
         fp = false_positive[i]
         tn = true_negative[i]
         # Calculating FPR for Each Year
         print(f"Calculating FPR for Year {year[i]}:")
         print(f"False Positives: {fp}")
         print(f"True Negatives: {tn}")
         # FPR formula: FP / (FP + TN)
         total_actual_negatives = fp + tn
         if total_actual_negatives > 0:
             fpr = fp / total_actual_negatives
             fpr = fpr * 100  # Convert to percentage
             fpr_dataframe[year[i]] = fpr
         else:
             print(f"No actual negatives for Year {year[i]}, cannot calculate FPR.\n")
    return fpr_dataframe

def determine_precision() -> dict[int, float]:
    precision_dataframe : dict[int, float] = {}
    for i in range(len(email_dataset)):
         tp = true_positive[i]
         fp = false_positive[i]
         # Calculating Precision for Each Year
         print(f"Calculating Precision for Year {year[i]}:")
         print(f"True Positives: {tp}")
         print(f"False Positives: {fp}")
         # Precision formula: TP / (TP + FP)
         total_predicted_positives = tp + fp
         if total_predicted_positives > 0:
             precision = tp / total_predicted_positives
             precision = precision * 100  # Convert to percentage
             precision_dataframe[year[i]] = precision
         else:
             print(f"No predicted positives for Year {year[i]}, cannot calculate Precision.\n")
    return precision_dataframe

def main() -> None:
    #..Model's Accuracy Calculation
    accuracy = determine_accuracy()
    print(f"Model Accuracy: {accuracy}\n")
    #..Model's Recall/True Positive rate (TPR) Calculation
    recall = determine_tpr()
    print(f"Model Recall/True Positive Rate (TPR): {recall}\n")
    #..Model's False Alarm/False Positive rate (FPR) Calculation
    fpr = determine_fpr()
    print(f"Model False Alarm/False Positive Rate (FPR): {fpr}\n")
    #..Model's Precision Calculation
    precision = determine_precision()
    print(f"Model Precision: {precision}\n")
    #..Plotting Accuracy over the Years
    accuracy_plot = px.line(
        x=list(accuracy.keys()),
        y=list(accuracy.values()),
        title="Model Accuracy Over the Years",
        labels={"x": "Year", "y": "Accuracy (%)"}
    )
    accuracy_plot.show()
    #..Plotting Recall/TPR over the Years
    recall_plot = px.line(
        x=list(recall.keys()),
        y=list(recall.values()),
        title="Model Recall/True Positive Rate (TPR) Over the Years",
        labels={"x": "Year", "y": "Recall/TPR (%)"}
    )
    recall_plot.show()
    #..Plotting False Alarm/FPR over the Years
    fpr_plot = px.line(
        x=list(fpr.keys()),
        y=list(fpr.values()),
        title="Model False Alarm/False Positive Rate (FPR) Over the Years",
        labels={"x": "Year", "y": "False Alarm/FPR (%)"}
    )
    fpr_plot.show()
    #..Plotting Precision over the Years
    precision_plot = px.line(
        x=list(precision.keys()),
        y=list(precision.values()),
        title="Model Precision Over the Years",
        labels={"x": "Year", "y": "Precision (%)"}
    )
    precision_plot.show()

if __name__ == "__main__":
    # ✅ Program entry point
    main()