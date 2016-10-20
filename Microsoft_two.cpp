#include<iostream>
#include<vector>
#include<string>
#include<cstdlib>
#include<stdlib.h>
#include<sstream>
#include<limits.h>
using namespace std;

struct Tnode{
    Tnode* left;
    Tnode* right;
    int num;
    int flag;
};

vector<string> split(string s, char delimiter)
{
    vector<string> ret;
    int l = s.length();
    int b = 0,e = 0,i;
    for(i=0;i<l;i++)
    {
        if(s[i]==delimiter){
            e = i;
            ret.push_back(s.substr(b, e - b));
            b = i + 1;
        }
    }
    ret.push_back(s.substr(b, l));
    return ret;
}

string Tobinary(int data){
    string ret = "";
    string s;
    stringstream ss;
    for(int i=0;i<8;i++){
        int n = data % 2;
        ss << n;
        ss >> s;
        ret = s + ret;
        ss.clear();
        data /= 2;
    }
    return ret;
}

void createTree(string flag, string ip, int mask, int num, Tnode* root){
    vector<string> ipDelim = split(ip, '.');
    Tnode* node = root;
    Tnode* tmp;
    for(int i=0;i<ipDelim.size();i++){
        int data = atoi(ipDelim[i].c_str());
        string binaryS = Tobinary(data);
        cout << data<<" "<<binaryS << endl;
        for(int j = 0;j<8;j++){
            if (mask <= 0){
                if (flag == "allow") node->flag = 1;
                else node->flag = 0;
                node->num = num;
                free(tmp);
                //cout <<node->flag <<endl;
                return;
            }
            tmp = (Tnode*)malloc(sizeof(Tnode));
            tmp -> left = NULL;
            tmp -> right = NULL;
            tmp -> flag = -1;
            tmp -> num = -1;
            if(binaryS[j] == '0'){
                mask--;
                if(node->left == NULL)node->left = tmp;
                node = node->left;
            }else{
                mask--;
                if(node->right == NULL)node->right = tmp;
                node = node -> right;
            }
            //cout << binaryS[j]<<" "<<node->flag <<endl;
            free(tmp);
        }
        if (mask <= 0){
            if (flag == "allow") node->flag = 1;
            else node->flag = 0;
            node->num = num;
            cout <<node->flag <<endl;
        }
        //cout <<node->flag <<endl;
    }
    return;
}


int main()
{
    int n,m;
    string filter,ip;
    vector<string> ipDelim;
    Tnode* root = (Tnode*)malloc(sizeof(Tnode));
    root ->left = NULL;
    root ->right = NULL;
    root -> flag = 2;
    while(cin >>n>>m){
        for(int i=0;i<n;i++){
            cin>>filter>>ip;

            ipDelim = split(ip, '/');

            if (ipDelim.size() == 1){
                createTree(filter, ipDelim[0], 32, i, root);
            }else{
                int mask = atoi(ipDelim[1].c_str());
                createTree(filter, ipDelim[0], mask, i, root);
            }
            //cout << root->flag << endl;
        }

        for(int i=0;i<m;i++){
            cin>>ip;
            Tnode* node = root;
            ipDelim = split(ip, '.');
            int now_num = INT_MAX;
            bool ans = true;
            bool over = false;
            for(int j=0;j<ipDelim.size();j++){
                int data = atoi(ipDelim[j].c_str());
                string binaryS = Tobinary(data);
                for(int k=0;k<8;k++){
                    //cout << binaryS[k]<<" "<<node->flag <<endl;
                    if(node->flag != -1){
                        if(node->num < now_num){
                            now_num = node->num;
                            if(node->flag == 1)ans = true;
                            else ans = false;
                        }
                    }
                    if(binaryS[k] == '0' && node->left != NULL)node = node -> left;
                    else if(binaryS[k] == '1' && node->right != NULL)node = node->right;
                    else {
                            over = true;
                            break;
                    }
                }
                if(over)break;
            }
            if(ans)cout << "YES" << endl;
            else cout << "NO" << endl;
        }
    }
    return 0;
}
