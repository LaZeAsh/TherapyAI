# TherapyAI
TherapyAI is an application that allows you to talk to a voice assistant about hard times and get help. TherapyAI uses Cohere's Natural Language Processing to figure out the nature of your text and then inform's our prompt of "bot is an emotion support Voice Assistant who wants to help the user feel better because user is {feelings}". After this we use Cohere's autogeneration to generate text for how we can respond to the user. This is a way to give the user someone to talk to in case they do not have the resources to consult with a therapist but still need advice.

### Getting Started

Macbook specific instructions
```bash
pip3 install virtualenv # install virtualenv if you haven't already

virtualenv env # Start a virtual environment
source env/bin/activate # Activate a virtual environment
pip install -r requirements.txt
python3 voice_recognition.py # To execute the voice recognition file to test
```