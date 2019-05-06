"""
489 robot room cleaner
"""

class Solution:
  def cleanRoom(self, robot):
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1)) # up, right, down, left, turn right for each one to get the next direction

    def goback(robot):
      robot.turnLeft()
      robot.turnLeft()
      robot.move()
      robot.turnRight()
      robot.turnRight()

    def dfs(pos, robot, d, visited):
      robot.clean()
      visited.add(pos)
      for i in range(len(dirs)):
        d = (d + i) % len(dirs)
        x, y = pos[0]+dirs[d][0], pos[1]+dirs[d][1]
        if (x, y) not in visited and robot.move(): # return True if the from cell is empty and the robot moves into it
          dfs((x, y), robot, d, visited)
          goback(robot) # need to go back
        robot.turnRight() # need to change the direction when meets obstacle, also need to change the direction for up, right, down and left

    dfs((0, 0), robot, 0, set())