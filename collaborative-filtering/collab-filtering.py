#import library
#import the dataset
from recommendation_data import dataset
from math import sqrt


def similarity_score(person1,person2):

    # this Returns the ration euclidean distancen score of person 1 and 2

    # To get both rated items by person 1 and 2
    both_viewed = {}

    for item in dataset[person1]:
        if item in dataset[person2]:
            both_viewed[item] = 1
        
        # The Conditions to check if they both have common rating items
        if len(both_viewed) == 0:
            return 0

        # Finding Euclidean distance
        sum_of_eclidean_distance = []

        for item in dataset[person1]:
            if item in dataset[person2]:
                sum_of_eclidean_distance.append(pow(dataset[person1][item] - dataset[person2][item], 2))
        sum_of_eclidean_distance = sum(sum_of_eclidean_distance)
        
        return 1/(1+sqrt(sum_of_eclidean_distance))

def person_correlation(person1, person2):
    
    #we want to see correlation score person1 and person2 

   # To get both rated items
    both_rated = {}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item] = 1

    number_of_ratings = len(both_rated)

    # Checking for ratings in common
    if number_of_ratings == 0:
        return 0

    # Add up all the preferences of each user
    person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
    person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])

    # Sum up the squares of preferences of each user
    person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in both_rated])
    person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in both_rated])

    # Sum up the product value of both preferences for each item
    product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])

    # Calculate the pearson score
    numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
    denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))

    if denominator_value == 0:
        return 0
    else:
        r = numerator_value / denominator_value
        return r

def most_similar_users(person, number_of_users):

    # returns the number_of_users (similar persons) for a given specific person
    
    scores = [(person_correlation(person, other_person), other_person) for other_person in dataset if other_person != person]

    # Sort the similar persons so the highest scores person will appear at the first
    scores.sort()
    scores.reverse()
    
    for x in range(len(scores)):
        print(scores[x])
    #return scores[0:number_of_users]
        
def user_recommendations(person):

    # Gets recommendations for a person by using a weighted average of every other user's rankings
    
    totals = {}
    simSums = {}
    rankings_list =[]
    for other in dataset:
        # don't compare me to myself
        if other == person:
            continue
        sim = person_correlation(person,other)
        #print ">>>>>>>",sim

        # ignore scores of zero or lower
        if sim <=0: 
            continue
        for item in dataset[other]:

            # only score movies i haven't seen yet
            if item not in dataset[person] or dataset[person][item] == 0:

            # Similrity * score
                totals.setdefault(item,0)
                totals[item] += dataset[other][item]* sim
                # sum of similarities
                simSums.setdefault(item,0)
                simSums[item]+= sim

        # Create the normalized list

    rankings = [(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    # returns the recommended items
    recommendataions_list = [recommend_item for score,recommend_item in rankings]
    #return recommendataions_list,rankings
    #return rankings
    for x in range(len(rankings)):
        print(rankings[x])
    
        
print('')

# want to see recommendation movie for TioRL and the score.

print('User recommendation for username TioRL: ')
print('')
print(user_recommendations('TioRL'))
print('')

#want to see similar user with TioRL and after we know the similiar one, that person have similar movie tastes with me. The negative point means TioRL not similar to that person.

print('Similar user for username TioRL: ')
print('')
print(most_similar_users('TioRL',6))
print('')

#just want to check similarity score between TioRL and OM INDRA

print('Similarity score for TioRL and OM INDRA')
print('')
print(similarity_score('TioRL','OM INDRA'))
print('')