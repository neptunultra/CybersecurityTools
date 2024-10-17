#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* adjList[100];
void addedge(int u, int v){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = v;
newNode->next = adjList[u];
adjList[u] = newNode;
}
void printGraph(int V){
    for (int i = 0; i < v; i++){
        printf("Adjacency list of vertex %d: ". i);
        struct Node* temp = adjList[i];
        while (temp !=NULL){
            printf("%d -> ", temp->data);
            temp = temp->next
        }
        printf("NULL\n");
    }
}
int main() {
    int V, E;
    printf("Enter the number of vertices: ");
    scanf("%d", &V);
    printf("Enter the number of edges: ");
    scanf("%d", &E);

    for (int i = 0; i   
 < V; i++) {
        adjList[i] = NULL;
    }

    for (int i = 0; i < E; i++) {
        int u, v;
        printf("Enter the edge (u v): ");
        scanf("%d %d", &u, &v);
        addEdge(u, v);
        // For undirected graphs, addEdge(v, u);
    }

    printGraph(V);

    return 0;
}

