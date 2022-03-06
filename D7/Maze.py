import turtle
class maze:
    def __init__(self, mazeFileNmae):
        rowsInMaze = 0                         # 初始化迷宫行数
        columnsInMaze = 0                      # 初始化迷宫列数
        self.mazelist = []                     # 初始化迷宫布局列表
        mazeFile = open(mazeFileNmae, 'r')     # 读取迷宫文件
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line:               # 从每行的右边开始读
                rowList.append(ch)             # 添加到行列表
                if ch == 'S':                  # S为乌龟初始位置
                    self.startRow = rowsInMaze # 乌龟初始行
                    self.startCol = col        # 乌龟初始列
                col = col + 1                  # 列号数计 行列搜索
            rowsInMaze = rowsInMaze +1         # 行号计数
            self.mazelist.append(rowList)      # mazelist即为代表迷宫初始布局的嵌套列表
            columnsInMaze = len(rowList)       # 获取迷宫总列数
        self.rowsInMaze = rowsInMaze           # 设置迷宫总行数
        self.columnsInMaze = columnsInMaze     # 设置迷宫总行数
        self.xTranslate = -columnsInMaze/2     # 以中心为原点，设置左上角初始x坐标
        self.yTranslate = rowsInMaze / 2       # 以中心为原点，设置左上角初始y坐标
        self.t = turtle.Turtle()
        self.t.shape('turtle')                 # 画笔设为乌龟形状
        self.wn = turtle.Screen()              # 建立一个作画窗口
        self.wn.setworldcoordinates(-columnsInMaze/2,-rowsInMaze/2,columnsInMaze/2,rowsInMaze/2)
        #设置世界坐标系，上述参数依次为画布左下角x轴坐标，画布左下角y轴坐标，画布右上角x轴坐标。画布右上角y轴坐标

    #在屏幕上绘制迷宫
    def drawMaze(self):
        self.t.speed(20)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawBox(x + self.xTranslate,-y + self.yTranslate,'orange')

    def drawBox(self,x,y,color):
        self.t.up()
        self.t.goto(x - 0.5,y - 0.5)
        self.t.color(color)
        self.t.fillcolor('green')
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self,x,y):
        self.t.up()
        # setheading()设置海龟朝向，towards()从海龟位置到由(x, y)，矢量或另一海龟位置连线的夹角。此数值依赖于海龟初始朝向，由"standard"、"world"或"logo" 模式设置所决定。
        self.t.setheading(self.t.towards(x + self.xTranslate,-y + self.yTranslate))
        self.t.goto(x + self.xTranslate,-y +self.yTranslate)

    def traceDot(self,color):
        self.t.dot(color)                      # 默认size画路径原点

    def updatePosion(self,row,col,val):        # 更新海龟位置，并做标注
        self.mazelist[row][col] = val#假如第3行第2列，则3表示y方向距离，2表示x方向距离
        self.moveTurtle(col,row)#因此move时，col和row交换位置
        if val == PART_OF_PATH:
            color = 'green'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        self.traceDot(color)                   # 根据上述情况trace路径点

    def isExit(self,row,col):
        return (row ==0 or row == self.rowsInMaze - 1 or col ==0 or col ==self.columnsInMaze)

    def __getitem__(self, key):
        return self.mazelist[key]





def searchFrom(maze,startRow,startColumn):
    if maze[startRow][startColumn]== OBSTACLE:
        return False
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    if maze.isExit(startRow,startColumn):
        maze.updatePosion(startRow, startColumn, PART_OF_PATH)
        return  True
    maze.updatePosion(startRow, startColumn, TRIED)
    found = searchFrom(maze,startRow-1,startColumn) or \
            searchFrom(maze,startRow+1,startColumn) or \
            searchFrom(maze,startRow,startColumn-1) or \
            searchFrom(maze,startRow,startColumn+1)
    if found:
        maze.updatePosion(startRow,startColumn,PART_OF_PATH)
    else:
        maze.updatePosion(startRow,startColumn,DEAD_END)
    return found

if __name__ == '__main__':
    PART_OF_PATH = 'O'
    TRIED ='.'
    OBSTACLE = '+'
    DEAD_END = '-'
    myMaze = maze('maze.txt')
    myMaze.drawMaze()
    searchFrom(myMaze,myMaze.startRow,myMaze.startCol)
