# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        directory_stack = list()
        for directory in directories:
            if not directory == '' and not directory == '.':
                if not directory == '..':
                    directory_stack.append(directory)
                elif directory_stack:
                    directory_stack.pop()
        return f"/{'/'.join(directory_stack)}"
