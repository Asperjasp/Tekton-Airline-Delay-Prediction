In this project called **`Data Engineering Project Proposal: Airline Delay Prediction`** I would like to highlight on the importance of questioning the why behind its action, as a work ethic in the Tekton Development Principles which include but are not limited to asking 

- Why are we talking and selling like we do ?
- Who are the customers and what are their cultures ? how does relates to us ?

Asking proper questions to answer the why behind each product, ensuring the maximum quality possible, and not building project combining fancy words like: 

- Building a Facebook but for people who play golf or are into wine.
- Clone of Twitter but shinny.

Allowing to build things that provide as much value as possible and are worth the effort , specifically from LATAM, because it is possible to do great in business and consequently to believe it ourselves ad Latin Americans and not let other people that come from Israel or Europe achieve the succeed we could have achieved on our own due to the mindset difference, we are equally or more capable.

## **Data Engineering Project Proposal: Airline Delay Prediction Pipeline on GCP**

**I will develop a project in the area of Airline Data analytics , which has the following principles
Build a robust, scalable `ETL Pipeline` on `Google Cloud Platform (GCP)` using `Python` and `Airflow` to ingest publicly available airline operational data, store it efficiently in `BigQuery`, and apply a basic `Machine Learning model` (using Python) to predict flight delays, with results visualized in a tool like `Tableau` o `Power BI`. The final output should demonstrate mastery of the required tools and provide a clear, business-relevant insight for an airline client.**

For this I provide the source code in the following repository :

https://github.com/Asperjasp/Tekton-Airline-Delay-Prediction

And the **`source database`** which comes form a data set in **`kaggle`** 

https://www.kaggle.com/datasets/giovamata/airlinedelaycauses/data

**This is perfect because it aligns with the job proposals following goals such as :**

| **Role Requirement** | **Project Component (Project)** |
| --- | --- |
| GCP, BigQuery, SQL | Design and create a Data Warehouse schema in BigQuery; write optimized SQL for data transformation. |
| Python | Write the ETL scripts (Extract/Transform/Load) and the Machine Learning model script. |
| ETL Processes, Airflow | Build a scheduled workflow (DAG) in Apache Airflow (using Google Cloud Composer on GCP) to automate the entire pipeline. |
| MongoDB familiarity | Simulate or use a NoSQL source (e.g., an API output that resembles a JSON document) and load it into a service like Cloud Firestore or just parse the JSON/dict in Python to showcase understanding of non-relational data extraction. |
| Data Analyst/Visualization | Create a dashboard in Power BI/Tableau to visualize the delay predictions and key performance indicators (KPIs). |
| Documenting (Confluence) & Tracking (Jira) | Structure your GitHub repository with clear documentation (README.md, data dictionary) and map out the project phases using a simple task tracker (like a Notion board or a simplified Jira/Confluence simulation in your repo). |

****In order to build this project and adapt it so that it follows the my principles I use to deliver high quality results, delegate and prioritize tasks to achieve results `on-time` ****I will out-line the requirements in my **`Notion Project Management System`** which include

- **`Objectives` :**  Long term Goals, the high relevance, and importance result which usually last about 1-week or longer
- **`Projects` :** Subcategory of Objectives which include the main components and deliverables needed to achieve the **`goal`** that can be completed in the range of 1 - 6 days
- **`Tasks` :**  Immediate , short, focused **`actions`** which contribute the most little piece of work needed to accomplish a **`project`** in a definitive **`calendar-block time`** of around **`1 - 8 hours`**

## `Objective`

Successful deployment of an end-to-end Flight Delay Prediction ETL Pipeline on GCP using Airflow, Python, and BigQuery.

### **`⚙️ Project 1: Data Ingestion and Storage (Focus: Python, APIs, MongoDB, BigQuery Schema)**`

- **Task 1.1:** Research and select a public airline dataset (e.g., U.S. DOT's Bureau of Transportation Statistics, Open Flights, or even a smaller, simple simulated dataset for proof-of-concept). **(Target: 1 hr)**

For this  i identified two datasets, but we will proceed with the one with a more robust documentation it being  the following

https://www.kaggle.com/datasets/giovamata/airlinedelaycauses/data

For working with the data in the Kaggle Dataset we strongly advise to use **`Kaggle CLI`** to download the data locally in the **`01_raw_data` folder** according to the **`/Docs/Data.md`** documentation

- **Task 1.2:** Write a **Python** script to **extract** data (simulating an API call or reading a local file) and a separate script to process a small, structured JSON file (simulating **MongoDB** data like flight gate assignments) to demonstrate multi-source extraction. **(Target: 3 days)**
- **Task 1.3:** Design the **BigQuery** data warehouse schema (Staging, Dimension, and Fact tables) for the airline data. Use `CREATE TABLE` and `INSERT` statements to load initial data. **(Target: 3 days)**

### `🛠️ **Project 2: ETL Logic and Orchestration (Focus: SQL, Airflow, GCP)**`

- **Task 2.1:** Develop the core **SQL transformation logic** in BigQuery to clean data, perform joins, aggregate key metrics (e.g., average delay by origin airport), and create the final modeling table. **(Target: 3 days)**
- **Task 2.2:** Write a simple Python script for a **basic ML classification model** (e.g., Logistic Regression or a Decision Tree using `scikit-learn`) to predict if a flight will be *Delayed* (Binary: Yes/No). **(Target: 3 days)**
- **Task 2.3:** Set up a basic **Apache Airflow** (or Google Cloud Composer) environment and create a **DAG** (Directed Acyclic Graph) in Python that orchestrates: **Extract → Transform (SQL) → Load → ML Prediction.** **(Target: 3 days)**

### `📊 **Project 3: Deliverables and Presentation (Focus: Documentation, Visualization, Professionalism)**`

- **Task 3.1:** Create a **Tableau/Power BI dashboard** visualizing the ML model's prediction accuracy, the top 5 predicted delay routes, and operational KPIs (average departure delay, cancellation rates) from Big Query. **(Target: 2 days)**
- **Task 3.2:** Finalize the project on **GitLab/GitHub** with a professional `README.md` that serves as your **Confluence** documentation (detailing architecture, data model, technology stack) and use your **Notion** tracker to show the **Jira** like task management. **(Target: 2 days)**
- **Task 3.3:** Prepare a concise, compelling 5-minute presentation explaining the business value and the engineering decisions behind your project. **(Target: 2 days)**

That would be all. Thank you very much for your time and I hope that we work and create something meaningful together, let me know what you think you loved about the project in the repo, and the value proposition to **`TekTon Labs.`**

Success

Alejandro Sánchez Poveda

alesanchezpov@gmail.com