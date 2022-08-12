from asyncio import events
import json 

event_file = 'reward_event.json'
excel_data_file = 'excel_data_reward.json'
base = 10**12
size_data_block = 64

def parse(input_file, output_file):
    with open(input_file, 'r') as input:
        events = json.load(input)['result']
    counts = []
    total = 0
    for event in events:
        timestamp = int(event['timeStamp'], 16)
        total += (int(event['data'][2:][size_data_block:size_data_block*2], 16) / base) 
        counts.append([timestamp, total])
    with open(output_file, 'w') as output:
        json.dump(counts, output)

if __name__ == '__main__':
    parse(event_file, excel_data_file)
