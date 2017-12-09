#drawsnake.py
import turtle
 
def drawSnake(rad, angle, len, neckrad):
	for i in range(len):
		turtle.circle(rad, angle)#沿着圆形爬行:轨迹半径的位置,爬行弧度值
		turtle.circle(-rad, angle)
	turtle.circle(rad, angle/2)
	turtle.fd(rad)#forward()表示向前直线爬行移动:距离
	turtle.circle(neckrad+1, 180)
	turtle.fd(rad*2/3)

def main():
	turtle.setup(1300, 800, 0, 0)#建立turtle窗口:宽度,高度,坐标
	pythonsize = 30
	turtle.pensize(pythonsize)#运行轨迹长度
	turtle.pencolor("blue")#轨迹颜色:rgb
	turtle.seth(-40)#运行方向:角度
	drawSnake(40, 80, 5, pythonsize/2)

main()