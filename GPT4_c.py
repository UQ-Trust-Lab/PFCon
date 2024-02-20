import os
import openai

def fetch_GPT_ob_res(sent1, sent2, sent3):
  key = ''
  openai.api_key = key
  # open("key_guan.txt","r").read().strip("\n")

  completion_1 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: Under the context of OAuth authorization, does the access to object "tags of photos" require the permission to access "comments of your photos", the permission system is: <>'
                                  'results: No'},

      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
      {'role': 'user', 'content': 'sentence:' + sent1},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
    ],
    temperature = 0
  )

  res_1 = completion_1['choices'][0]['message']['content']

  completion_2 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: Under the context of OAuth authorization. The service  OneDrive has a description: OneDrive is the place to store your files so you can access them from virtually any device. Use OneDrive and you\'ll never be without the documents, notes, photos, and videos that matter to you. does the access to object "tags of photos" require the permission to access "comments of your photos" '
                                  'results: Yes'},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
      
      {'role': 'user', 'content': 'sentence:' + sent2},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
    ],
    temperature = 0
  )

  res_2 = completion_2['choices'][0]['message']['content']

  completion_3 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: Under the context of OAuth authorization. The service  OneDrive has a description: OneDrive is the place to store your files so you can access them from virtually any device. Use OneDrive and you\'ll never be without the documents, notes, photos, and videos that matter to you.  does the access to object "tags of photos" require the permission to access "comments of your photos", Lattice system for object in MyDrive, we use "a < b" to denote that a is the attribute of b. ("filename < photos", "path < photos","comments < photos", "tags < photos" )'
                                  'results: \n From the lattice system, tags is one attribute of photos, comments is another attributes of photos, access to tags of photos does not require the access to photo comments \n The answer is No. '},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
      
      {'role': 'user', 'content': 'sentence:' + sent3},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
    ],
    temperature = 0
  )

  res_3 = completion_3['choices'][0]['message']['content']
  return res_1, res_2, res_3

def fetch_chatGPT_op_ob_res(sent1, sent2, sent3):
  key = ''
  openai.api_key = key
  # open("key_guan.txt","r").read().strip("\n")

  completion_1 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: Under the context of OAuth authorization, does the action "Create text file" require the permission "add a file OneDrive" '
                                  'results: Yes'},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
      
      {'role': 'user', 'content': 'sentence:' + sent1},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
    ],
    temperature = 0
  )

  res_1 = completion_1['choices'][0]['message']['content']

  completion_2 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: Under the context of OAuth authorization. The service  OneDrive has a description: OneDrive is the place to store your files so you can access them from virtually any device. Use OneDrive and you\'ll never be without the documents, notes, photos, and videos that matter to you. Does the Service action "Create text file" require the permission "add a file OneDrive",Return Yes or No '
                                  'results: Yes'},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions, Return Yes or No'},
      
      {'role': 'user', 'content': 'sentence:' + sent2},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
    ],
    temperature = 0
  )

  res_2 = completion_2['choices'][0]['message']['content']

  completion_3 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: Under the context of OAuth authorization. The service  OneDrive has a description: OneDrive is the place to store your files so you can access them from virtually any device. Use OneDrive and you\'ll never be without the documents, notes, photos, and videos that matter to you. Does the Service action "see your photos" require the permission "delete your photos", We use symbols "<" to denote "is subsumed by". The lattice system is (see < access, delete  < edit, change < edit, add < edit, access  < unknown, edit < unknown). Return Yes or No '
                                  'results: \n From the lattice system, s a result, the operation "access" is a prerequisite for executing the action "see your photos", while "edit" exists in a parallel hierarchy compared to "access" since they all are under "unknown". "edit" and "see" has no direct relationship. Therefore, there is no subsumptive relationship between "edit" and "see". We conclude the action "see your photos" does not require permission to "edit your photos". \n The answer is No. '},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
      
      {'role': 'user', 'content': 'sentence:' + sent3},
      {'role': 'assistant', 'content': 'Assist me in judging whether the API to perform action requires permissions'},
    ],
    temperature = 0
  )

  res_3 = completion_3['choices'][0]['message']['content']
  return res_1, res_2, res_3

def fetch_chatGPT_res(sent):
  key = ''
  openai.api_key = key
  # open("key_guan.txt","r").read().strip("\n")

  completion_1 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'assistant', 'content': 'Assist me in breaking down complex sentences into a series of simpler sentences, each comprising only one operation and one object, the simple sentence should contain no conjunctions.'},
      {'role': 'user', 'content': sent},
    ],
    temperature = 0
  )

  res_1 = completion_1['choices'][0]['message']['content']
  completion_2 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: IFTTT will be able to access, change, and add or delete your photos and documents on MyDrive.'
                                  'results:{[IFTTT will be able to access your photos on MyDrive; IFTTT will be able to access your documents on MyDrive; IFTTT will be able to change your photos on MyDrive; IFTTT will be able to change your documents on MyDrive; IFTTT will be able to add to your photos on MyDrive; IFTTT will be able to add to your documents on MyDrive; IFTTT will be able to delete your photos on MyDrive; IFTTT will be able to delete your documents on MyDrive.]}'},
      {'role': 'assistant', 'content': 'Assist me in breaking down complex sentences into a series of simpler sentences, each comprising only one operation and one object, the simple sentence should contain no conjunctions.'},
      
      {'role': 'user', 'content': 'sentence:' + sent},
      {'role': 'assistant', 'content': 'Assist me in breaking down complex sentences into a series of simpler sentences, each comprising only one operation and one object, the simple sentence should contain no conjunctions.'},
    ],
    temperature = 0
  )
  res_2 = completion_2['choices'][0]['message']['content']
  
  completion_3 = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': 'You are a developer of OAuth authorization system.'},
      {'role': 'user', 'content': 'I will give you a complex sentence and the expected results '
                                  'sentence: IFTTT will be able to access, change, and add or delete your photos and documents on MyDrive.'
                                  'This sentence contains four operations on two objects (each operation can access these two objects), so there should be 4*2 = 8 simpler sentences, and results:{[IFTTT will be able to access your photos on MyDrive; IFTTT will be able to access your documents on MyDrive; IFTTT will be able to change your photos on MyDrive; IFTTT will be able to change your documents on MyDrive; IFTTT will be able to add to your photos on MyDrive; IFTTT will be able to add to your documents on MyDrive; IFTTT will be able to delete your photos on MyDrive; IFTTT will be able to delete your documents on MyDrive.]}'},
      {'role': 'assistant', 'content': 'Assist me in breaking down complex sentences into a series of simpler sentences, each comprising only one operation and one object, the simple sentence should contain no conjunctions.'},
      
      {'role': 'user', 'content': 'sentence:' + sent},
      {'role': 'assistant', 'content': 'Assist me in breaking down complex sentences into a series of simpler sentences, each comprising only one operation and one object, the simple sentence should contain no conjunctions.'},
    ],
    temperature = 0
  )
  res_3 = completion_3['choices'][0]['message']['content']
  # res_list = res_content.replace('results:{[', '').replace(']}', '').split(';')
  return res_1, res_2, res_3

def analyze_sent_sep_performance():
  f = 'permission_sentence.txt'
  queries = open(f, 'r').readlines()
  count = 1
  for query in queries:
    query  = query.strip('\n')
    if len(query) == 0:
      continue

    if count > 20:
      break

    # tks = query.split('##')
    # action = tks[0]
    # permission = tks[1]
    # sent = 'Under the context of OAuth authorization, does the action "' + action + '" require the permission "' + permission + '"' 

    res_1, res_2, res_3 = fetch_chatGPT_res(query.strip('\n'))
    print('count: ',count, '#######################')
    print('query ###', query)
    print('res_1' , '\n', res_1)
    print('###')
    print('res_2', '\n', res_2)
    print('###')
    print('res_3', '\n', res_3)

    count += 1
  print(count)

def analyze_object_check_performance():
  f = 'action_permission_photos.txt'
  lines = open(f, 'r').readlines()
  count = 0
  for line in lines:
    tks = line.split('##')
    action = tks[0]
    permission = tks[1]
    count += 1

    service_description = "OneDrive is the place to store your files so you can access them from virtually any device. Use OneDrive and you will never be without the documents, notes, photos, and videos that matter to you."
    sent1 = 'Under the context of OAuth authorization, does the action "' + action + '" require the permission "' + permission + '"' 
    sent2 = 'Under the context of OAuth authorization, The service description is: ' + service_description + '. does the action "' + action + '" require the permission "' + permission + '"' 
    sent3 = sent2 + '. We use symbols "<" to denote "is subsumed by". The lattice system is (see < access, delete  < edit, change < edit, add < edit, access  < unknown, edit < unknown)'
    res_1, res_2, res_3 = fetch_chatGPT_op_ob_res(sent1, sent2, sent3)
    print('count: ',count, '#######################')
    print('query ###', line)
    print('res_1' , '\n', res_1)
    print('###')
    print('res_2', '\n', res_2)
    print('###')
    print('res_3', '\n', res_3)

  return

def analyze_ob_results():
  f = 'object_permission_photos.txt'
  lines = open(f, 'r').readlines()
  count = 0
  for line in lines:
    tks = line.split('##')
    object = tks[0]
    permission = tks[1]
    lattice = tks[2]
    service_des_onedrive = "OneDrive is the place to store your files so you can access them from virtually any device. Use OneDrive and you will never be without the documents, notes, photos, and videos that matter to you."
    service_des_monzo = "The bank of the future. Instant notifications. Built-in budgeting. Free payments abroad. This isn’t banking as you know it. Monzo is a bank for everyone, built together with our community. Join the revolution today."
    service_description = ""
    if count < 11:
      service_description = service_des_onedrive
    else:
      service_description = service_des_monzo
    sent1 = 'Under the context of OAuth authorization, does the access to object "' + object + '" require the permission to access the object "' + permission + '"'
    sent2 = 'Under the context of OAuth authorization, The service description is: ' + service_description + '. does the access to object "' + object + '" require the permission to access "' + permission + '"' 
    sent3 = sent2 + ' lattice system: ' + lattice

    res_1, res_2, res_3 = fetch_GPT_ob_res(sent1, sent2, sent3)
    print('count: ',count, '#######################')
    print('query ###', line)
    print('res_1' , '\n', res_1)
    print('###')
    print('res_2', '\n', res_2)
    print('###')
    print('res_3', '\n', res_3)
    count += 1
  return

if __name__ == '__main__':
  analyze_ob_results()
  pass