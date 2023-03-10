#include<iostream>
using namespace std;

class node
{
    int prn;
    char name[10];
    node *next;
    public:
    node()
{
    prn=0;
    next=NULL;
}   
friend class ssl;
};
class ssl
{
	node *head;
	public:
    node* create();
	int count();
	void display(node*);
	node* reverse(node*);
	node* insertpresi();
	void insertmem();
	void insertsec();
	node* remove();
	node* concat(node*,node*);
};

node *ssl::create()
{
	node *neww,*temp=NULL;
	bool first=true;
	char ch='n';
	do
	{
		neww=new node;
		cout<<"Enter PRN number: "<<endl;
		cin>>neww->prn;
		cout<<"Enter Name: "<<endl;
		cin>>neww->name;
		if (first)
		{
			head=neww;
			temp=head;
			first=false;
		}
		else{
			temp->next=neww;
			temp=neww;
		}
		cout<<"Do you want more elements(y/n): "<<endl;
		cin>>ch;
	} while (ch=='y');	
	return head;
}

int ssl::count()
{
	int cnt=0;
	node *temp;
	temp=head;
	if(temp==NULL)
	cout<<"No members present"<<endl;
	while(temp!=NULL)
	{
		temp=temp->next;
		cnt++;
	}
	cout<<"Number of Total Members are: "<<cnt<<endl;
}

void ssl::display(node*head)
{
	node *temp;
	temp=head;
	while(temp!=NULL)
	{
		cout<<"Name is: "<<temp->name<<endl;
		cout<<"PRN is: "<<temp->prn<<endl;
		temp=temp->next;
	}
}

node*  ssl::reverse(node *head)
{
	node *temp,*nxt=NULL,*prev=NULL;
	temp=head;
	while(temp!=NULL)
	{
		nxt=temp->next;
		temp->next=prev;
		prev=temp;
		temp=nxt;
	}
	head=prev;
	return head;
}

node* ssl::remove()
{
	int key;
	node *temp=head,*prev;
	cout<<"Enter prn of member to delete: "<<endl;
	cin>>key;
	while(temp->prn!=key)
	{
		prev=temp;
		temp=temp->next;
	}
	if(temp==NULL)
	{
		cout<<"Member not present!"<<endl;		
	}
	
	else
	{
		if(head==temp)
		head=temp->next;
		else
		{
			prev->next=temp->next;
			delete temp;
		}
	}
	return head;
	
}

node* ssl::insertpresi()
{
	node *temp,*neww=new node;
	cout<<"Enter name: "<<endl;
	cin>>neww->name;
	cout<<"Enter prn: "<<endl;
	cin>>neww->prn;
	if(head==NULL)
	head=neww;
	else
	{
		temp=head;
		head=neww;
		neww->next=temp;
	}
	return head;
}

void ssl::insertsec()
{
	node *neww=new node,*temp;
	cout<<"Enter name: "<<endl;
	cin>>neww->name;
	cout<<"Enter prn: "<<endl;
	cin>>neww->prn;
	if(head==NULL)
	head=neww;
	else
	{
		head=temp;
		while(temp!=NULL)
		{
			temp=temp->next;
		}
		temp->next=neww;
	}
}

void ssl::insertmem()                       
{
	int key;
	node *temp,*New;                            
	New=new node;                               
	cout<<"\n Enter the PRN of the student ";   
	cin>>New->prn;
	cout<<"\n Enter the name of the student: ";  
	cin>>New->name;
	if(head==NULL)                          
		head=New;                        
	else
	{
		cout<<"\n Enter the PRN after which you want to insert the node: ";   
		cin>>key;
		temp=head;                         
		do
		{
			if(temp->prn==key)             
			{
				New->next=temp->next;       
				temp->next=New;            
				break;
			}
			else
				temp=temp->next;            
		}while(temp!=NULL);                 
	}
	cout<<"\n The member is inserted";       
}
node* ssl::concat(node *head1,node *head2)  
{
	node *temp;                                  
	temp=head1;                                  
	while(temp->next!=NULL)                      
		temp=temp->next;                        
	temp->next=head2;                           
	cout<<"\n The lists are concatenated";      
	return head1;
}
int main()
{
	ssl s;                                    
	int ch,ch1;
	char ans='y';                            
	node *start=NULL;
	node *start1,*start2,*start3;            
	start1=NULL;                              
	start2=NULL;                              
	start3=NULL;                              
	do
	{
		cout<<"\n 1. Create.";
	     cout<<"\n 2. Display members";
	     cout<<"\n 3. Insert member";
	     cout<<"\n 4. Delete member";
	     cout<<"\n 5. Total number of members of club";
	     cout<<"\n 6. Display list in reverse using recursion";
	     cout<<"\n 7. Concatenate two lists";
	     cout<<"\n 8. Exit";
		cout<<"\n Enter your choice: ";
		cin>>ch;
		switch(ch)
		{
		     case 1:
			     start=s.create();                    
			     break;
		     case 2:
			     s.display(start);                   
			     break;
		     case 3:
			     cout<<"\n The members are ";         
			     s.display(start);
			     cout<<"\n Menu";
			     cout<<"\n 1. Insert President";    
			     cout<<"\n 2. Insert Member";       
			     cout<<"\n 3. Insert Secretary";    
			     cout<<"\n Enter your choice: ";
			     cin>>ch1;
			     switch(ch1)                            
			     {			   
			          case 1:
				          start=s.insertpresi();  
				          break;
			          case 2:
				          s.insertmem();          
				          break;
			          case 3:
				          s.insertsec();        
				          break;
			     }
			     break;		
		     case 4:
			     start=s.remove();                       
			     break;
		     case 5:
			     s.count();                              
			     break;
		     case 6:
			     s.reverse(start);                       
			     break;
		     case 7:                                      
			     cout<<"\n Enter the data for first division";
			     start1=s.create();
			     cout<<"\n Enter the data for second division";
			     start2=s.create();
			     start3=s.concat(start1,start2);
			     s.display(start3);
			     break;
		}
		cout<<"\n Want to continue to Menu(y/n): ";       
		cin>>ans;
	}while(ans=='y'||ans=='Y');                           

    return 0;
}



