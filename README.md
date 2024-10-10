# callcentere_project_skyhack


# Call Center Data Analysis

## Introduction
This project aims to analyze call center data from United Airlines to improve two key performance metrics:
1. **Average Handle Time (AHT)** - The total time an agent spends on a call.
2. **Average Speed to Answer (AST)** - The time a customer waits in the queue before the call is answered.

By optimizing these metrics, the project seeks to reduce customer wait time, improve agent efficiency, and enhance overall customer satisfaction.

## Objectives
- Identify call reasons that contribute to higher AHT and AST.
- Provide insights into call handling inefficiencies.
- Offer actionable recommendations to improve both metrics.

## Data Overview
The following datasets are used in this analysis:
1. **callsf0d4f5a.csv**: Contains information about call times, durations, and agent assignments.
2. **reason18315ff.csv**: Lists the reasons for each call.
3. **sentiment_statisticscc1e57a.csv**: Provides sentiment analysis of the calls, including customer and agent tones.

### Key Fields in the Data:
- **call_start_datetime**: When the call started.
- **call_end_datetime**: When the call ended.
- **agent_assigned_datetime**: When the agent was assigned to the call.
- **primary_call_reason**: The reason for the call (e.g., booking, post-flight inquiries).
- **agent_tone** and **customer_tone**: Sentiment scores based on the tones detected in the conversation.

## Installation Instructions
To run this project locally, follow the steps below:

### Prerequisites
Ensure that you have Python installed on your system. The required Python packages include:
- `pandas`
- `matplotlib`
- `seaborn`

### Install the necessary packages:
```bash
pip install pandas matplotlib seaborn
```

## Project Setup
1. Clone or download the project to your local machine.
2. Navigate to the project directory and place the necessary CSV files inside the `data` folder:
   - `callsf0d4f5a.csv`
   - `reason18315ff.csv`
   - `sentiment_statisticscc1e57a.csv`

### Folder Structure:
```
/project-directory
   /data
      callsf0d4f5a.csv
      reason18315ff.csv
      sentiment_statisticscc1e57a.csv
   /scripts
      main.py
   /output
      (Generated visualizations will be saved here)
   README.md
```

## How to Run the Code
After setting up the files, follow these steps to run the project:

1. Navigate to the project directory in the terminal:
   ```bash
   cd /path/to/project-directory
   ```

2. Run the main Python script:
   ```bash
   python scripts/main.py
   ```

## Expected Output
The script will generate two visualizations in the `output/` folder:

1. **`aht_by_call_reason.png`**:
   - A bar chart displaying the average handle time for each call reason. This helps identify the call types that require the most time to resolve.

2. **`ast_by_call_reason.png`**:
   - A bar chart showing the average speed to answer for each call reason. This highlights the types of calls that tend to have the longest wait times.

## Analysis and Insights
### 1. **Average Handle Time (AHT) by Call Reason**:
This chart allows you to pinpoint the call reasons associated with the longest call durations. For example, a high AHT for "Post-Flight" or "Checkout" calls could indicate that these processes are more complex or require additional agent support.



![aht_by_call_reason](https://github.com/user-attachments/assets/8536aae2-1ef8-489e-8457-7fdc7b510b2e)





### 2. **Average Speed to Answer (AST) by Call Reason**:
This chart highlights the customer wait times. Long wait times for certain call reasons (e.g., "Post-Flight" or "Mileage Plus") could suggest the need for more resources or streamlined call routing.




![ast_by_call_reason](https://github.com/user-attachments/assets/136ad2a8-aa97-4aa5-a549-855d1fae0cf8)







### Actionable Recommendations:
- **Reduce AHT**: Consider automating simpler call processes or providing agents with more comprehensive training on high-AHT call types.
- **Decrease AST**: Improve call routing efficiency or introduce more self-service options for customers to address common issues.

## Conclusion
This analysis provides actionable insights that can help United Airlines optimize their call center operations, reduce customer wait times, and improve agent efficiency. By addressing inefficiencies in both AHT and AST, the airline can enhance customer satisfaction and streamline support processes.

## Contact Information
For questions or further discussion, please reach out to the project maintainer:
- **Name**: Hemant Solanki
- **Email**: hemant.solanki.ug21@nsut.ac.in
