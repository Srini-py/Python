# Implement locking in a binary tree. 
# A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

	# is_locked, which returns whether the node is locked
	
	# lock, which attempts to lock the node. If it cannot be locked, then it should return false. 
	# Otherwise, it should lock it and return true.
	
	# unlock, which unlocks the node. If it cannot be unlocked, then it should return false. 
	# Otherwise, it should unlock it and return true.

# You may augment the node to add parent pointers or any other property you would like.

# You may assume the class is used in a single-threaded program, 
# so there is no need for actual locks or mutexes.

# Each method should run in O(h), where h is the height of the tree.


class LockableBinaryTree:
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self._is_locked = False
        self.locked_descendants = 0


    def can_lock(self):
        if self.locked_descendants > 0:
            return False
        
        cur = self.parent
        while cur:
            if cur._is_locked:
                return False
            cur = cur.parent
        return True


    def is_locked(self):
        return self._is_locked


    def lock(self):
        if self.can_lock():
            self._is_locked = True
            
            cur = self.parent
            while cur:
                cur.locked_descendants += 1
                cur = cur.parent
            return True
        return False


    def unlock(self):
        if self.can_lock():
            self._is_locked = False
            
            cur = self.parent
            while cur:
                cur.locked_descendants -= 1
                cur = cur.parent
            return True
        return False