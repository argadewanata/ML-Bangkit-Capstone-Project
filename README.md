# ML-Bangkit-Capstone-Project-Nongki-C23PR513
A Repository containing the Machine Learning (ML) section of Bangkit 2023 Capstone Project by Group C23-PR513. Other parts of this project can be accessed through [this link](https://github.com/argadewanata/C23-PR513_Mid-Checkpoint)

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

# Overall Development Flow 
1. [Gathering hangout spot data details from Google Maps API](#gathering-hangout-spot-data-details-from-google-maps-api)  
2. [Gathering all the spot features and reviews from Google Maps](#gathering-all-the-spot-features-and-reviews-from-google-maps)  
3. [Formatting all the data using pandas](#formatting-all-the-data-using-pandas)  
4. [Building a new machine learning model using indobert transfer learning](#building-a-new-machine-learning-model-using-indobert-transfer-learning)  
5. Predicting the review sentiment with that model  
6. Building a recommender system using TF-IDF with cosine similarity
7. Adding all the processed data to the database

# Further Explanation
## Gathering hangout spot data details from Google Maps API
For this capstone project, we have developed a Minimal Viable Product (MVP). Currently, we have gathered data for places located in Yogyakarta, specifically three types of places: cafes, restaurants, and bars. To obtain this data, we utilized the [Google Maps API](https://developers.google.com/maps/documentation/places/web-service/details). Through the provided link, we learned that the API offers multiple ways to retrieve the desired response. Our cloud computing team provided us with the necessary API_KEY for this purpose. 

To fetch the response, we developed a Python program, and the final version can be found in this file: [GetJSONfromOneCityv1.py](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/GetData/GetJSONfromAPI/GetJSONfromOneCityV1.py). Using this code, we fetched all possible places within a 50km radius of Yogyakarta based on a pinpoint query. After each iteration, we shifted the pinpoint location to ensure we obtained a broader range of places that align with our project requirements.

Once we obtained the potential places, we made subsequent requests to gather detailed information such as name, formatted phone number, formatted address, opening hours, rating, and more. The results were appended and stored in a JSON file named [1City_v1_all_fields.json](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/GetData/JSON_Response/1City_v1_all_fields.json).

## Gathering all the spot features and reviews from Google Maps 
For this project, one of our objective is to conduct sentiment analysis on place reviews in order to determine the sentiment associated with each place. While we initially obtained reviews from the API response, we realized that the limited number of reviews (only five) was insufficient for our needs. To overcome this limitation, we use data scraping for additional reviews on Google Maps and added them to our database. By adopting this approach, we were able to gather a larger volume of reviews, which greatly assisted us in developing an effective yet precise sentiment analysis system.

## Formatting all the data using pandas
To ensure the accuracy of our sentiment analysis, we follow a formatting step to enhance the data and optimize the results. The initial data is in JSON format, which we load and convert into a pandas dataframe. By transforming the data into a dataframe, we gain the ability to easily manipulate the information. This includes creating new columns, duplicating dataframes, merging data, and more. In this [Python notebook file](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Data%20Cleaning/Revision%202/Cleaning_data_03_revised.ipynb), we perform necessary manipulations on the dataframe to align it with our requirements, and subsequently export it to separate CSV files. From this previous [JSON file](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/GetData/JSON_Response/1City_v1_all_fields.json), we get [Places.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Database/CSV/Places.csv), [types.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Database/CSV/types.csv), and [OperationHours.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Database/CSV/OperationHours.csv).

## Building a new machine learning model using indobert transfer learning
Once we have obtained the [Review.csv](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/cleaned.csv) dataset, our next step is to build a sentiment analysis model based on the reviews provided. Prior to conducting the analysis, we will first clean the text reviews using regular expressions to eliminate numbers, single characters, multiple whitespaces, and special characters. Furthermore, we will utilize [this](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/new_kamusalay.csv) resource to standardize all Indonesian slang words into a uniform format. Additionally, we will employ [this](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/stopwordbahasa.csv) dataset to remove any stopwords that may affect the analysis process.

Once the data has been cleaned and prepared, we proceed to build a model using transfer learning from an existing Indobert. In addition to the pre-trained layers, we incorporate five additional layers into the model. The model summary can be viewed   
![Model_Summary](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/78808a90-bcef-45b3-b651-69b330097095)  
For model compilation, we utilize BinaryCrossentropy as it proves highly effective for classifying binary tasks such as this project. The model is then trained for four epochs with a batch size of 30, and the process is time-efficient. The model loss and accuracy graphs are shown below
![Model_Loss](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/4f2091f1-b90e-4438-98f2-c512b8adf93f)
![Model_Accuracy](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/assets/70679432/bbf51ffc-b2a4-4251-8012-fc37703d8e30)  

Moving on to the model evaluation metrics: 
The recall is 0.84  
The precision is 1.00  
The accuracy is 0.84  
The F1 measure is 0.91    

Following the evaluation, we save the model as an .h5 file.   
For a more detailed overview of the process, you can refer to the [sentiment_analysis_python_notebook](https://github.com/argadewanata/ML-Bangkit-Capstone-Project/blob/main/Sentiment%20Analysis/SentimentAnalysis.ipynb)



