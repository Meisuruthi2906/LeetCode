from sortedcontainers import SortedList

class TaskManager:
    def __init__(self, tasks):
        
        self.task_info = {}
        self.sorted_tasks = SortedList()
        for user, tid, pri in tasks:
            self.add(user, tid, pri)

    def add(self, userId, taskId, priority):
        self.task_info[taskId] = (userId, priority)
        self.sorted_tasks.add( (-priority, -taskId) )

    def edit(self, taskId, newPriority):
        userId, oldPri = self.task_info[taskId]
        self.sorted_tasks.discard( (-oldPri, -taskId) )
        self.task_info[taskId] = (userId, newPriority)
        self.sorted_tasks.add( (-newPriority, -taskId) )

    def rmv(self, taskId):
        userId, priority = self.task_info.pop(taskId)
        self.sorted_tasks.remove( (-priority, -taskId) )

    def execTop(self):
        if not self.sorted_tasks:
            return -1
        negPri, negTid = self.sorted_tasks.pop(0)  
        taskId = -negTid
        userId, _ = self.task_info.pop(taskId)
        return userId
