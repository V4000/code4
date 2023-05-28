#include<iostream>
#include<omp.h>
#include<bits/stdc++.h>
using namespace std;
vector<bool> v;
vector<vector<int>> adj;

void makeEdge(int a,int b) {
    adj[a].push_back(b);
}

void bfsTraversal(int a) {
    queue<int> q;
    q.push(a);
    while(!q.empty()) {
        int r=q.front();
        q.pop();
        for(auto i=adj[r].begin();i!=adj[r].end();i++) {
            if(!v[*i]) {
                v[*i]=true;
                q.push(*i);
            }
        }
        cout<<r<<" ";
    }

}

int main() {
    omp_set_num_threads(4);
    int n,e;
    cout<<"\nEnter number of vertices and number of edges";
    cin>>n>>e;
    cout<<"\nEnter starting and ending point of edges start with 0 vertice";
    int a,b;
    v.assign(n,false);
    adj.assign(n,vector<int>());
    for(int i=0;i<e;i++) {
        cin>>a>>b;
        makeEdge(a,b);
    }
    for(int i=0;i<n;i++) {
        if(!v[i]) {
            bfsTraversal(i);
        }
    }
    return 0;
}


Output - 
Enter number of vertices and number of edges6
8

Enter starting and ending point of edges start with 0 vertice0 1
0 2
1 3
1 4
2 4
3 5
4 5
3 4
BFS Traversal - 
0 1 2 3 4 5
