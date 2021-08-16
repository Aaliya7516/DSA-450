#include <iostream>
using namespace std;

int main() {
	int arr[] = {3,3,43,45,65,654,8,2,123,31,5435,5,54,23,123,12};
	
	int min = arr[0];
	int max = arr[0];
	int l = sizeof(arr)/sizeof(arr[0]);
	
	for (int i = 0; i < l; i++){
	    if (min > arr[i]){
	        min = arr[i];
	    }
	    else if (max < arr[i]){
	        max = arr[i];
	    }
	}
	cout<<min <<"    "<< max;
	
	return 0;
}