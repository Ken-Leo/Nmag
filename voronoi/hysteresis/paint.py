import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.rcParams['animation.ffmpeg_path'] = 'D:\\env\\ImageMagick-7.0.4-0-portable-Q16-x64\\ffmpeg.exe'
# plt.rcParams['animation.convert_path'] = '"D:\\env\\ImageMagick-7.0.4-0-portable-Q16-x64\\convert.exe"'


def read_points(file_name='../geo/Point.txt'):
    point_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            line_token = line.split(',')
            point_list.append((float(line_token[0].strip()), float(line_token[1].strip())))
    return point_list


def read_regions(file_name='../geo/Region.txt'):
    region_point_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            point_list = []
            line_token = line.split('\t')
            for token in line_token:
                if token == '\n':
                    continue
                tokens = token.split(',')
                point_list.append((float(tokens[0].strip()), float(tokens[1].strip())))
            region_point_list.append(point_list)
    return region_point_list


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
                result_list[line_index][token_index] = float(token.strip())
                token_index += 1
            line_index += 1
    return result_list


def result_hard(result_list):
    result_array = []
    for i, result in enumerate(result_list):
        if i % 2 == 0:
            result_array.append(result)
    return result_array

point_list = read_points()
region_list = read_regions()
result_list = read_results()
print('point_list: %d, region_list: %d, result_list: %s' % (len(point_list), len(region_list), str(result_list.shape)))
# paint from stage 80 to 100
start_stage, end_stage = 75, 100
result_max = result_list[start_stage:end_stage].max()
result_min = result_list[start_stage:end_stage].min()
result_norm = mpl.colors.Normalize(vmax=result_max, vmin=result_min)
fig = plt.figure()
ax = fig.gca()
plt.axis((-15, 15, -15, 15))
# only hard result
poly_coll = mpl.collections.PolyCollection(region_list, norm=result_norm, cmap=mpl.cm.get_cmap('jet'))
result_array = np.array(result_hard(result_list[start_stage]))
poly_coll.set_array(result_array)
plt.colorbar(poly_coll, orientation='vertical')
ax.add_collection(poly_coll)
# point_list
for i in range(len(point_list)):
    point = point_list[i]
    ax.text(point[0], point[1], str(i + 1), fontsize=10)
    ax.plot(point[0], point[1], 'r.')
ax.set_xlabel('Stage: %d' % (start_stage+1))
def update(frame_number):
    stage_index = start_stage + frame_number
    result_array = np.array(result_hard(result_list[stage_index]))
    poly_coll.set_array(result_array)
    ax.set_xlabel('Stage: %d' % (stage_index+1))
    return poly_coll
poly_ani = animation.FuncAnimation(fig, update, frames=end_stage-start_stage, interval=500, repeat=False)
plt.rcParams['animation.ffmpeg_path'] = 'D:\\env\\ImageMagick-7.0.4-0-portable-Q16-x64\\ffmpeg.exe'
FFwriter = animation.FFMpegWriter(fps=3, bitrate=7200)
poly_ani.save('result.mp4', writer=FFwriter)
plt.close()
