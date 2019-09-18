COLLABORATIVE-FILTERING-RECOMMENDATION
The idea of collaborative filtering is finding users in a community that share appreciations. If two users have same or almost same rated items in common, then they have similar taste. Such users build a group or a so-called neighborhood. A user gets recommendations for those items that user hasn’t rated before but was positively rated by users in his/her neighborhood.

Collaborative filtering has basically two approaches:

1. User Based Approach
In this approach, Items that are recommended to a user are based on an evaluation of items by users of the same neighborhood, with whom he/she shares common preferences. If the article was positively rated by the community, it will be recommended to the user. In the user-based approach, articles which are already rated by a user, play an important role in searching for a group that shares appreciations with him/her.
2. Item Based Approach
Referring to the fact that the taste of users remains constant or change very slightly, similar articles build neighborhoods based on appreciations of users. Afterwards, the system generates recommendations with articles in the neighborhood that a user might prefer.

ref: https://www.quora.com/What-is-the-difference-between-content-based-filtering-and-collaborative-filtering
--------------------------------------------------------------------------

code: collab-filtering.py
data: recommendation_data.py

to run the program type:

python collab-filtering.py

--------------------------------------------------------------------------

ref for the code: https://github.com/aryankashyap0/collaborative-filtering-python
