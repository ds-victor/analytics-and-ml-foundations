# Labeled vs Unlabeled Data

## 1. Why This Matters
Supervised learning requires labeled data. Getting labels is expensive – that's why unsupervised learning is valuable.

## 2. Core Concept
**Labeled data**: each example has a target value (e.g., house price). **Unlabeled data**: only features, no target. Labeling is the process of adding targets.

```mermaid
graph LR
    Raw[Unlabeled Data] --> Hum[Human Labeler/Expert]
    Hum --> Lab[Labeled Data]
    Lab --> Model[Supervised Model Training]
```

## 3. Real-World Examples
• Labeled: historical house sales with price, emails marked spam/not spam.
• Unlabeled: raw customer browsing logs, images without captions.

## 4. Comparison
| Aspect | Labeled | Unlabeled |
|--------|---------|-----------|
| Cost | High (human annotators) | Low (automatic collection) |
| Use | Supervised learning | Unsupervised, pre-training |
| Quality | Prone to human error | No ground truth |

## 5. Decision Tree
1. Have targets for prediction? → Use supervised learning (needs labeled).
2. No targets, want patterns? → Unsupervised (uses unlabeled).
3. Small labeled set + large unlabeled? → Semi-supervised learning.

## 6. Common Misconceptions
• Unlabeled data is not useless – it's used for pre-training (e.g., BERT).
• Active learning helps you choose what to label, reducing cost.

## 7. FAQ
**Q: Can I use unlabeled data to improve supervised models?** Yes, via self-supervised learning or pre-training.
**Q: How much labeled data do I need?** Depends on problem – hundreds to millions.

## 8. Next Steps
Now read about supervised vs unsupervised learning.

## 9. Running Example
Our house prices are **labeled** – we know the price (target). But imagine we also have 10,000 property listings without price – that's unlabeled data, which we could use for pre-training a feature extractor.

## 10. Interview Prep
1. Why is labeling expensive? Give an example.
2. What is semi-supervised learning?

