import random
import json
import time
import torch
from brain import NeuralNetwork
from neural_network import bag_of_words,tokenize
from voice_input import Listen
from voice_output import say
from functional import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('content.json','r') as jd:
    contents = json.load(jd)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']


model_state = data['model_state']

model = NeuralNetwork(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

Name = "Python Assistant"
def main_function():
    stm = Listen()
    result_search = str(stm)
    if stm == "quit" or stm == "exit":
        say('Goodbye Sir.')
        exit()
    elif stm == None:
        main_function()
        
    stm = tokenize(stm)
    w = bag_of_words(stm,all_words)
    w = w.reshape(1,w.shape[0])
    w = torch.from_numpy(w).to(device)
    output = model(w) 
    
    _ , predicted = torch.max(output,dim=1)
    itm = predicted.item()
    tag = tags[itm]
    
    probs = torch.softmax(output,dim=1)
    
    prob = probs[0][itm]
    
    if prob.item() > 0.75:
        for con in contents['content']:
            if tag == con['tag']:
                replay = random.choice(con['responses'])
                if 'time' in replay:
                    get_error(replay)
                elif 'date' in replay:
                    get_error(replay)
                elif 'day' in replay:
                    get_error(replay)
                elif 'internet speed' in replay:
                    get_error(replay)
                elif 'break' in replay:
                    get_error(replay)
                elif 'wikipedia' in replay:
                    get_input_error(replay,stm)
                elif 'google' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'YouTube' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'website' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'playmusic' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'weather' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,stm[-1])
                elif 'temperature' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'calculate' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'whatsapp message' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'whatsapp call' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'whatsapp video' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'whatsapp chat' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'facebook message' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'facebook call' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'facebook video' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'facebook chat' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'instagram' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open word' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open excel' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open powerpoint' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open access' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open chrome' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open vscode' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open command' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open photoshop' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open outlook' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open jupyter' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open spyder' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open zoom' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open py projects' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'open dj projects' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'remember that' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'what do you remember' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                elif 'how to' in replay:
                    say("Ok Sir..")
                    get_input_error(replay,result_search)
                
                else:
                    say(replay)
while True:
    main_function()

    
