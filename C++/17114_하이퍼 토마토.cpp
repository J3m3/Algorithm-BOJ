#include <iostream>
#include <queue>

using namespace std;

int dM[22] = {1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0};
int dN[22] = {0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0};
int dO[22] = {0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0};
int dP[22] = {0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0};
int dQ[22] = {0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0};
int dR[22] = {0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
              -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int dS[22] = {0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
              0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0};
int dT[22] = {0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0,
              0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0};
int dU[22] = {0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0,
              0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0};
int dV[22] = {0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0,
              0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0};
int dW[22] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1};

struct Coord {
    int m, n, o, p, q, r, s, t, u, v, w;
};

int main() {
    int m, n, o, p, q, r, s, t, u, v, w;
    cin >> m >> n >> o >> p >> q >> r >> s >> t >> u >> v >> w;
    int tomatoes[w][v][u][t][s][r][q][p][o][n][m];
    queue<Coord> qu;
    
    for (int W = 0; W < w; W++)
        for (int V = 0; V < v; V++)
            for (int U = 0; U < u; U++)
                for (int T = 0; T < t; T++)
                    for (int S = 0; S < s; S++)
                        for (int R = 0; R < r; R++)
                            for (int Q = 0; Q < q; Q++)
                                for (int P = 0; P < p; P++)
                                    for (int O = 0; O < o; O++)
                                        for (int N = 0; N < n; N++)
                                            for (int M = 0; M < m; M++) {
                                                cin >> tomatoes[W][V][U][T][S][R][Q][P][O][N][M];

                                                if (tomatoes[W][V][U][T][S][R][Q][P][O][N][M] == 1) {
                                                    Coord init_tomato;
                                                    init_tomato.m = M;
                                                    init_tomato.n = N;
                                                    init_tomato.o = O;
                                                    init_tomato.p = P;
                                                    init_tomato.q = Q;
                                                    init_tomato.r = R;
                                                    init_tomato.s = S;
                                                    init_tomato.t = T;
                                                    init_tomato.u = U;
                                                    init_tomato.v = V;
                                                    init_tomato.w = W;
                                                    qu.push(init_tomato);
                                                }
                                            }
    
    while (!qu.empty()) {
        int mm, mn, mo, mp, mq, mr, ms, mt, mu, mv, mw;
        Coord coord = qu.front();
        qu.pop();
        mm = coord.m;
        mn = coord.n;
        mo = coord.o;
        mp = coord.p;
        mq = coord.q;
        mr = coord.r;
        ms = coord.s;
        mt = coord.t;
        mu = coord.u;
        mv = coord.v;
        mw = coord.w;

        for (int i = 0; i < 22; i++) {
            int nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw;
            nm = mm + dM[i];
            nn = mn + dN[i];
            no = mo + dO[i];
            np = mp + dP[i];
            nq = mq + dQ[i];
            nr = mr + dR[i];
            ns = ms + dS[i];
            nt = mt + dT[i];
            nu = mu + dU[i];
            nv = mv + dV[i];
            nw = mw + dW[i];

            if (nm >= m || nm < 0
             || nn >= n || nn < 0
             || no >= o || no < 0
             || np >= p || np < 0
             || nq >= q || nq < 0
             || nr >= r || nr < 0
             || ns >= s || ns < 0
             || nt >= t || nt < 0
             || nu >= u || nu < 0
             || nv >= v || nv < 0
             || nw >= w || nw < 0)
                continue;
            
            if (tomatoes[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] != 0)
                continue;
            
            Coord ncoord;
            ncoord.m = nm;
            ncoord.n = nn;
            ncoord.o = no;
            ncoord.p = np;
            ncoord.q = nq;
            ncoord.r = nr;
            ncoord.s = ns;
            ncoord.t = nt;
            ncoord.u = nu;
            ncoord.v = nv;
            ncoord.w = nw;

            qu.push(ncoord);
            tomatoes[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] += tomatoes[mw][mv][mu][mt][ms][mr][mq][mp][mo][mn][mm] + 1;
        }
    }

    int max_days = 0;
    for (int W = 0; W < w; W++)
        for (int V = 0; V < v; V++)
            for (int U = 0; U < u; U++)
                for (int T = 0; T < t; T++)
                    for (int S = 0; S < s; S++)
                        for (int R = 0; R < r; R++)
                            for (int Q = 0; Q < q; Q++)
                                for (int P = 0; P < p; P++)
                                    for (int O = 0; O < o; O++)
                                        for (int N = 0; N < n; N++)
                                            for (int M = 0; M < m; M++) {
                                                if (tomatoes[W][V][U][T][S][R][Q][P][O][N][M] == 0) {
                                                    cout << -1;
                                                    return 0;
                                                }
                                                if (max_days < tomatoes[W][V][U][T][S][R][Q][P][O][N][M])
                                                    max_days = tomatoes[W][V][U][T][S][R][Q][P][O][N][M];
                                            }

    cout << max_days - 1;

    return 0;
}