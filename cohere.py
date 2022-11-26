import cohere
from cohere.classify import Example
co = cohere.Client('')
# all example scenarios
# examples = [
#     Example("I feel very sad", "negative"),
#     Example("I am happy", "positive"),
#     Example(),
#     Example(),
#     Example(),
#     Example()
# ]

# will get from the speech recognition
inputs = [

]

# judging our responses
response = co.classify(
    model = 'medium',
    inputs = inputs,
    examples = examples
)

print(response.classifications)
