
import pygame

from creatingabotton import button
import random

WIDTH = 1000
HIGHT = 400
ROWS = 20
COLS = 50

class Cube(object):
    
    def __init__(self,pos,color = (0,0,0)):
        self.x = pos[0] - (pos[0]%20)
        self.y = pos[1] - (pos[1]%20)
        self.color  = color

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,(self.x + 1,self.y + 1,19,19))

def drawgrid(surface):

    sizeBr = HIGHT//ROWS
    sizeBc = WIDTH//COLS

    x = 0
    y = 0

    for _ in range(ROWS):
        y += sizeBr
        pygame.draw.line(surface,(138,54,15), (0,y),(WIDTH,y))

    for _ in range(COLS):
        x += sizeBc
        pygame.draw.line(surface,(138,54,15), (x,0),(x,HIGHT))

class treenode(object):
    childs = []
    def __init__(self,data,prnt):
        self.data = data
        self.prnt = prnt



distances = []

for _ in range(COLS + 1):
    x = [] 
    for _ in range(ROWS + 1):
        x.append(None)
    distances.append(x)

def dikstra():

    


   pass
    
def bfs():
    global q,visited,done
    
    xval = q[0].data.x
    yval = q[0].data.y
        
    if (xval+20 < WIDTH) and (not visited[(xval+20)//20][yval//20]): 
        q.append(treenode(Cube([xval + 20,yval],(255,255,0)),q[0]))
        visited[(xval + 20)//20][yval//20] = True
        q[0].childs.append(q[-1])
        
        
    if (xval - 20 >= 0) and (not visited[(xval-20)//20][yval//20]):
        q.append(treenode(Cube([xval - 20,yval],(255,255,0)),q[0]))
        visited[(xval -20)//20][yval//20] = True
        q[0].childs.append(q[-1])
        

    if (yval + 20 < HIGHT) and (not visited[(xval)//20][(yval+20)//20]):
        q.append(treenode(Cube([xval,yval + 20],(255,255,0)),q[0]))
        visited[(xval)//20][(yval)//20] = True
        q[0].childs.append(q[-1])
        

    if (yval - 20 >= 0) and (not visited[(xval)//20][(yval - 20)//20]):
        q.append(treenode(Cube([xval,yval - 20],(255,255,0)),q[0]))
        visited[(xval)//20][(yval - 20)//20] = True
        q[0].childs.append(q[-1])
    
    
    done.append(q[0])
    if q[0].data == st:
        q.pop(0).data.color = (255,0,0)
    else:
        q.pop(0).data.color = (0,0,255)


def redrawwin(surface):
    global wall,st,end,ans,reached
    surface.fill((202,255,112))
    drawgrid(surface)

    if reached:
        reached.data.color = (255,97,3)
        if reached.prnt.prnt:
            ans.append(reached)
        
            reached = reached.prnt
        

    

    for j in range(COLS + 1):
        for jj in range(ROWS + 1):
            if wall[j][jj]:
                wall[j][jj].draw(surface)

    for j in range(len(q)):
        q[0].data.color = (234,1,132)
        q[j].data.draw(surface)

    for j in range(len(done)):
        done[j].data.draw(surface)


    for j in range(len(ans)):
        ans[j].data.draw(surface)
        
    createMaze.draw(surface,(0,0,0))
    resetbutton.draw(surface,(0,0,0))
    mybutton.draw(surface,(0,0,0))
    st.draw(surface)
    end.draw(surface)
    pygame.display.update()

def buttonclick(buton,event,pos):
    
    if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if buton.isOver(pos):
            return True

    if event.type ==pygame.MOUSEMOTION:
        if buton.isOver(pos):
            buton.color = (255,0,0)
        else:
            buton.color = (0,255,0)

    return False

def drag(event):
    global z,pos,r
    if event.type == pygame.MOUSEBUTTONDOWN :
        z =1
        return True
    
    elif z == 1 and event.type == pygame.MOUSEMOTION:
        return True
    
    elif event.type == pygame.MOUSEBUTTONUP :
        z = 0
        r =0
        return False
    else:
        return False    


def reset():
    global st,end,wall,z,r,q,visited,i,done,ans,reached,start,na,speed,speedt
    z =0 # used for draging the mouse
    wall = [] # use store cordinates of obstacles
    for _ in range(COLS + 1):
        x = []
        for _ in range(ROWS + 1):
            x.append(None)
        wall.append(x)
    
    r =0 # used for draging the st end nodes
    st = Cube([240,200],(255,0,0)) #starting node created
    end = Cube([740,200],(0,255,0)) #ending node created
    start =  0 # flag to check bfs is stared
    
    q = []  #A queue used to perform bfs
    q.append(treenode(st,None)) #intial nodes entes in a queue
    
    visited = [] # cheks if a node is visited or not
    
    ans = [] # strores the shortest path after bfs teversel
    
    for k in range(COLS+1):
        x = []
        for j in range(ROWS+1):
            x.append(False)
        visited.append(x) #all nodes set as not visited

    na = 1 #identifies reached at end
    
    reached  = None # will have reached node then its perents and so on
    done = [] # these are the nodes completely prossed
    
    speed = -1000 
    speedt =  50000

    
def main():
    global st,end,wall,z,r,q,visited,i,done,ans,reached,start,mybutton,resetbutton,na,speed,speedt,createMaze
    win = pygame.display.set_mode((WIDTH,600)); #set window size
    clock = pygame.time.Clock()
    
    z =0 # used for draging the mouse
    wall = [] # use store cordinates of obstacles
    for _ in range(COLS + 1):
        x = []
        for _ in range(ROWS + 1):
            x.append(None)
        wall.append(x)
    
    r =0 # used for draging the st end nodes
    st = Cube([240,200],(255,0,0)) #starting node created
    end = Cube([740,200],(0,255,0)) #ending node created
    start =  0 # flag to check bfs is stared
    
    q = []  #A queue used to perform bfs
    q.append(treenode(st,None)) #intial nodes entes in a queue
    
    visited = [] # cheks if a node is visited or not
    
    ans = [] # strores the shortest path after bfs teversel
    
    for k in range(COLS+1):
        x = []
        for j in range(ROWS+1):
            x.append(False)
        visited.append(x) #all nodes set as not visited

    na = 1 #identifies reached at end
    
    reached  = None # will have reached node then its perents and so on
    done = [] # these are the nodes completely prossed
    mybutton = button((0,255,0), 375 ,450,250,100,'Visulize BFS') #creates a button
    createMaze =  button((0,255,0), 100,450,220,70,'Darw Maze')
    resetbutton =  button((0,255,0),700,450,100,50,'reset')
    speed = -1000 
    speedt =  50000

    while True:
        pygame.time.delay(speed)
        clock.tick(speedt)
        
        for event in pygame.event.get():
            
            pos = pygame.mouse.get_pos()
            
            if pos[1] > 380 :
                if (buttonclick(mybutton,event,pos)):
                    start = 1
                
                if (buttonclick(resetbutton,event,pos)):
                    reset()

                if (buttonclick(createMaze,event,pos)):
                    reset()
                    for a in range(0,COLS+1,2):
                        skip  = random.randint(0,HIGHT//2)
                        skip2 = random.randint(HIGHT//2,HIGHT)
                        for b in range(ROWS+1):
                            if not(st.y == b*20 and st.x == a*20) and not(end.y == b*20 and end.x == a*20) and not(b*20 == (skip - (skip%20))) and not(b*20 == (skip2 - (skip2%20))):
                                wall[a][b] = Cube([a*20,b*20],(0,0,0))
                                visited[a][b] = True
                    
            else:
                
                p = drag(event)
                
                if(p):
                    if (pos[0] >= st.x and pos[0] <= st.x +20)and (pos[1] >= st.y and pos[1] <= st.y +20) or r ==1:
                        if z != 0:
                            r =1
                        st.x = (pos[0] - pos[0]%20)
                        st.y = (pos[1] - pos[1]%20)
                        q.pop(0)
                        q.append(treenode(st,None))
            
                    elif (pos[0] >= end.x and pos[0] <= end.x +20)and (pos[1] >= end.y and pos[1] <= end.y +20) or r ==2:
                        if z!= 0:
                            r = 2
                        end.x = (pos[0] - pos[0]%20)
                        end.y = (pos[1] - pos[1]%20)
                        
                            
                    else:
##                        if visited[(pos[0] - pos[0]%20)//20][(pos[1] - pos[1]%20)//20] and not prev == pos:
##                            wall[(pos[0] - pos[0]%20)//20][(pos[1] - pos[1]%20)//20] = None
##                            visited[(pos[0] - pos[0]%20)//20][(pos[1] - pos[1]%20)//20] = False
##
##                        else:
##                            prev = pos
                        wall[(pos[0] - pos[0]%20)//20][(pos[1] - pos[1]%20)//20] = Cube([pos[0],pos[1]],(0,0,0)) 
                        visited[(pos[0] - pos[0]%20)//20][(pos[1] - pos[1]%20)//20] = True
                            

        if start == 1:
            bfs()

        if len(q) == 0:
            reset()
            print("not reachable")
        
        if (q[0].data.x == end.x and q[0].data.y == end.y) and na == 1 :
            reached = q[0]
            na = 0
            speed = 100
            speedt = 300
            start = 0


       
        redrawwin(win)
main()
