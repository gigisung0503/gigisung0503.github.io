---
title: "Automated Literature Review"
description: ""
author: "Gigi Sung"
date: "6/27/2024"
# draft: true
---

Yup. A literature review could be dragging and ineffective without systematic tools. This post will introduce a prompt that can help you automate the process of literature review.

*p.s. My neoliberal self told me to include LinkedIn post in the prompt. Feel free to remove it if you don't like it.*


### Automated Literature Review Prompt

**Prompt:**

```
You are tasked with performing an automated literature review. For each provided article, extract key insights, cite the exact source or wording from the article, and explain the relevance to the specified research project. Additionally, create a short, insightful LinkedIn post sharing insights from the given article.

#### Article Text:
[Insert article text here]

#### Research Project Description:
[Insert research project description here]

#### Key Insights:
1. **Insight 1**: [Extracted key insight]
   - **Citation**: [Exact wording or paragraph from the article]

2. **Insight 2**: [Extracted key insight]
   - **Citation**: [Exact wording or paragraph from the article]

3. **Insight 3**: [Extracted key insight]
   - **Citation**: [Exact wording or paragraph from the article]

#### Relevance to Research Project:
- **Relevance 1**: [Explanation of relevance of Insight 1 to the research project]
- **Relevance 2**: [Explanation of relevance of Insight 2 to the research project]
- **Relevance 3**: [Explanation of relevance of Insight 3 to the research project]

#### LinkedIn Post:
```

---

### Example Usage of the Prompt

```prompt
#### Article Text:

[Insert the full text of the provided article here]


#### Research Project Description:

Analyzing changes in human mobility due to the COVID-19 pandemic, focusing on travel behavior before and after the pandemic across different regions and socio-economic groups. 




#### Key Insights:
1. **Insight 1**: Increased use of urban green spaces in higher GDP regions during the COVID-19 pandemic.
   - **Citation**: "The GDP per capita of studied locations also played a role in the direction of changes in UGS use: locations with higher GDP per capita were more likely to experience an increase in UGS use than locations with a lower GDP per capita."

2. **Insight 2**: Stricter COVID-19 policies correlated with decreased use of public parks.
   - **Citation**: "The stringency of COVID-19 policies had a negative impact on UGS use during and after the first lockdowns... A weighted logistic regression revealed that locations reporting decreased use had significantly higher COVID-19 governance stringency."

3. **Insight 3**: Socio-economic disparities influenced the ability to adopt social distancing behaviors.
   - **Citation**: "Low-income and minority communities, facing cascading health challenges, are found to be least able to modify mobility behavior and therefore experienced a disproportionate burden of COVID-19 infection risk during the first wave of the pandemic."

#### Relevance to Research Project:
- **Relevance 1**: The finding that higher GDP regions saw increased use of green spaces aligns with the project's aim to analyze travel behavior changes based on socio-economic factors, highlighting how wealthier areas adapted differently.
- **Relevance 2**: The correlation between strict COVID-19 policies and decreased park use provides insight into how policy stringency influenced mobility, relevant for comparing regions with varying restrictions.
- **Relevance 3**: Understanding that socio-economic disparities impacted mobility behavior adoption is crucial for the project's focus on different socio-economic groups, emphasizing the need to consider inequality in behavioral responses.

#### LinkedIn Post:

🚶‍♂️🌳 **Urban Green Spaces and COVID-19: A Study on Usage Patterns and Socio-Economic Disparities** 🌳🚶‍♀️

A recent study highlights significant changes in the use of urban green spaces (UGS) during the COVID-19 pandemic. Key findings include:

1. **Higher GDP, Higher Usage**: Regions with higher GDP per capita saw increased use of UGS, emphasizing the role of economic conditions in adapting to the pandemic.
2. **Policy Impact**: Stricter COVID-19 policies were linked to decreased use of public parks, reflecting how governance stringency influenced outdoor activities.
3. **Socio-Economic Disparities**: Low-income and minority communities faced greater challenges in adopting social distancing behaviors, leading to higher infection risks.

These insights underscore the importance of considering economic and social factors in urban planning and public health strategies.

#UrbanPlanning #PublicHealth #COVID19 #Research #GreenSpaces #SocioEconomicFactors
```

---

This prompt can be reused for different articles by inserting the relevant text and adjusting the extracted insights, relevance, and LinkedIn post accordingly.