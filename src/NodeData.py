class Node(object):
    """ Node class """

    def __init__(self, num: int, pos: tuple):
        self.id = num
        self.out = {}  # Edges from this node to other nodes
        self.In = {}  # Edges from other nodes to this node
        self.distance = "inf"
        self.previous_node = None
        self.pos = pos

    def add_out(self, node_id: int, weight: float):
        self.out[node_id] = weight

    def add_in(self, node_id: int, weight: float):
        self.In[node_id] = weight

    def get_out(self):
        return self.out

    def get_in(self):
        return self.In

    def get_id(self):
        return self.id

    def get_previous_node(self):
        return self.previous_node

    def set_previous_node(self, node):
        self.previous_node = node

    def get_distance(self):
        return self.distance

    def set_distance(self, dist: float):
        self.distance = dist

    def get_weight(self, node_id):
        return self.out[node_id]

    def get_node(self):
        return self

    def get_pos(self):
        return self.pos

    def set_pos(self, pos: tuple):
        self.pos = pos

    def __repr__(self):
        return "|edges out| " + self.out.__str__() + " |edges in| " + self.In.__str__()

    def __lt__(self, other):
        if self.get_distance() == "inf" and other.get_distance() == "inf":
            return 0
        if self.get_distance() == "visited" and other.get_distance() == "visited":
            return 0
        if self.get_distance() == "inf":
            return -1
        if other.get_distance() == "inf":
            return 1
        return self.get_distance() < other.get_distance()
