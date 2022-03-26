# Movie Recommendation System based on Content Similarity

A recommendation system (or engine) is a filtering system which aim is to predict a  preference a user would give to an item, eg. title etc.

For our project, we choose content-based

This program is a prototype of a content-based movie recommendation system. This method relies on Natural Language processing to find correlation in movies based on their features like title,genre, actor, director,keywords etc. All these features are extracted from the textual data which is cleaned and pre-processed for modeling. The vectors of words corresponding to each movie are input to the cosine similarity function. Cosine similarity is applied to find how close two sentences (converted to vectors) are. The above operation results in cosine values of each movie w.r.t to ever other movie. Higher the cosine value between two movies, more is the similarity between the movies.

# Snapshot

![image](https://user-images.githubusercontent.com/84611644/159121246-baf0e728-e681-4426-af6a-6e5546d54040.png)
