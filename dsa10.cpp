#include<iostream>
using namespace std;
# define max 20


class students
{
    int marks[max];
    public:
        students()
        {
            for(int i=0;i<max;i++)
            marks[i]=0;
        }

        void insertheap(int total);
        void displayheap(int total);
        void showmax(int total);
        void showmin();

};

void students::insertheap(int total)
{
    for(int i=1;i<=total;i++)
    {
        cout<<"Enter Marks";
        cin>>marks[i];
        int j=i;
        int par=j/2;
    while(marks[j]<=marks[par]&&j!=0)
    {
        int tmp = marks[j];
        marks[j] = marks[par];
        marks[par] = tmp;
        j=par;
        par=j/2;

    }

    }
}

void students::displayheap(int total)
{
    int i=1,space=6;
    cout<<endl;
    while(i<=total)
    {
        if(i==1 || i==2 || i==4 || i==8 || i==16)
        {
            cout<<endl<<endl;
            for(int j=0;j<space;j++)
            cout<<" ";
            space-=2;
        }
    cout<<" "<<marks[i];i++;
    }   
}

void students::showmax(int total)
{
    int max1=marks[1];
    for(int i=2;i<=total;i++)
    {
        if(max1<marks[i ])
        max1 = marks[i];
    }
    cout<<"Maximum marks : "<<max1;
}

void students::showmin()
{
    cout<<"Minimum marks : "<<marks[1];
}

int main()
{
    int ch,cont,tmp;
    int total;
    students s1;

    do
    {
        cout<<"-----MENU-----"<<endl;
        cout<<"1. Read marks of students"<<endl;
        cout<<"2. Display Min heap"<<endl;
        cout<<"3. Find max Marks"<<endl;
        cout<<"4. Find min Marks"<<endl;
        cout<<"Enter Choice"<<endl;

        cin>>ch;
        switch (ch)
        {
        case 1:
            cout<<"How many Students : ";
            cin>>total;
            s1.insertheap(total);
            break;
        
        case 2:
            s1.displayheap(total);
            break;

        case 3:
            s1.showmax(total);
            break;

        case 4:
            s1.showmin();
            break;

        }
        cout<<endl<<"Do You Want To Continue?(1 for continue)";
        cin>>cont;
    }while (cont==1);
    
        return 0;
}