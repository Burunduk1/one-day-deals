/**
 * Sergey Kopeliovich (burunduk30@gmail.com)
 */

#include <cstdio>
#include <random>
#include <numeric>

#define FAST_ALLOCATOR_MEMORY 2e8
#include "optimization.h" // http://acm.math.spbu.ru/~sk1/algo/lib/optimization.h.html

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define all(a) (a).begin(), (a).end()

struct node {
	node *l, *r;
	int x, y;
};
using pnode = node*;

// <=x and >x
void split(pnode v, pnode &l, pnode &r, int x) {
	if (!v)
		l = r = 0;
	else if (v->x <= x)
		split(v->r, v->r, r, x), l = v;
	else
		split(v->l, l, v->l, x), r = v;
}

void insert(pnode &v, int x, int y) {
	if (v && v->y < y)
		insert(x < v->x ? v->l : v->r, x, y);
	else {
		pnode l, r;
		split(v, l, r, x);
		v = new node {l, r, x, y};
	}
}

int cnt = 0;
void merge(pnode &v, pnode l, pnode r) {
	cnt++;
	if (!l || !r)
		v = l ? l : r;
	else if (l->y < r->y)
		merge(l->r, l->r, r), v = l;
	else
		merge(r->l, l, r->l), v = r;

}
void erase(pnode &v, int x) {
	if (v->x != x)
		erase(x < v->x ? v->l : v->r, x);
	else
		merge(v, v->l, v->r);
}

void out(pnode v, int dep = 0) {
	if (!v) return;
	out(v->l, dep + 1);
	printf("%*sx=%d\n", dep * 2, "", v->x);
	out(v->r, dep + 1);
}
int main() {
	// use N=10 to and uncomment debug-output, to test correctness
	const int N = 1e6; 
	mt19937 gen;
	pnode root = 0;
	forn(i, N) {
		insert(root, i, gen());
		// printf("\nafter insert i=%d\n", i);
		// out(root); 
	}

	vector<int> p(N);
	iota(all(p), 0);
	// you may shuffle, if you want
	// shuffle(all(p), gen);
	for (int x : p) {
		erase(root, x);
		// printf("\nafter erase x=%d\n", x);
		// out(root);
	}

	printf("ratio = %.3f\n", 1. * cnt / N);
}
