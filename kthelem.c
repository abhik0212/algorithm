#include<stdio.h>
#include<stdlib.h>
int medianofmedians(int *a,int size);
int medoffive(int *a,int start,int length);
int partition(int *arr, int lower, int upper, int pivot);
int findkth(int *a,int lower,int upper, int k);
int findpos(int *a,int pivotelem);
int main()
{
	int arr[]={3,11,2,10,15,1,6,8,7,4,9,4,3,10,7,14};
	int size=sizeof(arr)/sizeof(int);
	int k=4;
	//int val= medianofmedians(arr,size);
	//printf("val=%d",val);

	printf("element at pos %d is %d\n",k,findkth(arr,0,size-1,k));
	return 0;
}
int findkth(int *a,int lower,int upper, int k)
{
	int pivotelem=medianofmedians(a,upper+1);
	//printf("pivot=%d",pivot);
	int i,j;
	int positionbeforepartition=findpos(a,pivotelem);
	for(i=lower;i<=upper;i++)
		printf("%d ",a[i]);
	printf("\n");
	int pos=partition(a,lower,upper,positionbeforepartition);
	
	for(i=lower;i<=upper;i++)
		printf("%d ",a[i]);
	printf("\n");
	printf("pivotelem=%d positionbeforepartition=%d pos=%d k=%d upper=%d\n",pivotelem,positionbeforepartition,pos,k,upper);
	//sleep(1);
	if(pos==k)
		return a[pos];
	if(pos<k)
		return(findkth(a+pos+1,0,upper-pos-1,k-pos-1));
	else
		return(findkth(a,0,pos-1,k));
}
int findpos(int *a,int pivotelem)
{
	int i=0;
	while(1)
	{
		if(a[i]==pivotelem)
			return i;
		i++;
	}

}
int medianofmedians(int *a,int size)
{
	int i,newsize,*new,index,val;
	if(size==1) return a[0];
	if(size%5==0) newsize=size/5;
	else newsize=size/5 +1;		
	new=(int*) malloc(sizeof(int) * newsize);
	index=0;
	i=0;
	while(1)
	{
		//printf("i=%d size=%d",i,size);
		if(i<=size-5)
		{
			val=med(a,i,5);
			new[index]=val;
			//printf("hi1 %d\n",val);
			i+=5;
			index++;
		}
		else
		{
			val=med(a,i,size-i);
			new[index]=val;
			//printf("hi2 %d\n",val);
			//new[index]=med(a,i,size-i);
			break;
		}
		
	}
	return (medianofmedians(new,newsize));
}

int med(int *arr,int start, int length)
{
	int i,j=0,Temp,A[length];
	for(i=start;i<start+length;i++)
	{	
		A[j]=arr[i];
		//printf("%d ",A[j]);
		j++;
	}
	for(i=0; i<length; i++)
	{
		Temp = A[i];
		j = i-1;
		while(Temp<A[j] && j>=0)
		{
			A[j+1] = A[j];
			j = j-1;
		}
		A[j+1] = Temp;
	}
	return A[length/2];
}
int partition(int *arr, int lower, int upper, int pivot)
{
	int temp,i,j;
	//printf("\nin partitionfunction: before partition\n");
	//for(i=lower;i<=upper;i++)
	//	printf("%d ",arr[i]);
	//printf("\n");
	i=lower-1;
	j=upper+1;
	
	while(1)
	{
		do {i++;}
		while(arr[i]<=arr[pivot] && i<upper);
		do{j--;}
		while(arr[j]>=arr[pivot] && j>lower);
		
		if(i<j)
		{
			temp=arr[i];
			arr[i]=arr[j];
			arr[j]=temp;
			//i--;
			//j++;
			
		}
		else
		{
			if(j>pivot)
			{
				temp=arr[pivot];
				arr[pivot]=arr[j];
				arr[j]=temp;
				return j;
			}
			else if (i<pivot)
			{
				temp=arr[pivot];
				arr[pivot]=arr[i];
				arr[i]=temp;
				return i;
				
			}
			else
				return pivot;
		}
	}	
}
