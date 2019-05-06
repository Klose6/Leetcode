"""
489 robot room cleaner
"""

class Solution:
  def cleanRoom(self, robot):
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def goback(robot):
      robot.turnLeft()
      robot.turnLeft()
      robot.move()
      robot.turnRight()
      robot.turnRight()

    def dfs(pos, robot, d, visited):
      if pos in visited:
        return
      robot.clean()
      visited.add(pos)
      for i in range(len(dirs)):
        d = (d + i) % len(dirs)
        x, y = pos[0]+dirs[d][0], pos[1]+dirs[d][1]
        if robot.move() and (x, y) not in visited: # return True if the from cell is empty and the robot moves into it
          dfs((x, y), robot, d, visited)
          goback(robot) # need to go back
        robot.turnRight() # change direction after processing the current cell

    dfs((0, 0), robot, 0, set())