from read_data import fromJson
def get_post_per_month(data:dict)->dict:
    
    month = {
        6:0,
        7:0,
        8:0,
        9:0,
        10:0,
        11:0,
    }
    message = data['messages']
    for msg in messages:
        if msg ['type']==message:
            date = msg['date']

            month[int(date[5:7])]+=1
    
    
    return month
file_path = "data/result.json"
data = fromJson(file_path)
month = get_post_per_month(data)
print(month)
