# Snowflake Case Study: Learning Journey from Mock Test to Data-Driven Guide

## Overview

This project is a case study built from a mock test I took during my Snowflake training. After scoring 47%, I decided to turn the explanatory HTML scorecard into a structured and searchable guide using Snowflake's data capabilities.

The goal was to transform failure into a learning resource by scraping the test data, organizing it into Snowflake tables, and building an interactive UI that helps understand Snowflake concepts across various domains.

## Objectives

- Extract meaningful data (domain, question, correct answer, explanation) from a local HTML mock test scorecard.
- Store the structured data in Snowflake as a centralized reference.
- Build an interactive UI to group and present content by domain, helping others review Snowflake topics in a guided format.

## Tech Stack

| Component           | Description                                       |
|---------------------|---------------------------------------------------|
| Python              | Used for HTML parsing and data extraction         |
| BeautifulSoup       | Library for scraping local HTML                   |
| Snowflake           | Cloud data platform to store structured data      |
| Streamlit / React + Flask | For building an interactive documentation viewer |
| Pandas (optional)   | To manipulate and optionally export data to CSV   |

## Data Structure

The extracted data is modeled with the following schema:

| Column          | Type   | Description                                  |
|------------------|--------|----------------------------------------------|
| DOMAIN           | String | Topic or section (e.g., Architecture)        |
| QUESTION         | String | The test question                            |
| CORRECT_ANSWER   | String | The correct answer as per the mock test      |
| EXPLANATION      | String | The rationale or concept behind the answer   |

## Core Steps

1. **Parse Local HTML File**  
   Use BeautifulSoup to scrape questions, answers, and explanations.

2. **Transform and Load**  
   Format the scraped data and load it into a Snowflake table using Python or a CSV loader.

3. **Visualize as Interactive Guide**  
   Create a UI grouped by domain where users can view and explore the Q&A with explanations.

## Outcome

This case study showcases how real learning gaps can be turned into technical artifacts. It also acts as a reusable reference for Snowflake concepts categorized by topic — useful for learners and teams alike.

## Future Enhancements

- Add tagging (e.g., difficulty levels)
- Include filtering and search in the UI
- Allow users to mark questions as understood
- Track improvement by comparing multiple mock test results

## Credits

This project is self-initiated as a part of personal Snowflake training and hands-on learning goals. All content is adapted and anonymized for educational purposes only.
