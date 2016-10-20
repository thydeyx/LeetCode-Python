#include<iostream>
#include<queue>
#include<limits.h>
using namespace std;


const int DOWN=1;
const int RIGHT=0;

struct State{
    int x,y;
    int cost;
    int dir;
    State(int _x,int _y, int _cost, int _dir):x(_x),y(_y),cost(_cost),dir(_dir){}
    State():x(0),y(0),cost(0),dir(RIGHT){};
    bool operator < (const State & arg) const
    {
        return this->cost > arg.cost;
    }
};


int main()
{
    int n,m;
    char graph[110][110];
    int vis[110][110][2];
    while(cin >>n>>m){
        priority_queue<State> q;
        //cout << n << " " << m << endl;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++){
                cin >> graph[i][j];
                vis[i][j][0]=INT_MAX;
                vis[i][j][1]=INT_MAX;
            }
            //cout << graph[i] << endl;
        }
        vis[0][0][1] = 0;
        vis[0][0][0] = 0;
        State s;
        s.x=0;
        s.y=0;
        s.cost=0;
        s.dir=RIGHT;

        q.push(s);
        while(!q.empty()){
            State now = q.top();
            int x = now.x;
            int y = now.y;
            q.pop();
            if(x == n - 1 && y == m - 1){
                cout << now.cost << endl;
                break;
            }
            State down;
            down.dir = DOWN;
            if(x + 1 < n){
                down.cost = now.cost;
                if(now.dir == RIGHT && graph[x][y + 1] == '.' && (y + 1) < m){
                    down.cost += 1;
                }

                if(graph[x+1][y] == 'b'){
                    down.cost += 1;
                }
                if(down.cost < vis[x + 1][y][DOWN])
                {
                    down.x = x + 1;
                    down.y = y;
                    vis[x + 1][y][DOWN] = down.cost;
                    q.push(down);
                }

            }
            State right;
            right.dir = RIGHT;
            if(y + 1 < m){
                right.cost = now.cost;
                if(now.dir == DOWN && graph[x + 1][y] == '.' && (x + 1) < n){
                    right.cost += 1;
                }

                if(graph[x][y+1]=='b'){
                    right.cost += 1;
                }
                if(right.cost < vis[x][y+1][RIGHT])
                {
                    right.x = x;
                    right.y = y+1;
                    vis[x][y+1][RIGHT] = right.cost;
                    q.push(right);
                }

            }

        }

    }
    return 0;
}
