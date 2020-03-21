from util import Stack, Queue  # These may come in handy

def earliest_ancestor(ancestors, starting_node):

    q = Queue()
    visited = set()
    most_recent = []


    if has_parents(ancestors,starting_node) is False:
        return -1

    q.enqueue(starting_node)
    while q.size() > 0:

        v = q.dequeue()
        #print(v)
        print(f"Current Node {v}")

        if v not in visited:
            visited.add(v)

            if has_parents(ancestors,v):

                most_recent.clear()

                for parent,child in ancestors:
                    if child == v:
                        q.enqueue(parent)
                        #print(f"queue {parent}")
                        print(f"queueing {parent} as the parents of {v}")

                        most_recent.append(parent)


                print()
            else:
                print(f"{v} has no parents\n")

    return min(most_recent)

def has_parents(ancestors,node):
    children = set()
    for parent, child in ancestors:
        children.add(child)
    if node in children:
        return True
    else:
        return False      


# print(earliest_ancestor(test_ancestors,9))

# ancestor = earliest_ancestor(test_ancestors,6)           
# print(f"The earliest ancestor to the input is {ancestor}")