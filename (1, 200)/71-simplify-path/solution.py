class Solution(object):
    def simplifyPath(self, path):
        actions = path.split('/')
        cur_path = ''
        for action in actions:
            if action == '.':
                continue
            if action == '..':
                cur_path = '/'.join(cur_path.split('/')[:-1])
                continue
            if action == '':
                continue
            cur_path += '/' + action
        return cur_path if cur_path else '/'
