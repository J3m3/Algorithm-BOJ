use std::{collections::BinaryHeap, io::*};

#[derive(Clone)]
struct Edge(i32, usize);

fn dijkstra(graph: &Vec<Vec<Edge>>, dist: &mut Vec<i32>, s: usize, t: usize) -> i32 {
    dist[s] = 0;

    let mut pq: BinaryHeap<(i32, usize)> = BinaryHeap::new();
    pq.push((-dist[s], s));

    while let Some((this_w, this)) = pq.pop() {
        let this_w = -this_w;

        if this_w > dist[this] {
            continue;
        }
        if this == t {
            return dist[t];
        }
        for &Edge(child_w, child) in graph[this].iter() {
            let n_dist = this_w + child_w;
            if dist[child] > n_dist {
                dist[child] = n_dist;
                pq.push((-n_dist, child));
            }
        }
    }
    dist[t]
}

fn main() {
    let stdin = read_to_string(stdin().lock()).unwrap();
    let mut tokens = stdin.split_ascii_whitespace();
    let mut next = || tokens.next().unwrap().parse::<usize>().unwrap();

    let n = next();
    let m = next();

    let mut dist: Vec<i32> = vec![i32::MAX; n + 1];
    let mut graph: Vec<Vec<Edge>> = vec![vec![]; n + 1];
    for _ in 0..m {
        let a = next();
        let b = next();
        let c = next() as i32;

        graph[a].push(Edge(c, b));
        graph[b].push(Edge(c, a));
    }

    let s = next();
    let t = next();
    let answer = dijkstra(&graph, &mut dist, s, t);

    println!("{answer}");
}
