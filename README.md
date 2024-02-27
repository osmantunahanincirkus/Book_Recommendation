# book_recommendation
Book Recommendation Site develop with Sentiment Analysis using Node.js and Vue.js

## SUMMARY

In this project, the design and implementation of a system to provide personalized book recommendations and perform emotional analysis of book comments were examined in detail. In particular, two key components were focused on: the user-based collaborative filtering algorithm and sentiment analysis.

First of all, users' evaluations of their books were analyzed with the user-based collaborative filtering algorithm, and based on these evaluations, special book recommendations were offered to users with similar tastes. With this approach, each user's unique preferences were taken into account, thus personalizing and enriching the user experience.

Secondly, book reviews were analyzed with the sentiment analysis algorithm and it was determined whether these comments were positive or negative. This is important to determine readers' overall perception of the book and helps users make informed book choices.

The implementation of these two algorithms was carried out using modern web technologies. Node.js was used for backend operations, Vue.js for frontend operations and Flask API was used for integration of the sentiment analysis model.

As a result, this project introduced an innovative system that personalizes and enriches the user experience, while also helping users make informed book choices. This project also provided a comprehensive evaluation and analysis of practical applications of sentiment analysis and collaborative filtering. This system helps book lovers and publishers better understand readers' book preferences and emotional reactions and further personalize their services.

## LITERATURE

### Recommendation Systems

Recommendation systems examine user interactions and habits by dividing them into two different categories: overt and covert activities. While overt activities take into account the actions users take on a particular platform (comments, ratings, etc.), latent activities focus on how much time the user spends on the platform and what actions they have taken in the past.

Recommendation systems are divided into three types depending on the strategies used: collaborative filtering, content-based filtering, and hybrid filtering, where these two strategies are combined. These systems aim to provide users with the most accurate and relevant recommendations. User tastes are based either on information received directly from users or inferred from their viewing behavior. This not only increases user appreciation, but also serves the platforms' goals of expanding their user base and increasing their profits. In this project, the User-Based Collaborative Filtering method, one of the Collaborative Filtering methods, was used.

#### User-Based Collaborative Filtering

First, let's briefly explain collaborative filtering. Collaborative filtering is a recommendation system that aims to provide recommendations by evaluating interactions between users and products. In general, it analyzes the interactions of users with similar preferences or products with similar features on each other. As a result of this analysis, users' possible ratings for a particular product or service are predicted and recommendations are made accordingly.

User-Based Collaborative Filtering (UBCF) is a recommendation system that aims to create personalized recommendations based on preference similarities between users. This method allows users with similar behaviors and interests to benefit from each other's choices and preferences.

The basis of UBCF is based on recommending to an active user products that other users who have similar preferences have previously liked. In other words, the system estimates the liking of a product that a user has not yet experienced or purchased, based on the evaluations of other users who are similar to it.

#### Sentiment Analysis

Sentiment Analysis is an approach, a study, that detects emotions on comments and text-based documents in which people express their opinions and ideas. Sentiment analysis is a field of study that evaluates people's emotions and opinions and analyzes their behavior on a subject through written language (Liu, 2012).

Sentiment Analysis, like every other field of work, has a functioning and process. Each step in this process is of great importance in itself, and in order for Sentiment Analysis to give an accurate result, these steps must be processed completely and with the same importance. Sentiment Analysis Process; It consists of 5 steps: Data Set Creation, Data Preprocessing, Target Term Extraction, Target Term Category Finding and Target Term Sentiment Classification. In some of these steps, several methods and algorithms are used.

In this study, the "turkish_product_reviews" dataset from Hugging Face was used as the dataset to train our Sentiment Analysis model. Pre-processing operations were carried out on the data in our dataset with the NLTK Library. An attempt was made to complete the data pre-processing step by applying tokenization, stop words and stemming operations respectively on the comments in our "sentence" column in our data set. Target Term Extraction was carried out with the TF-IDF Method.

## HOW TO DOWNLOAD AND RUN THE PROJECT

### Requirements
1. *Docker* and *Docker Compose* should be installed.
2. *Node.js* is required to run the project.

### Steps

#### 1. Clone the Project
- Open the terminal and navigate to the directory where you want to clone the project.
- Clone the project:
  ```bash
  git clone <project_git_url>
  cd <project_folder_name>
  ```
#### 2. Run the Project with Docker
Navigate to the root directory of the project in the terminal.
Start the project using Docker Compose:
```bash
docker-compose up
```
#### 3. Set Up the Node.js Environment
To run the Vue.js client, go to the vue-client directory and perform the necessary steps in the terminal:

```bash
cd vue-client
npm install
npm run serve
```
#### 4. Set Up the API and Server Side
To start the Express.js API, execute the necessary steps in the terminal:
```bash
# Navigate back to the main directory
cd ../
# Start the API
npm install
npm start
```
#### 5. Database
We've started the MySQL database via Docker. If you need to modify any settings, you can edit the environment variables in the docker-compose.yml file.
### 6. Accessing the Project
   Access the project in a web browser at http://localhost:9777. The Vue.js client runs on this port.

### Note
DataSets used in this project, you can access it from here: https://github.com/IsmailCanMutlu/Deps

## RESULT

In this project, an innovative system was designed and implemented to improve readers' digital book discovery experiences. Our work focused on the integration of user-based collaborative filtering and sentiment analysis algorithms. Both a recommendation system that provides personalized book recommendations through a user-based collaborative filtering algorithm and a system that analyzes the emotional tone of book reviews using sentiment analysis were designed and implemented.

With the recommendation system created with a user-based collaborative filtering algorithm, readers were offered a personalized book discovery experience. By analyzing users' previous book reviews, unique and customized book recommendations were provided to each reader. This allowed the selection of books to be personalized and readers to receive recommendations based on their interests and tastes.

By using the sentiment analysis algorithm, a better understanding of what readers think about a book was achieved. By analyzing the emotional tone of book reviews, readers were provided with valuable insight into the overall perception of a book. However, it helps readers learn more about general reviews of a book and thus make a more informed choice.

Using modern web technologies, these algorithms are integrated into a website. An effective and user-friendly website was created using Node.js and Vue.js. Our sentiment analysis model was successfully integrated into the system using the Flask API.

As a result, with our study, readers were provided with personalized book recommendations, and an effective and user-friendly system was designed and implemented to analyze the emotional tone of book reviews using sentiment analysis. With this system, the book discovery experience in the digital age has been enriched and also helped readers make more informed book choices. This thesis also provided a valuable perspective on the methodologies and technologies used in designing and implementing such systems.

## Contribution

This project was developed by two people.

- [@osmantunahanincirkus](https://github.com/osmantunahanincirkus)
- [@IsmailCanMutlu](https://github.com/IsmailCanMutlu)

## License

[MIT License](LICENSE)
