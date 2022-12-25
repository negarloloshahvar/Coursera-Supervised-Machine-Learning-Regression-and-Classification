# Week 2: Regression with Multiple Input Variables

## Feature Scaling

* Three different techniques:

- 1. Feature scaling, essentially dividing each positive feature by its maximum value, or more generally, rescale each feature by both its minimum and maximum values using (x-min)/(max-min). Both ways normalizes features to the range of -1 and 1, where the former method works for positive features which is simple and serves well for the lecture's example, and the latter method works for any features.

- 2. Mean normalization:  𝑥𝑖:=𝑥𝑖−𝜇𝑖 / 𝑚𝑎𝑥−𝑚𝑖𝑛

- 3. Z-score normalization 𝑥𝑖:=𝑥𝑖−𝜇𝑖 / sigma
