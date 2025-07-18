#include <iostream>
using namespace std;

void solve() {
	int n; cin >> n;
	int arr[n];

	for (int i = 0; i < n; i++) {
		arr[i] = (3*n)+i;
	}

	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
}


int main() {
	solve();
}

