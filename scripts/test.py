# # # 测试wxpython是否正确安装
# # import wx
# # import wx.glcanvas

# # class Frame(wx.Frame):
# #     def __init__(self, size, title):
# #         super(Frame, self).__init__(
# #             None,
# #             style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
# #         )
# #         self.SetTitle(title)
# #         self.SetClientSize(size)
# #         self.Center()
# #         self.view = Canvas(self)
        
# # class Canvas(wx.glcanvas.GLCanvas):
# #     def __init__(self, parent):
# #         super(Canvas, self).__init__(
# #             parent,
# #             attribList=[
# #                 wx.glcanvas.WX_GL_CORE_PROFILE,
# #                 wx.glcanvas.WX_GL_RGBA,
# #                 wx.glcanvas.WX_GL_DOUBLEBUFFER,
# #                 wx.glcanvas.WX_GL_DEPTH_SIZE,
# #                 24
# #             ]
# #         )
        
# # app = wx.App(False)
# # frame = Frame((256, 256), "Hello")
# # frame.Show()
# # app.MainLoop()

# 测试simple_3dviz是否正确安装
import numpy as np

from simple_3dviz import Mesh, Lines
from simple_3dviz.window import show


def heart_voxel_grid(N):
    """Create a NxNxN voxel grid with True if the voxel is inside a heart
    object and False otherwise."""
    x = np.linspace(-1.3, 1.3, N)
    y = np.linspace(-1.3, 1.3, N)
    z = np.linspace(-1.3, 1.3, N)
    x, y, z = np.meshgrid(x, y, z)
    return (2*x**2 + y**2 + z**2-1)**3 - (1/10) * x**2*z**3 - y**2*z**3 < 0


if __name__ == "__main__":
    voxels = heart_voxel_grid(64)
    m = Mesh.from_voxel_grid(voxels, colors=(0.8, 0, 0))
    l = Lines.from_voxel_grid(voxels, colors=(0, 0, 0.), width=0.001)
    show([l, m])
# import wx
# import wx.glcanvas

# class Frame(wx.Frame):
#     def __init__(self, size, title):
#         super(Frame, self).__init__(
#             None,
#             style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
#         )
#         self.SetTitle(title)
#         self.SetClientSize(size)
#         self.Center()
#         self.view = Canvas(self)
        
# class Canvas(wx.glcanvas.GLCanvas):
#     def __init__(self, parent):
#         super(Canvas, self).__init__(
#             parent,
#             attribList=[
#                 wx.glcanvas.WX_GL_CORE_PROFILE,
#                 wx.glcanvas.WX_GL_RGBA,
#                 wx.glcanvas.WX_GL_DOUBLEBUFFER,
#                 wx.glcanvas.WX_GL_DEPTH_SIZE,
#                 24
#             ]
#         )
        
# app = wx.App(False)
# frame = Frame((256, 256), "Hello")
# frame.Show()
# app.MainLoop()