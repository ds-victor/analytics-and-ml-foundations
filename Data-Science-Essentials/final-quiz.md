# Final Quiz: Data Science Essentials

Test your knowledge of the data science lifecycle. Choose the best answer for each question.

## Beginner (6 Questions)
1. **What is the primary difference between Data Analytics and Data Science?**
   - A) Analytics uses SQL, Science uses Python.
   - B) Analytics focuses on historical insights, while Science focuses on predictive modeling.
   - C) There is no difference.
   - D) Analytics is for business people, Science is for engineers.

2. **What does the 'S' in SMART objectives stand for?**
   - A) Simple
   - B) Standard
   - C) Specific
   - D) Strategic

3. **Which file is used to specify Python dependencies for a project?**
   - A) setup.py
   - B) config.yaml
   - C) requirements.txt
   - D) .gitignore

4. **What is the purpose of a `.gitignore` file?**
   - A) To ignore errors in your code.
   - B) To specify which files should not be tracked by Git.
   - C) To delete files from your hard drive.
   - D) To hide files from other users on your computer.

5. **Which of the following is a categorical variable in our house price dataset?**
   - A) `sqft`
   - B) `price`
   - C) `location`
   - D) `year_built`

6. **Why do we use virtual environments?**
   - A) To make the code run faster.
   - B) To isolate project-specific dependencies.
   - C) To run code on a remote server.
   - D) To protect our computer from viruses.

## Intermediate (8 Questions)
7. **Which metric is most appropriate for a regression task where you want to penalize large errors heavily?**
   - A) MAE
   - B) Accuracy
   - C) RMSE
   - D) Precision

8. **What is 'Data Leakage'?**
   - A) When a dataset is accidentally deleted.
   - B) When information from the test set is used to train the model.
   - C) When data is leaked to the public.
   - D) When a database connection is left open.

9. **In Feature Engineering, what is 'One-Hot Encoding' used for?**
   - A) Scaling numerical variables to a range of 0 to 1.
   - B) Converting categorical variables into a numerical format.
   - C) Handling missing values.
   - D) Reducing the number of features in a dataset.

10. **What is the 'Bias-Variance Trade-off'?**
    - A) Balancing model complexity and generalization error.
    - B) Choosing between two different datasets.
    - C) Trading off training time for accuracy.
    - D) The cost of data collection vs. the value of the model.

11. **Why is a 'Stratified Split' used?**
    - A) To ensure the training set is larger than the test set.
    - B) To maintain the same proportion of a categorical variable in both splits.
    - C) To speed up the splitting process.
    - D) To remove outliers before splitting.

12. **What does MLflow help with?**
    - A) Writing faster Python code.
    - B) Visualizing data in notebooks.
    - C) Tracking experiments, parameters, and metrics.
    - D) Cleaning messy datasets.

13. **Which of the following is a testable hypothesis?**
    - A) "The data is very interesting."
    - B) "We should collect more data next year."
    - C) "Increasing square footage is positively correlated with house price."
    - D) "Machine Learning is better than statistics."

14. **What is a 'Demographic Parity' in the context of fairness?**
    - A) Ensuring all locations have the same number of houses.
    - B) Ensuring the model predicts similar average outcomes across different groups.
    - C) Ensuring the model is 100% accurate for everyone.
    - D) Hiring a diverse team of data scientists.

## Advanced (6 Questions)
15. **If your model has high training accuracy but low test accuracy, what is likely happening?**
    - A) Underfitting
    - B) Overfitting
    - C) Data Leakage
    - D) The test set is too small.

16. **You calculate `price_per_sqft` on the entire dataset *before* splitting into train/test. Why is this a problem?**
    - A) It's not a problem; it's a good feature.
    - B) It causes data leakage because the target (`price`) is used to create the feature.
    - C) It makes the model too simple.
    - D) It violates the assumptions of Linear Regression.

17. **Which model is generally more interpretable: a single Decision Tree or a Random Forest?**
    - A) Decision Tree
    - B) Random Forest
    - C) Both are equally interpretable.
    - D) Neither is interpretable.

18. **In an ROI analysis, your model reduces RMSE from $30k to $15k. If you sell 100 houses, what is the 'Total Error Reduction'?**
    - A) $15,000
    - B) $1,500,000
    - C) $3,000,000
    - D) $45,000

19. **How would you handle a 'Temporal Split' in the house price dataset?**
    - A) Randomly shuffle and take the last 20%.
    - B) Split based on the `transaction_date` column.
    - C) Split based on the `year_built` column.
    - D) Use cross-validation.

20. **What is the risk of using 'proxy variables' for sensitive attributes?**
    - A) It makes the model less accurate.
    - B) It can lead to indirect discrimination even if the sensitive attribute is removed.
    - C) It increases the size of the dataset.
    - D) It requires more computational power.
