class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        print(dirs)
        stack = []
        output = ''
        for paths in dirs:
            if paths=='..':
                if not stack:
                    continue
                stack.pop()
            elif '/' not in paths and paths!='' and paths!='.':
               stack.append(paths)
        
        if not stack:
            return '/'

        for i in stack:
            output += '/' + i
        return output


