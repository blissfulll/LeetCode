class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfsRec(node, visited_nodes, stack):

            stack.pop()

            if node not in visited_nodes:
                visited_nodes.append(node)
            
                for key in rooms[node]:
                    # print(rooms[node])
                    # print(key)
                    if key not in visited_nodes:
                        stack.append(key)
                # print(stack)
                # stack = list(set(stack))

            if stack:
                dfsRec(stack[-1], visited_nodes, stack)

            return visited_nodes
            # return set(visited_nodes)

        # print(dfsRec(0, [], [0]))

        # print(len(rooms))

        if len(dfsRec(0, [], [0])) == len(rooms):
            return True
        
        return False
        
