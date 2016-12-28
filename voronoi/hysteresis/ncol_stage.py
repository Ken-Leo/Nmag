import numpy as np


def read_results(file_name='ncol.txt'):
    result_list = np.zeros((106, 98))
    line_index = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            token_index = 0
            line_token = line.split('  ')
            for token in line_token:
                if len(token.strip()) == 0:
                    continue
                print(token)
                result_list[line_index][token_index] = float(token.strip())
                token_index += 1
            line_index += 1
    return result_list

result_list = read_results()
start_stage, end_stage = 0, 0
for i in range(106):
    positive_count = 0
    for j in range(98):
        if result_list[i][j] > 0:
            positive_count += 1
    if start_stage == 0 and positive_count > 49:
        start_stage = i
    if end_stage == 0 and positive_count >= 98:
        end_stage = i
    print('Stage %d Positive count %d' % (i+1, positive_count))
print('start_stage %d - end_stage %d' % (start_stage+1, end_stage+1))