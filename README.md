# Gaffer_OpenResources

基于开源软件Gaffer的节点示例

## Circle_Curve
通过让一个物体环绕世界中心360度，产生MotionPath，将这一段保存为一个正圆曲线

![image](https://github.com/WangSnowchen/Gaffer_OpenResources/assets/62184149/3042c6e4-fe02-476c-9f64-3e5df9c7bf89)

## Create_Points
通过对一个平面Scatter，取出一个点通过CollectScenes创建出多个可以批量控制位移的点

![image](https://github.com/WangSnowchen/Gaffer_OpenResources/assets/62184149/b2b15153-1a96-426e-9293-e6ed5c26a140)

## Crowds_BoundCenter
适用于群集角色命名为“A1”，“A2”。。。"A3"的情况，通过FilterResults和BoundQuery批量查询每个角色的中心位置并创建想要批量创建的物体（附有Python脚本来批量创建表格）

## GetZ
通过对渲染出来的Z通道进行计算，生成景深雾气

## NodeMetadata
通过对节点的Metadata进行操作，可以更改节点的颜色和连接线的颜色以及节点的注释

## Nuke_Color_to_gaffer
通过对nuke Grade节点的Multiply颜色数值做计算，还原在nuke中修改的颜色到灯光（注意：Multiply颜色数值调整应该在0-1之间调整，不可超过数值1）

## Onion_skin
在一帧里看到前后帧数的动态效果，类似2D动画的洋葱皮功能

## Point_Visualiser
添加需要查看点序号的模型，调整parameters_vertexIndex，会在opengl窗口高亮显示点的位置，配合PointConstraint来使用

## Reverse_Selection
在一个group中反向选择某一个物体

## SetVisibleSet
每次重开文件都会丢失VisibleSet的状态，此节点可以批量将设置path的VisibleSet为可见状态

## lightlinks_Spreadsheet
灯光链接表格

## LightDecayVisualiser
提供一种可视化的方式来调整灯光的衰减

![image](https://github.com/WangSnowchen/Gaffer_OpenResources/assets/62184149/bef441cf-a7a0-4823-a4c8-f7419327364d)
