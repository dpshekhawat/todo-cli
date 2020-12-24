import sys
import datetime
date = datetime.date.today().strftime('%d/%m/%Y')

args = sys.argv

help = "todo add 'todo item'\t#Add a new todo\ntodo ls\t\t#Show remaining todos\ntodo del NUMBER\t#Delete a todo\ntodo done NUMBER\t#Complete a todo\ntodo help\t\t#Show usage\ntodo report\t\t#Statistics"
tasks = []

try:
  command = args[1]
except IndexError:
  print(help)
  sys.exit(1)

if command not in ("add", "ls", "del", "done", "help", "report"):
  print(("Invalid command\n Use help to learn more about commands."))

if command == "add":
  task = args[2]
  tasks.append(task)
  file = open("todo.txt", "a")
  file.write(task+"\n")
  file.close()
  print("Added " + "'" + task + "'")
elif command == "ls":
  file = open("todo.txt", "r")
  tasks = file.readlines()
  if len(tasks) == 0:
    print('there are no tasks!')
  else:
    for task in tasks:
      print(task)
  file.close()
elif command == "del":
  try:
    file = open("todo.txt", 'r')
  except IOError as e:
    print(str(e))
    sys.exit(1)

  tasks = file.readlines()
  tasks = [task.strip() for task in tasks]
  task_id = args[2]
  del tasks[int(task_id)]
  file.close()
  file = open("todo.txt", 'w')
  tasks = [task + "\n" for task in tasks]
  file.writelines(tasks)
  print("Deleted todo #" + str(task_id))
elif command == "done":
  file = open("todo.txt", "r")
  tasks = file.readlines()
  tasks = [task.strip() for task in tasks]
  task_id = args[2]
  try:
    if int(task_id) <= len(tasks):
      f1 = open("done.txt", "a")
      f1.write(tasks[int(task_id)])
      del tasks[int(task_id)]
      file = open("todo.txt", 'w')
      tasks = [task + "\n" for task in tasks]
      file.writelines(tasks)
      file.close()
      f1.close()
      print("Marked todo #" + str(task_id) + " as done.")
    else:
      print("Error: todo #" + str(task_id) + " does not exist.")
  except IndexError:
    print("Error: todo #" + str(task_id) + " does not exist.")
elif command == "report":
  try:
    f1 = open("todo.txt", "r")
    todo = f1.readlines()
    f2 = open("done.txt", "r")
    done = f2.readlines()
  except FileNotFoundError:
    todo = []
    done = []
  print(str(date) + " " + "Pending: " + str(len(todo)) + " " + "Completed: " + str(len(done)))
elif command == "help":
  print(help)
else:
  print("Invalid command")