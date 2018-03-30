import json
import time

import requests

imei = raw_input("Enter IMEI >>").strip()

base_path = '/home/sandeep/portal/chosen/'

# original_imei = '352787060708993'

# train_files = [20160907032421, 20160907032759, 20160907032846, 20160907033003, 20160907033021, 20160907033140, 20160907033446, 20160907033527, 20160907033617, 20160907033646, 20160907033710, 20160907034048, 20160907034102, 20160907042523, 20160907042612, 20160907042622, 20160907042713, 20160907042749, 20160907054922, 20160907054923, 20160907054924, 20160907055002, 20160907055028, 20160907055201, 20160907060804, 20160907060809, 20160907061417, 20160907061424, 20160907061452, 20160907061513, 20160907061557, 20160907061831, 20160907061943, 20160907062322, 20160907062359, 20160907062436, 20160907063611, 20160907064201, 20160907064216, 20160907064234, 20160907065714, 20160907065814, 20160907065910, 20160907065924, 20160907065940, 20160907070107, 20160907070242, 20160907070357, 20160907070905, 20160907071130, 20160907071312, 20160907071516, 20160907071756, 20160907071839, 20160907072012, 20160907072138, 20160907072226, 20160907072712, 20160907073308, 20160907073329, 20160907073350, 20160907073503, 20160907074311, 20160907074402, 20160907074505, 20160907074513, 20160907074522, 20160907074535, 20160907074602, 20160907075000, 20160907075014, 20160907075117, 20160907075141, 20160907075208, 20160907075341, 20160907095035, 20160907095305, 20160907095359, 20160907095409, 20160907095423, 20160907095608, 20160907095626, 20160907095854, 20160907095902, 20160907095903, 20160907095929, 20160907095941, 20160907100011, 20160907100029, 20160907100042, 20160907100059, 20160907100120, 20160921133955, 20160921134004, 20160921134029, 20160921134054, 20160921134135, 20160921134140, 20160921134346, 20160921135037, 20160921135129, 20160921135152, 20160921135156, 20160921135205, 20160921135218, 20160925023035, 20160925023059, 20160925023106, 20160925023118, 20160925023519, 20160925023532, 20160925024042, 20160925024050, 20160925024222, 20160925024234, 20160925025305, 20160925025408, 20160925025558, 20160925025616, 20160925025731, 20160925030037, 20160925030105, 20160925030128, 20160925030538, 20160925030616, 20160925030737, 20160925030750, 20160925030849, 20160925030911, 20160925030915, 20160925031414, 20160925031657, 20160925032200, 20160925032253]

# test_files = [20160907033710, 20160907034048, 20160907034102, 20160907042523, 20160907042612, 20160907042622, 20160907042713, 20160907042749, 20160907054922, 20160907054923, 20160907054924, 20160907055002, 20160907055028, 20160907055201, 20160907060804, 20160907060809, 20160907061417, 20160907061424, 20160907061452, 20160907061513, 20160907061542, 20160907061557, 20160907061831, 20160907061943, 20160907062322, 20160907062359, 20160907062436, 20160907063611, 20160907064201, 20160907064216, 20160907064234, 20160907070242, 20160907070357, 20160907071516, 20160907073308, 20160907073329, 20160907073350, 20160907073503, 20160907074120, 20160907074311, 20160907074402, 20160907074505, 20160907074513, 20160907074522, 20160907074535, 20160907074602, 20160907075000, 20160907075014, 20160907075117, 20160907075141, 20160907075208, 20160907075341, 20160907095035, 20160907095305, 20160907095359, 20160907095409, 20160907095423, 20160907095608, 20160907095626, 20160907095854, 20160907095902, 20160907095903, 20160907095912, 20160907095929, 20160907095941, 20160907100011, 20160907100029, 20160907100042, 20160907100059, 20160907100120, 20160921133955, 20160921134004, 20160921134029, 20160921134054, 20160921134135, 20160921134140, 20160921134346, 20160921135037, 20160921135129, 20160921135152, 20160921135156, 20160921135205, 20160921135218, 20160925023035, 20160925023059, 20160925023106, 20160925023118, 20160925023519, 20160925023532, 20160925024042, 20160925024050, 20160925024222, 20160925024234, 20160925025305, 20160925025408, 20160925025558, 20160925025616, 20160925025731, 20160925030037, 20160925030105, 20160925030128, 20160925030538, 20160925030616, 20160925030737, 20160925030750, 20160925030849, 20160925030911, 20160925030915, 20160925031414, 20160925031657, 20160925032200, 20160925032253]


# CHOSEN 2
original_imei = '357143044484308'

train_files = [20160906140748, 20160906144629, 20160906144745, 20160906144915, 20160906144935, 20160906145032,
               20160906145105, 20160906145252, 20160906145608, 20160906161742, 20160906161820, 20160906161920,
               20160906162030, 20160906171426, 20160906171504, 20160906172525, 20160907015317, 20160907015723,
               20160907020826, 20160907035605, 20160907035652, 20160907035824, 20160907035902, 20160907041343,
               20160907041558, 20160907041819, 20160907041946, 20160907042249, 20160907042616, 20160907074620,
               20160907081307, 20160907081938, 20160907082822, 20160907085224, 20160907091937, 20160907092541,
               20160907093627, 20160907094152, 20160907094436, 20160907094614, 20160907095653, 20160907101930,
               20160907101941, 20160907110832, 20160907112220, 20160907125814, 20160907131855, 20160907132154,
               20160907132356, 20160907134740, 20160907135542, 20160907143008, 20160907161108, 20160907161117,
               20160907161702, 20160907175828, 20160907190822, 20160907191148, 20160907191158, 20160908033313,
               20160908035537, 20160908040545, 20160908040939, 20160908040949, 20160908041042, 20160908041051,
               20160908041126, 20160908052017, 20160908052510, 20160908075215, 20160908101732, 20160908101746,
               20160908104820, 20160908111033, 20160908115023, 20160908124229, 20160908125354, 20160908141919,
               20160908141928, 20160908141943, 20160908142151, 20160908155746, 20160908161728, 20160909012345,
               20160909035056, 20160909035104, 20160909035115, 20160909035130, 20160909035150, 20160909035159,
               20160909035258, 20160909035306, 20160909035311, 20160910133444, 20160910133446, 20160914101735,
               20160914130803, 20160914130810, 20160919014559, 20160919014604, 20160919014607, 20160920105338,
               20160920233250, 20160920233511, 20160921000034, 20160921000839, 20160921073628, 20160921104020,
               20160923024817, 20160923024825, 20160923024954, 20160923025002, 20160923025538, 20160925195733,
               20160926120513]

test_files = [20160906140748, 20160906161820, 20160906161920, 20160906162030, 20160906171426, 20160906171504,
              20160906172525, 20160907015317, 20160907015723, 20160907020826, 20160907035605, 20160907035652,
              20160907035902, 20160907041343, 20160907041558, 20160907041819, 20160907041946, 20160907042249,
              20160907042616, 20160907074620, 20160907081307, 20160907081938, 20160907082822, 20160907085224,
              20160907091937, 20160907092541, 20160907093627, 20160907094152, 20160907094436, 20160907094614,
              20160907095653, 20160907101930, 20160907101941, 20160907110832, 20160907112220, 20160907125814,
              20160907131855, 20160907132154, 20160907132356, 20160907134740, 20160907135542, 20160907143008,
              20160907161108, 20160907161117, 20160907161702, 20160907175828, 20160907190822, 20160907191148,
              20160907191158, 20160908033313, 20160908035537, 20160908040545, 20160908040939, 20160908040949,
              20160908041042, 20160908041051, 20160908041126, 20160908052017, 20160908052510, 20160908075215,
              20160908101732, 20160908101746, 20160908104820, 20160908111033, 20160908115023, 20160908124229,
              20160908125354, 20160908141919, 20160908141928, 20160908141943, 20160908142151, 20160908155746,
              20160908161728, 20160909012345, 20160909035056, 20160909035104, 20160909035115, 20160909035130,
              20160909035150, 20160909035159, 20160909035258, 20160909035306, 20160909035311, 20160910133444,
              20160910133446, 20160914101735, 20160914130803, 20160914130810, 20160919014559, 20160919014604,
              20160919014607, 20160920105338, 20160920233250, 20160920233511, 20160921000034, 20160921000839,
              20160921073628, 20160921104020, 20160923024817, 20160923024825, 20160923024954, 20160923025002,
              20160923025538, 20160925195733, 20160926120513]

# sort based on earliest time
train_files.sort()
test_files.sort()


def sandeep():
    print requests.get('http://localhost:8000/sandeep/').text


def train(imei, file_path):  # returns imei, result code, numfiles
    files = {'path': open(file_path, 'rb')}
    data = {'imei': imei}
    r = requests.post('http://localhost:8000/train/', files=files, data=data)
    print r.text


def test(imei, file_path):  # returns max version which can be passed to query
    files = {'path': open(file_path, 'rb')}
    data = {'imei': imei}
    r = requests.post('http://localhost:8000/test/', files=files, data=data)
    print r.text
    return json.loads(r.text)['max_version']


def ask_trained(imei, version):  # returns 'trained' or not
    data = {'imei': imei, 'version': version}
    r = requests.post('http://localhost:8000/ask_trained/', data=data)
    print r.text


def query(imei, version):  # used to get the summary ('result', 'version')
    data = {'imei': imei, 'version': version}
    r = requests.post('http://localhost:8000/query/', data=data)
    print r.text


def manual_fix(imei, version, signal):  # fixes a version. signal is either 0 or 1
    data = {'imei': imei, 'version': version, 'signal': signal}
    r = requests.post('http://localhost:8000/manual_fix/', data=data)
    print r.text
    # returns 'imei' and 'received_signal'


# MAIN PROCESSNG LOOP

# testing server
# sandeep()

datapoints = test_files  # train_files # [:10] + test_files

i = 0
latest_version = 0
while True:
    print 'loading data point number: {}'.format(i)
    print 'working on imei: {}'.format(imei)
    print 'pick your choice:'
    print '* train'
    print '* test'
    print '* ask'
    print '* query'
    print '* manual'
    print '* exit'

    # choice = raw_input("choice >>").strip()
    if i < 17:
        choice = 'train'
    else:
        choice = 'test'

    if choice == 'train':
        # train code here
        try:
            file_path = base_path + 'train/' + original_imei + '/' + str(datapoints[i])
            train(imei, file_path)
            time.sleep(2)
            ask_trained(imei, latest_version)
        except Exception as e:
            print e
        i += 1
    elif choice == 'test':
        # test code here
        try:
            file_path = base_path + 'train/' + original_imei + '/' + str(datapoints[i])
            latest_version = test(imei, file_path)
            print 'latest_version', latest_version
            time.sleep(5)
            query(imei, latest_version)
        except Exception as e:
            print e
        i += 1
    elif choice == 'ask':
        # ask trained code here
        ask_trained(imei, latest_version)
    elif choice == 'query':
        # query code here
        query(imei, latest_version)
        pass
    elif choice == 'manual':
        # manual code here
        signal = raw_input("signal >>").strip()
        manual_fix(imei, latest_version, signal)
    elif choice == 'exit':
        break
    else:
        print 'oops, typo?'
