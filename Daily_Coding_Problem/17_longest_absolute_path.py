'''
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. 
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.
'''

def lengthLongestPath(string):
    stack = [(-1, 0)]
    max_len = 0
    for i in string.split('\n'):
        depth = i.count('\t')
        i = i.replace('\t', '')
        while stack and depth <= stack[-1][0]:
            stack.pop()
        if '.' not in i:
            stack.append((depth, len(i) + stack[-1][1] + 1))
        else:
            max_len = max(max_len, len(i) + stack[-1][1])
    return max_len
    
    
path = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
print(lengthLongestPath(path))