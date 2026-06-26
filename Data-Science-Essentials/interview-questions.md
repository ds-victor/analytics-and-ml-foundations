# Data Science Interview Questions - Comprehensive Pool

This pool contains 60+ questions to help you prepare for professional Data Science roles, covering the entire ML lifecycle.

---

## 1. Technical Vertical (20 Questions)

### Easy
1. **Feature Engineering:** What is the difference between One-Hot Encoding and Label Encoding?
2. **Exploration:** Why is a correlation matrix useful during the initial stages of a project?
3. **Metrics:** Explain 'Root Mean Squared Error (RMSE)' and why it is commonly used for house price prediction.
4. **Git:** What is the purpose of a `.gitignore` file in a data science project?
5. **Python:** What is a 'List Comprehension' and why might you use it?
6. **IDE:** Why should you avoid using hardcoded absolute paths in your scripts?

### Medium
7. **Feature Engineering:** Explain how you would handle a high-cardinality categorical feature like 'Zip Code'.
8. **Experiment Tracking:** Why is it important to log hyperparameters (like `learning_rate`) and metrics (like `MAE`) in a tool like MLflow?
9. **Model Selection:** How do you choose between a Linear Regression and a Random Forest Regressor for a new dataset?
10. **Fairness:** What is the difference between 'Demographic Parity' and 'Equal Opportunity' in ML ethics?
11. **Data Leakage:** Explain how calculating the mean of a feature on the entire dataset (before splitting) causes leakage.
12. **Reproducibility:** Why is setting a random seed important for model training and evaluation?
13. **Pipelines:** What are the advantages of using a Scikit-Learn `Pipeline` object?
14. **Cross-Validation:** When would you choose 'Stratified K-fold' over standard K-fold cross-validation?

### Difficult
15. **Advanced Feature Engineering:** Explain the concept of 'Target Encoding' and its primary risks.
16. **Model Evaluation:** For a regression problem, why is it critical to analyze the distribution of residuals?
17. **Optimization:** How does 'Gradient Boosting' differ from 'Bagging' (Random Forest)?
18. **Fairness Detection:** Walk through the technical process of performing a 'Fairness Audit' on a deployed model.
19. **Architecture:** Describe how you would design a system to detect and handle 'Concept Drift' in production.
20. **Math:** Explain the role of the 'Kernel Trick' in Support Vector Machines (SVM).

---

## 2. Situational Vertical (20 Questions)

### Easy
21. A stakeholder asks for a price prediction for a property but the model hasn't been trained on that specific city yet. What do you do?
22. You discover a typo in the dataset after you've already started training. How do you proceed?
23. A manager wants you to use a complex Neural Network for a very simple problem. How do you handle it?
24. You find that your code runs 10x slower on the production server than on your laptop. What are your first steps?
25. A stakeholder asks for a "quick and dirty" analysis. How do you ensure it's still accurate?
26. You are asked to present to a non-technical audience. How do you simplify your visuals?

### Medium
27. You find that 30% of the values in your target variable (`price`) are missing. How does this change your project plan?
28. After deploying your model, the performance drops significantly after 6 months. What is your process for diagnosing the issue?
29. A domain expert (e.g., a real estate agent) says your model's most important feature "is irrelevant in the real world." How do you respond?
30. You have a choice between a 95% accurate 'black box' model and a 90% accurate interpretable model. Which do you recommend?
31. Your project budget is cut, and you can no longer use the paid experiment tracking tool. How do you adapt?
32. You are asked to build a model with data that you believe is inherently biased. What is your ethical and technical approach?
33. A stakeholder asks for a single number prediction, but your model shows a high degree of uncertainty. How do you communicate this?

### Difficult
34. You discovered a critical bug in the feature engineering pipeline of a model that has been in production for a year. How do you handle the fallout?
35. You have been asked to build a 'fair' model, but you discover that removing protected attributes (like race) actually decreases accuracy significantly. How do you navigate this trade-off?
36. You need to migrate a legacy ML pipeline from one cloud provider to another. What are your top 3 technical priorities?
37. You found that a 'proxy variable' is introducing bias into your model even though the sensitive attribute is removed. How do you technical identify and remove it?
38. Your model predictions are being used for high-stakes decisions (e.g., mortgage approvals). How do you design an 'Audit Trail' for every prediction?
39. You have been given a dataset with 1,000 features and only 5,000 rows. What is your strategy for feature selection and model training?
40. A stakeholder wants to know the "return on investment" of your model vs. the previous manual process. How do you calculate and present this?

---

## 3. Behavioural Vertical (20 Questions)

### Easy
41. Tell me about a data science project you are passionate about.
42. How do you manage your time when you have multiple datasets to clean?
43. Describe a time you worked on a team with different skill levels.
44. Why did you choose Data Science as a career path?
45. What is your favorite Python library for data science and why?
46. How do you handle being stuck on a difficult coding problem?

### Medium
47. Tell me about a time you identified an error in your own analysis after presenting it.
48. Describe a situation where you had to persuade a stakeholder to invest in better data infrastructure.
49. Give an example of a time you received critical feedback on your model's performance. How did you handle it?
50. Tell me about a time you had a disagreement with a developer about how to deploy a model.
51. Describe a time you had to learn a complex new domain (like real estate or finance) for a project.
52. How do you balance technical excellence with the need for speed in a fast-paced environment?
53. Describe a time you went above and beyond to ensure a model was ethically sound.

### Difficult
54. Tell me about a time you had to make a decision that went against the popular opinion in your team.
55. Describe a situation where you had to lead a data science initiative with no clear goal from the start.
56. Tell me about a time you disagreed with your manager's technical approach to a problem.
57. What is the most complex ML lifecycle problem you've ever managed (from framing to deployment)?
58. Describe a time you discovered a major ethical concern in a project you were working on.
59. How do you handle a situation where a stakeholder is pressuring you to produce results that support their preconceived conclusions?
60. Where do you think the responsibility of a Data Scientist ends and the responsibility of the business begins?
