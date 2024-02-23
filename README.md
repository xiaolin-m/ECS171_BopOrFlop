# Bop or Flop
Welcome to Bop or Flop, a machine learning project created to determine if a song, based on its characteristics, will be a "bop" (popular) or "flop" (unpopular).

For this model we used a dataset from Kaggle that looked at 30000 Spotify songs and giving appropiate rankings of musical traits such as energy, instrumentalness, and most important, popularity.

Then, we built three classifier models to classify if songs were popular (popularity > 60) or unpopular.

Random forest was our best performing model, so it is used in our frontend interface.

## Running the Frontend Interface
To run the frontend interface, open the folder boporflop_frontend. In the terminal run <code>python app.py</code>. This should give you a local server that will be running our frontend interface, which is built through Flask. Once open, you should get an interface that looks like this:

![Frontend](https://i.imgur.com/ymRglZO.png)

Edit the 12 attributes to create your personal song. Then click on **Test My Song** to give it a try! Upon testing, you will get a result of BOP or FLOP!

## Running the Backend
We have two Jupyter notebooks that can be used to look at the backend code.

To look at the determination of our data analysis, look at <code>data_analysis.ipynb</code>.

To look at our data preprocessing and creation of our final models, look at <code>data_preprocessing_and_models.ipynb</code>.
