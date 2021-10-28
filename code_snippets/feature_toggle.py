# check in which group of A/B testing the user is
user_in_treatment = feature_enabled("my_experiment_001") 

# this is the feature flag control path
if user_in_treatment:
    return experimental_functionality()
else:
    return existing_functionality()
