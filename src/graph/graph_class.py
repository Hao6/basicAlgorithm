
# coding: utf-8

# # 定义 class graph 
# - 使用邻接矩阵表示图(包括有向图与无向图)  
# - 邻接矩阵是个方阵，记为$M_{nn}$,其中$M_{ij}$表示顶点$i$与顶点$j$之间是否存在一条边；具体来说，如果不是带有边权重的图，则$M_{ij} = 0$表示顶点$i$与顶点$j$之间不存在一条边，而$M_{ij} = 1$表示顶点$i$与顶点$j$之间存在一条边；如果是带有边权重的图，则$M_{ij} != 0$表示的是顶点$i$与顶点$j$之间边的权重
# - 如果是无向图，则最终的邻接矩阵是对称的，否则就不一定

# In[1]:


class graph:
    # 使用邻接矩阵便可以构造出图
    def __init__(self, g_matrix, is_directed=True, vertexs = None, edges = None):
        self.is_directed = is_directed # 是否是有向图
        self.vertexs = vertexs              # 顶点集合
        self.edges   = edges              # 边集合，使用(vertex_x,vertex_y)表示顶点x与y之间的一条边
        self.graph_matrix = g_matrix         # 邻接矩阵
    # 判断两个顶点之间是否有一条边
    def is_edges(self,vertex_x,vertex_y):
        return self.graph_matrix[vertex_x][vertex_y] != 0
    # 删除两个顶点之间的一条边
    def del_edges(self,vertex_x,vertex_y):
        if self.is_edges(vertex_x,vertex_y) == True:
            self.graph_matrix[vertex_x][vertex_y] = 0
            if self.is_directed == False:
                self.graph_matrix[vertex_y][vertex_x] = 0
            if self.edges != None and (vertex_x,vertex_y) in self.edges:
                self.edges.remove((vertex_x,vertex_y))
                if self.is_directed == False:
                    self.edges.remove((vertex_y,vertex_x))
                
    # 添加一条边
    def add_edges(self,vertex_x, vertex_y ,weight):
        self.graph_matrix[vertex_x][vertex_y] = weight
        if self.is_edges(vertex_x,vertex_y) == False:
            if self.is_directed == False:
                self.graph_matrix[vertex_y][vertex_x] = weight
            if self.edges != None and (vertex_x, vertex_y) not in self.edges:
                self.edges.append((vertex_x, vertex_y))
                if self.is_directed == False:
                    self.edges.append((vertex_y, vertex_x))
            


    # 生成顶点集合
    def build_vertexs(self):
        if self.vertexs == None:
            self.vertexs = [i for i in range(len(self.graph_matrix))]
    
    # 生成边集合
    def build_edges(self):
        if self.edges == None:
            self.edges = [] # 初始化一个空的边集合
            for i in range(len(self.graph_matrix)):
                for j in range(len(self.graph_matrix)):
                    if self.is_edges(i,j)==True:
                        self.edges.append((i,j))


# ## class graph 的一些test 

# In[2]:


temp_graph = [[0,3,0],[3,0,4],[0,4,0]]
g_a = graph(temp_graph, is_directed=False)


# In[3]:


print g_a.edges


# In[4]:


print g_a.vertexs


# In[5]:


print g_a.graph_matrix


# In[6]:


g_a.build_edges()
print g_a.edges


# In[7]:


g_a.build_vertexs()
print g_a.vertexs


# In[8]:


for i in range(len(temp_graph)):
    for j in range(len(temp_graph)):
        print g_a.is_edges(i,j)


# In[9]:


for i in range(len(temp_graph)):
    for j in range(len(temp_graph)):
        g_a.del_edges(i,j)


# In[10]:


print g_a.edges


# In[11]:


for i in range(len(temp_graph)):
    for j in range(len(temp_graph)):
        print g_a.is_edges(i,j)


# In[12]:


# try:
#     get_ipython().system(u'jupyter nbconvert --to python graph_class.ipynb')
# except:
#     pass

