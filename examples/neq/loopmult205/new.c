int foo(int a, int b) {
	int c = 0;
	for (int i=0; i<a; ++i)
		c += b;
	return c;}

int main(int x, char*argv[]) {
	if (x>=183 && x<227)
		return foo(x,205);
	return 0;}