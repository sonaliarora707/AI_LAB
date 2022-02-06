#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;
 
vector <vector<pi>> QuesGraph;
 
// Function for adding edges to Graph 

void addEdge(int x, int y, int cost)
{
    QuesGraph[x].push_back(make_pair(cost, y));
    QuesGraph[y].push_back(make_pair(cost, x));
}
 

void Greedy_BFS(int src, int trgt, int n)
{
    vector<bool> visited(n, false);

    priority_queue <pi, vector<pi>, greater<pi> > pq;
    cout<<"Output of the Graph: \n";
    pq.push(make_pair(0, src));
    int s = src;
    visited[s] = true;
    while (!pq.empty()) {
        int x = pq.top().second;

        cout << x << " ";
        pq.pop();
        if (x == trgt)
            break;
 
        for (int i = 0; i < QuesGraph[x].size(); i++) {
            if (!visited[QuesGraph[x][i].second]) {
                visited[QuesGraph[x][i].second] = true;
                pq.push(make_pair(QuesGraph[x][i].first,QuesGraph[x][i].second));
            }
        }
    }
}
 

int main()
{
    int vertex = 14;
    QuesGraph.resize(vertex);

// The nodes are implemented using integers addEdge(x,y,cost);

    addEdge(0, 1, 3);
    addEdge(0, 2, 6);
    addEdge(0, 3, 5);
    addEdge(1, 4, 9);
    addEdge(1, 5, 8);
    addEdge(2, 6, 12);
    addEdge(2, 7, 14);
    addEdge(3, 8, 7);
    addEdge(8, 9, 5);
    addEdge(8, 10, 6);
    addEdge(9, 11, 1);
    addEdge(9, 12, 10);
    addEdge(9, 13, 2);
 
    int src = 0;
    int trgt = 9;
 
    // Function call

    Greedy_BFS(src, trgt, vertex);
 
    return 0;
}