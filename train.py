from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.agent import Agent
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

#python prmpt equivalent: python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
#train dialogue model (core)
def train_dialogue(domain_file, stories_file, model_dir):
  #assign domain to agent
  #agent = Agent(domain_file, policies=[KerasPolicy(), FallbackPolicy(), MemoizationPolicy(), FormPolicy()])
  agent = Agent(domain_file, policies=[KerasPolicy(), MemoizationPolicy(), FormPolicy()])
  #load story
  training_data = agent.load_data(stories_file)
  #train agent
  agent.train(training_data)
  #create model folder and store dialoge
  agent.persist(model_dir)

#python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
#train nlu model
def train_nlu(data_file, config_file, model_dir):
  #assign nlu
  training_data = load_data(data_file)
  # Create a config that uses this pipeline
  configuration = config.load(config_file)
  # Create a trainer that uses this config
  trainer = Trainer(configuration)
  # Create an interpreter by training the model
  trainer.train(training_data)
  #create model folder and store nlu
  trainer.persist(model_dir, fixed_model_name = "nlu")
  
if __name__ == "__main__":
  #train dialogue/core
  train_dialogue("domain.yml", "stories.md", "models/dialogue")
  #train nlu
  train_nlu("nlu.md", "nlu_config.yml", "models/")
  