# Whatsapp Analyzer project

## Description
A Python-based web app that analyzes exported WhatsApp chats to extract meaningful insights about user activity, word usage, emoji frequency, and message patterns. Built using Streamlit for the UI and Docker for easy deployment and portability, it provides users with intuitive charts and statistics from raw .txt chat data.

## Learnings:
* Through this project, I gained practical experience in working with unstructured text data and handling real-world edge cases in exported chat formats.
* I also learned how to use pandas for data manipulation, matplotlib/seaborn for visualization, and how to build and deploy data apps using Streamlit and Docker.

## Challenges:
* One of the main challenges was parsing and standardizing the inconsistent structure of exported WhatsApp messages, especially with different timestamp formats.
* Ensuring that the app handled both 12h and 24h timestamp formats robustly required careful debugging and optimization.


## Running the project
To run this directly from Docker run the following code in your terminal

`start docker`

`docker pull anuraggc15/whatsapp_analyzer:v1`

`docker run -p 80:80 anuraggc15/whatsapp_analyzer:v1`

On running it you will get a code to run this app in your local machine and it will look something like this

![Greeting Screen](img.png)

After uploading an exported chat and clicking on **Show Analysis** , you can observe and analyze the chats.

## Further developments to be made

> 1. Better graphs with time series analysis
> 2. Better stopword support
> 3. Sentiment analysis
