1. Write stories: stories.md 
2. Determine domain of bot: domain.yml
3. Train dialogue model using anaconda prompt(make sure to go to folder)(creates dialogue folder): python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
4. Test trained bot(make sure to use unstructured data "/greet"): python -m rasa_core.run -d models/dialogue
5. Add NLU: nlu.md
6. Add configuration for NLU: nlu_config.yml
7. Train NLU model (current folder): python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
8. Test bot (Dialogue and NLU model): python -m rasa_core.run -d models/dialogue -u models/current/nlu
                                      python -m rasa_core.run -d models/dialogue -u models/default/nlu
9. Teach AI interactively: python train_interactive.py 


  Rasa Core- flow of chatbot. can only understand structured language
  Rasa NLU- understands user input(unstructured language) and converts it to structured language
