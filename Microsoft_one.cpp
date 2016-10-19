#include<iostream>
using namespace std;
int check(int mid, int N, int W, int H, int a[])
{
    int page = 0;
    int w = W / mid;
    int h = H / mid;
    int p_w,p_w_y,hang=0;
    for(int i=0;i<N;i++){
        p_w = a[i] / w;
        p_w_y = a[i] % w;
        hang = hang + p_w;
        if(p_w_y != 0)hang ++;
    }
    page = hang / h;
    if(hang % h != 0)page ++;
    return page;
}
int main()
{
    int mid = 0;
    int n,T,N,P,W,H,ans=0,cnt;
    int a[100];
    while(cin>>n){
        for(int T=1;T<=n;T++){
            cin>>N>>P>>W>>H;
            for(int i=0;i<N;i++)
            {
                cin >> a[i];
            }
            int left=1, right=min(W,H);
            while(left <= right){
                mid = (left + right) / 2;
                cnt = check(mid, N, W, H, a);
                if(cnt > P){
                    right = mid - 1;
                }else{
                    ans = mid;
                    left = mid + 1;
                }
            }
            cout<<ans<<endl;
        }
    }
    return 0;
}
