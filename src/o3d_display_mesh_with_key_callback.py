import cv2, os, sys
import numpy as np
import open3d as o3d

delta = np.pi / 90
mesh = None

def key_callback_1(vis):

    angle = delta

    rotation = np.array([[np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]])

    transform = rotation #@ transform
    mesh.transform(transform)
    return True

def key_callback_2(vis):

    angle = -delta

    rotation = np.array([[np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]])

    transform = rotation #@ transform
    mesh.transform(transform)
    return True

def key_callback_3(vis):

    angle = delta

    rotation = np.array([[1, 0, 0, 0],
        [0, np.cos(angle), -np.sin(angle), 0],
        [0, np.sin(angle), np.cos(angle), 0],
        [0, 0, 0, 1]])

    transform = rotation #@ transform
    mesh.transform(transform)
    return True

def key_callback_4(vis):

    angle = -delta

    rotation = np.array([[1, 0, 0, 0],
        [0, np.cos(angle), -np.sin(angle), 0],
        [0, np.sin(angle), np.cos(angle), 0],
        [0, 0, 0, 1]])

    transform = rotation #@ transform
    mesh.transform(transform)
    return True

def key_callback_5(vis):

    angle = delta

    rotation = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])

    transform = rotation #@ transform
    mesh.transform(transform)
    return True

def key_callback_6(vis):

    angle = -delta

    rotation = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])

    transform = rotation #@ transform
    mesh.transform(transform)
    return True


def main():

    global mesh

    argv = sys.argv
    argc = len(argv)

    delta = np.pi / 45

    if argc < 2:
        print('%s loads and displays mesh file (.obj)' % argv[0])
        print('%s <obj file>' % argv[0])
        quit()

    mesh =  o3d.io.read_triangle_mesh(argv[1])

    mesh.compute_vertex_normals()

    # 可視化の設定
    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window()
    vis.add_geometry(mesh)
    vis.register_key_callback(ord("1"), key_callback_1)
    vis.register_key_callback(ord("2"), key_callback_2)
    vis.register_key_callback(ord("3"), key_callback_3)
    vis.register_key_callback(ord("4"), key_callback_4)
    vis.register_key_callback(ord("5"), key_callback_5)
    vis.register_key_callback(ord("6"), key_callback_6)

    # 実行
    vis.run()
    vis.destroy_window()

if __name__ == '__main__':
    main()
