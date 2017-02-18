import numpy as np
import scipy as sp
import scipy.spatial
import matplotlib.pyplot as plt
import matplotlib
import math
from functools import cmp_to_key


class BoundVoronoi:
    def __init__(self, bound=(-27.5, 27.5, -27.5, 27.5), space=0.1):
        self._bounds = np.array(bound)
        self._space = space

    def _generate_by_points(self, points):
        # create the reflection symmetries points
        points_left = np.copy(points)
        points_left[:, 0] = self._bounds[0] - (points_left[:, 0] - self._bounds[0])
        points_right = np.copy(points)
        points_right[:, 0] = self._bounds[1] + (self._bounds[1] - points_right[:, 0])
        points_down = np.copy(points)
        points_down[:, 1] = self._bounds[2] - (points_down[:, 1] - self._bounds[2])
        points_up = np.copy(points)
        points_up[:, 1] = self._bounds[3] + (self._bounds[3] - points_up[:, 1])
        all_points = np.concatenate((points, points_left, points_right, points_down, points_up))
        # generate by scipy.spatial
        vor = sp.spatial.Voronoi(all_points)
        return vor

    def _read_poisson(self, file_name='poisson/Poisson.txt'):
        position_list = []
        with open(file_name, 'r', encoding='utf-8') as f:
            first_line = True
            for line in f:
                if first_line:
                    first_line = False
                    continue
                line_token = line.split(' ')
                position_list.append((float(line_token[0]), float(line_token[1])))
        # sort by coordinate
        position_list.sort(key=lambda p: p[0]**2+p[1]**2)
        return position_list

    def _move_point(self, centroid, point):
        gap_x = point[0] - centroid[0]
        gap_y = point[1] - centroid[1]
        distance = math.sqrt(gap_y**2 + gap_x**2)
        new_y = point[1] - self._space / distance * gap_y
        new_x = point[0] - self._space / distance * gap_x
        return np.array([new_x, new_y])



    def generate(self):
        # read Poisson.txt
        points = self._read_poisson()
        points = np.array(points)
        # extends
        x_width = self._bounds[1] - self._bounds[0]
        y_width = self._bounds[3] - self._bounds[2]
        points[:, 0] = points[:, 0] * x_width + self._bounds[0]
        points[:, 1] = points[:, 1] * y_width + self._bounds[2]
        vor = self._generate_by_points(points)
        sp.spatial.voronoi_plot_2d(vor)
        # plt.show()
        plt.savefig('images/vor_full.png')
        plt.close()
        # get points and vertices
        vertice_list = []
        point_list = []
        for i in range(len(points)):
            point = points[i]
            point_list.append(point)
            vertices = []
            region_index = vor.point_region[i]
            vertice_index_list = vor.regions[region_index]
            if len(vertice_index_list) == 0 \
                    or -1 in vertice_index_list:
                raise Exception('Region should not at boundary')
            for vertice_index in vertice_index_list:
                vertice = vor.vertices[vertice_index]
                vertices.append(vertice)
            vertices = np.array(vertices)
            vertice_list.append(vertices)
        rgb = np.random.random((len(point_list), 3))
        # paint vertice_list
        fig = plt.figure()
        ax = fig.gca()
        plt.axis(self._bounds)
        # vertice_list
        poly_coll = matplotlib.collections.PolyCollection(vertice_list, facecolors=rgb)
        ax.add_collection(poly_coll)
        # point_list
        for i in range(len(points)):
            point = point_list[i]
            ax.text(point[0], point[1], str(i + 1), fontsize=10)
            ax.plot(point[0], point[1], 'r.')
        plt.savefig('images/vor.png')
        plt.close()
        # get space_vertice_list
        space_vertice_list = []
        for i in range(len(points)):
            point = point_list[i]
            vertices = vertice_list[i]
            space_vertices = []
            for vertice in vertices:
                space_vertices.append(self._move_point(point, vertice))
            space_vertices = np.array(space_vertices)
            space_vertice_list.append(space_vertices)
        # paint vertice_list
        fig = plt.figure()
        ax = fig.gca()
        plt.axis(self._bounds)
        # vertice_list
        poly_coll = matplotlib.collections.PolyCollection(space_vertice_list, facecolors=rgb)
        ax.add_collection(poly_coll)
        # point_list
        for i in range(len(points)):
            point = point_list[i]
            ax.text(point[0], point[1], str(i + 1), fontsize=10)
            ax.plot(point[0], point[1], 'r.')
        plt.savefig('images/vor_space.png')
        plt.close()
        # save points
        with open('Point.txt', 'w', encoding='utf-8') as f:
            f.write('NumPoints = %d\n' % len(point_list))
            for point in point_list:
                f.write('%f, %f\n' % (point[0], point[1]))
        # save regions
        with open('Region.txt', 'w', encoding='utf-8') as f:
            f.write('NumRegions = %d\n' % len(space_vertice_list))
            for vertices in space_vertice_list:
                for vertice in vertices:
                    f.write('%f, %f\t' % (vertice[0], vertice[1]))
                f.write('\n')

bound_vor = BoundVoronoi()
bound_vor.generate()