import pandas as pd
import numpy as np
import networkx as nx
import math
# Load data
print("Loading data...")
titles = {}
pubs = []
pub_to_idx = {}
df = pd.read_csv("titles.csv")
for index, row in df.iterrows():
    titles[row['this_publ']] = row['title']
    pub_to_idx[row['this_publ']] = len(pubs)
    pubs.append(row['this_publ'])

years = {}
df = pd.read_csv("years.csv")
for index, row in df.iterrows():
    years[row['this_publ']] = row['year']

authors = {}
df = pd.read_csv("authors.csv")
for index, row in df.iterrows():
    if row['this_publ'] in authors:
        authors[row['this_publ']].add(row['author'])
    else:
        authors[row['this_publ']] = {row['author']}

names = {}
df = pd.read_csv("names.csv")
for index, row in df.iterrows():
    names[row['author']] = row['name']

# Build graph
print("Building graph...")
g = nx.DiGraph()
df = pd.read_csv("citations.csv")
for index, row in df.iterrows():
    src = row['this_publ']
    tar = row['other_publ']
    g.add_edge(pub_to_idx[src], pub_to_idx[tar])

# PageRank
print("Calculating PageRank...")
# start value
nstart = {node: math.exp(-(2025 - years[pubs[node]]) / 2) for node in g.nodes}

pr = nx.pagerank(g, alpha=0.5, nstart=nstart)
pr_list= list(pr.items())
pr_list.sort(key=lambda x: x[1], reverse=True)
paper_rankings = pd.DataFrame(map(lambda x: (pubs[x[0]], titles[pubs[x[0]]], x[1]), pr_list), columns=["id", "title", "score"])
paper_rankings["rank"] = paper_rankings["score"].rank(ascending=False)


paper_rankings["year"] = paper_rankings["id"].map(lambda x: years[x])
paper_rankings.to_csv("paper_rankings.csv", index=False)

# Most influential authors
print("Calculating most influential authors...")
author_pr = {}
for node in g.nodes:
    for author in authors[pubs[node]]:
        weight = pr[node] / len(authors[pubs[node]])
        if author in author_pr:
            author_pr[author] += weight
        else:
            author_pr[author] = weight
author_rankings = pd.DataFrame(map(lambda x: (x[0], names[x[0]], x[1]), author_pr.items()), columns=["id", "name", "score"])
author_rankings.sort_values(by="score", ascending=False, inplace=True)
author_rankings["rank"] = author_rankings["score"].rank(ascending=False)
author_rankings.to_csv("author_rankings.csv", index=False)


