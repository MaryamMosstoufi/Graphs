def earliest_ancestor(ancestors, starting_node):
    dic = {}
    for each in ancestors:
        if each[1] not in dic:
            dic[each[1]] = [each[0]]
        else:
            dic[each[1]].append(each[0])

    if starting_node not in dic:
        return - 1
    else:
        visited = set()
        paths = []
        s = [[starting_node]]

        while len(s) > 0:
            cur_path = s[-1]
            cur_node = cur_path[-1]
            s.pop()
            if cur_node not in dic:
                paths.append(cur_path)
            elif cur_node not in visited:
                visited.add(cur_node)
                for parent in dic[cur_node]:
                    new_path = list(cur_path)
                    new_path.append(parent)
                    s.append(new_path)
        longest_path = []
        for path in paths:
            if len(path) > len(longest_path):
                longest_path = path
            elif len(path) == len(longest_path):
                if path[-1] < longest_path[-1]:
                    longest_path = path
        return longest_path[-1]
