import configparser
import numpy as np

class CONFIG:

    def __init__(self, ini_file):

        if ini_file == '':

            print('ini file not found.')
            self.status = False

        else:
            inifile = configparser.SafeConfigParser()
            inifile.read(ini_file)

            #
            # Curve Params の読み込み
            #

            # nr_points を読み込む
            self.nr_points = inifile.getint('Curve Params', 'nr_points')
            #print('nr_points:%d' % self.nr_points)

            # tmin を読み込む
            self.tmin = eval(inifile.get('Curve Params', 'tmin'))
            #print('tmin:%f' % self.tmin)

            # tmax を読み込む
            self.tmax = eval(inifile.get('Curve Params', 'tmax'))
            #print('tmax:%f' % self.tmax)

            # x(t) を読み込む
            self.xt = inifile.get('Curve Params', 'xt')
            #print('x(t):%s' % self.xt)

            # y(t) を読み込む
            self.yt = inifile.get('Curve Params', 'yt')
            #print('y(t):%s' % self.yt)

            # proj_t を読み込む
            self.proj_t = eval(inifile.get('Curve Params', 'proj_t'))
            #print('proj_t:%f' % self.proj_t)

            # proj_x を読み込む
            self.proj_x = eval(inifile.get('Curve Params', 'proj_x'))
            #print('proj_x:%f' % self.proj_x)

            # proj_y を読み込む
            self.proj_y = eval(inifile.get('Curve Params', 'proj_y'))
            #print('proj_y:%f' % self.proj_y)

            #
            # Continuous Shooting Params の読み込み
            #

            # elevation を読み込む
            self.elevation = inifile.getfloat('Continuous Shooting Params', 'elevation')
            #print('elevation:%f' % self.elevation)

            # azimuth_start を読み込む
            self.azimuth_start = inifile.getfloat('Continuous Shooting Params', 'azimuth_start')
            #print('azimuth start:%f' % self.azimuth_start)

            # azimuth_end を読み込む
            self.azimuth_end = inifile.getfloat('Continuous Shooting Params', 'azimuth_end')
            #print('azimuth start:%f' % self.azimuth_start)

            # azimuth_step を読み込む
            self.azimuth_step = inifile.getfloat('Continuous Shooting Params', 'azimuth_step')
            #print('azimuth step:%f' % self.azimuth_step)
