from grid import Grid
from linkedStack import LinkedStack

def getOut(startRow, startCol, maze, showProcess=False):
   """Finds a way out of the maze, if it exists."""
   choices = LinkedStack()
   choices.push(findStartPos(maze))
   
   while not choices.isEmpty():
      c = choices.pop()
      if maze[c[1]][c[0]] == "G":
         return True
      else:
         maze[c[1]][c[0]] = "."
         
         if showProcess:
            print(maze)
            input()
         
         
         for newX, newY in [(c[0]+1, c[1]), (c[0]-1, c[1]),
                            (c[0], c[1]+1), (c[0], c[1]-1)]:
            
            if newX >= 0 and newX < maze.getWidth() and \
               newY >= 0 and newY < maze.getHeight() and \
               maze[newY][newX] not in ".*":
               choices.push((newX, newY))
      
   return False

def getMazeFromFile():
   """Reads the maze from a text file and returns a grid thatrepresents it."""
   name = input("Enter a file name for the maze: ")
   fileObj = open(name, 'r')
   firstLine = list(map(int, fileObj.readline().strip().split()))
   rows = firstLine[0]
   columns = firstLine[1]
   maze = Grid(rows, columns, "*")
   for row in range(rows):
      line = fileObj.readline().strip()
      column = 0
      for ch in line:
         maze[row][column] = ch
         column += 1
   return maze

def findStartPos(maze):
   """Returns the position of the start symbol in the grid."""
   for row in range(maze.getHeight()):
      for column in range(maze.getWidth()):
         if maze[row][column] == 'S':
            return(column, row)
   
   return(-1, -1)

def main():
   maze = getMazeFromFile()
   print(maze)
   (startRow, startCol) = findStartPos(maze)
   success = getOut(startRow, startCol, maze, True)
   if success:
      print("Maze solved:")
      print(maze)
   else:
      print("No path out of this maze")
      
      
if __name__ == "__main__":
   main()