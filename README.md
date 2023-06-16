# ML-Bangkit-Capstone-Project-Nongki-C23PR513
A Repository containing the Machine Learning (ML) section of Bangkit 2023 Capstone Project by Group C23-PR513. Other parts of this project can be accessed through [this link](https://github.com/argadewanata/C23-PR513_Mid-Checkpoint).  

## Title of Capsone Project 
Nongki

## Abstract
In Indonesia, people face difficulties finding the perfect hangout spot that matches their needs. This leads to frustration, wasted time, and money by visiting the places that do not match their preferences. Our project addresses this by developing a mobile app with a plethora of hangout spots database. It provides detailed information, reviews, and personalized recommendations based on user preferences, budget, and location. Traditional search engines and review sites can be unreliable, while our app offers accurate suggestions, promoting hidden gems and supporting local businesses. Users can break the monotony of visiting the same places and discover new options. With our app, they can save time researching but instead get tailored recommendations based on their characteristics. By leveraging user preferences and dietary needs, our app ensures relevant suggestions and helps boost exposure and sales for hangout spots.

## Author
Created and developed by the Machine Learning Cohort of Google Bangkit 2023, with the following profiles:
Bangkit ID  | Full Name                       |                
----------- | ------------------------------- |               
M038DSX1765 | Muhammad Azka Bintang Pramudya  | 
M040DSY0555 | Shahnaz Salsabila Ishak         |
M038DSX0370 | Rere Arga Dewanata              |

## Related Link to Our Project
1. [Slide presentation link](https://www.canva.com/design/DAFlzSyG0OM/UzO5bba6TuWcpynpdTvZGg/edit?utm_content=DAFlzSyG0OM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
2. [Video Presentation](https://youtu.be/SKhmMks5kag)
3. [Project Brief](https://docs.google.com/document/d/1WBYCNjmgmEvCtbIrnKq-Q-XFo5L7woNx/edit?usp=sharing&ouid=113117300709765044885&rtpof=true&sd=true)
4. [Demo Apps](https://drive.google.com/file/d/1b7-apcgAvGetBgnD-sEjVhCUBSs2-vAa/view?usp=sharing)

# Overall Development Flow 
1. [Gathering hangout spot data details from Google Maps API](#gathering-hangout-spot-data-details-from-google-maps-api)  
2. [Gathering all the spot features and reviews from Google Maps](#gathering-all-the-spot-features-and-reviews-from-google-maps)  
3. [Formatting all the data using pandas](#formatting-all-the-data-using-pandas)  
4. [Building a new machine learning model using indobert transfer learning](#building-a-new-machine-learning-model-using-indobert-transfer-learning)  
5. [Predicting the review sentiment with that model](#predicting-the-review-sentiment-with-that-model) 
6. [Building a recommender system using TF-IDF with cosine similarity](#building-a-recommender-system-using-tf-idf-with-cosine-similarity)
7. [Adding all the processed data to the database](#adding-all-the-processed-data-to-the-database)

# Further Explanation
## Gathering hangout spot data details from Google Maps API
For this capstone project, we have developed a Minimal Viable Product (MVP). Currently, we have gathered data for places located in Yogyakarta, specifically three types of places: cafes, restaurants, and bars. To obtain this data, we utilized the [Google Maps API](https://developers.google.com/maps/documentation/places/web-service/details). Through the provided link, we learned that the API offers multiple ways to retrieve the desired response. Our cloud computing team provided us with the necessary API_KEY for this purpose. 

To fetch the response, we developed a Python program, and the final version can be found in this file: [GetJSONfromOneCityv1.py](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/GetData/GetJSONfromAPI/GetJSONfromOneCityV1.py). Using this code, we fetched all possible places within a 50km radius of Yogyakarta based on a pinpoint query. After each iteration, we shifted the pinpoint location to ensure we obtained a broader range of places that align with our project requirements.

Once we obtained the potential places, we made subsequent requests to gather detailed information such as name, formatted phone number, formatted address, opening hours, rating, and more. The results were appended and stored in a JSON file named [1City_v1_all_fields.json](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/GetData/JSON_Response/1City_v1_all_fields.json).

## Gathering all the spot features and reviews from Google Maps 
For this project, one of our objective is to conduct sentiment analysis on place reviews in order to determine the sentiment associated with each place. While we initially obtained reviews from the API response, we realized that the limited number of reviews (only five) was insufficient for our needs. To overcome this limitation, we use [this scraping python notebook](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/GetData/Scrapping/Kode/Review%20scrap.ipynb) for additional reviews on Google Maps and added them to our database. By adopting this approach, we were able to gather a larger volume of reviews, which greatly assisted us in developing an effective yet precise sentiment analysis system.

## Formatting all the data using pandas
To ensure the accuracy of our sentiment analysis, we follow a formatting step to enhance the data and optimize the results. The initial data is in JSON format, which we load and convert into a pandas dataframe. By transforming the data into a dataframe, we gain the ability to easily manipulate the information. This includes creating new columns, duplicating dataframes, merging data, and more. In this [Python notebook file](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Data%20Cleaning/Revision%202/Cleaning_data_03_revised.ipynb), we perform necessary manipulations on the dataframe to align it with our requirements, and subsequently export it to separate CSV files. From this previous [JSON file](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/GetData/JSON_Response/1City_v1_all_fields.json), we get [Places.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Database/CSV/Places.csv), [types.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Database/CSV/types.csv), and [OperationHours.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Database/CSV/OperationHours.csv).

## Building a new machine learning model using indobert transfer learning
Once we have obtained the [Review.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/cleaned.csv) dataset, our next step is to build a sentiment analysis model based on the reviews provided. Prior to conducting the analysis, we will first clean the text reviews using regular expressions to eliminate numbers, single characters, multiple whitespaces, and special characters. Furthermore, we will utilize [this](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/new_kamusalay.csv) resource to standardize all Indonesian slang words into a uniform format. Additionally, we will employ [this](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/stopwordbahasa.csv) dataset to remove any stopwords that may affect the analysis process.

Once the data has been cleaned and prepared, we proceed to build a model using transfer learning from an existing Indobert. We split the data into train and test. In addition to the pre-trained layers, we incorporate five additional layers into the model. The model summary can be viewed   
![Model_Summary](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/78808a90-bcef-45b3-b651-69b330097095)  

The model then trained for four epochs with a batch size of 30, and the process is time-efficient. The model loss and accuracy graphs are shown below  
![Model_Loss](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/4f2091f1-b90e-4438-98f2-c512b8adf93f)  
![Model_Accuracy](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/bbf51ffc-b2a4-4251-8012-fc37703d8e30)    

Moving on to the model evaluation metrics: 
The recall is 0.84  
The precision is 1.00  
The accuracy is 0.84  
The F1 measure is 0.91    

Following the evaluation, we save the model as an .h5 file.   
For a more detailed overview of the process, you can refer to this [sentiment_analysis_python_notebook](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/SentimentAnalysis.ipynb)

## Predicting the review sentiment with that model
After the model has been created, we predict all the review datas and get all the sentiments.

## Building a recommender system using TF-IDF with cosine similarity
Once we have collected all the review sentiments, our next step is to develop a recommender system using the Term Frequency - Inverse Document Frequency (TF-IDF) algorithm. TF-IDF is a powerful technique that utilizes word frequency to determine the relevance of words within a document. To illustrate, refer to the example, which showcases the calculation of TF-IDF scores.

![Example_TFIDF](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/6fe55b0d-19f9-485b-8ae4-d2c3354990b8)

By employing this table, we can determine the similarity between the characteristics of different places. Leveraging this information, we can recommend places that share similar characteristics based on the user's wishlist. This approach enhances the accuracy of our recommendations and improves the overall user experience.

## Adding all the processed data to the database  
After all the data has been processed, we will store all the data in MySQL. This is the MySQL Physical Data Model (PDM).
![PDM_Capstone_Project_Bangkit](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/82fa5503-355f-49d4-8a4d-45daa958da04)  

To create table, we're using this [SQL Statement](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Database/SQL/CreateTable.sql).  
To store that, we convert all existing csv to sql using [all of this python script](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/tree/main/Database/PythonCSVConverterToSQL).   
With this script, we will get [all of this mySQL Statement](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/tree/main/Database/SQL) so we can input to the data easier
